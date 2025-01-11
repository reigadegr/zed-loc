import re
import json
import os

# 定义文件路径列表
input_file_paths = [
    r'zed\crates\activity_indicator\src\activity_indicator.rs',
    # anthropic
    r'zed\crates\anthropic\src\anthropic.rs',
    # r'zed\crates\anthropic\src\supported_countries.rs',
    r'zed\crates\assets\src\assets.rs',
    # assistant
    r'zed\crates\assistant\src\assistant_panel.rs',
    r'zed\crates\assistant\src\assistant_settings.rs',
    r'zed\crates\assistant\src\context_store.rs',
    r'zed\crates\assistant\src\context.rs',
    r'zed\crates\assistant\src\inline_assistant.rs',
    r'zed\crates\assistant\src\patch.rs',
    r'zed\crates\assistant\src\prompt_library.rs',
    r'zed\crates\assistant\src\prompts.rs',
    r'zed\crates\assistant\src\slash_command_picker.rs',
    r'zed\crates\assistant\src\slash_command.rs',
    r'zed\crates\assistant\src\streaming_diff.rs',
    r'zed\crates\assistant\src\terminal_inline_assistant.rs',
    # assistant_slash_command
    r'zed\crates\assistant_slash_command\src\assistant_slash_command.rs',
    # assistant_tools
    r'zed\crates\assistant_tools\src\now_tool.rs',
    # assistant2
    r'zed\crates\assistant2\src\active_thread.rs',
    r'zed\crates\assistant2\src\assistant_model_selector.rs',
    r'zed\crates\assistant2\src\assistant_panel.rs',
    r'zed\crates\assistant2\src\assistant_settings.rs',
    r'zed\crates\assistant2\src\buffer_codegen.rs',
    r'zed\crates\assistant2\src\context_store.rs',
    r'zed\crates\assistant2\src\context_strip.rs',
    r'zed\crates\assistant2\src\context.rs',
    r'zed\crates\assistant2\src\inline_assistant.rs',
    r'zed\crates\assistant2\src\inline_prompt_editor.rs',
    r'zed\crates\assistant2\src\message_editor.rs',
    r'zed\crates\assistant2\src\prompts.rs',
    r'zed\crates\assistant2\src\streaming_diff.rs',
    r'zed\crates\assistant2\src\terminal_inline_assistant.rs',
    r'zed\crates\assistant2\src\thread_history.rs',
    r'zed\crates\assistant2\src\thread_store.rs',
    r'zed\crates\assistant2\src\thread.rs',
    r'zed\crates\assistant2\src\context_picker\directory_context_picker.rs',
    r'zed\crates\assistant2\src\context_picker\fetch_context_picker.rs',
    r'zed\crates\assistant2\src\context_picker\file_context_picker.rs',
    r'zed\crates\assistant2\src\context_picker\thread_context_picker.rs',
    r'zed\crates\assistant2\src\ui\context_pill.rs',
    # audio
    r'zed\crates\audio\src\assets.rs',
    # auto_update
    r'zed\crates\auto_update\src\auto_update.rs',
    # auto_update_ui
    r'zed\crates\auto_update_ui\src\update_notification.rs',
    # breadcrumbs
    r'zed\crates\breadcrumbs\src\breadcrumbs.rs',
    # call
    r'zed\crates\call\src\cross_platform\mod.rs',
    r'zed\crates\call\src\cross_platform\participant.rs',
    r'zed\crates\call\src\cross_platform\room.rs',
    r'zed\crates\call\src\macos\mod.rs',
    r'zed\crates\call\src\macos\participant.rs',
    r'zed\crates\call\src\macos\room.rs',
    # channel
    r'zed\crates\channel\src\channel_buffer.rs',
    r'zed\crates\channel\src\channel_chat.rs',
    r'zed\crates\channel\src\channel_store.rs',
    # cli
    r'zed\crates\cli\src\main.rs',
    # client
    r'zed\crates\client\src\client.rs',
    r'zed\crates\client\src\socks.rs',
    r'zed\crates\client\src\telemetry.rs',
    r'zed\crates\client\src\test.rs',
    r'zed\crates\client\src\user.rs',
    # clock
    r'zed\crates\clock\src\clock.rs',
    # coolab
    r'zed\crates\collab\src\api\billing.rs',
    r'zed\crates\collab\src\api\contributors.rs',
    r'zed\crates\collab\src\api\events.rs',
    r'zed\crates\collab\src\api\extensions.rs',
    r'zed\crates\collab\src\api\ips_file.rs',
    r'zed\crates\collab\src\bin\dotenv.rs',
    r'zed\crates\collab\src\db\queries\access_tokens.rs',
    r'zed\crates\collab\src\db\queries\billing_preferences.rs',
    r'zed\crates\collab\src\db\queries\buffers.rs',
    r'zed\crates\collab\src\db\queries\channels.rs',
    r'zed\crates\collab\src\db\queries\contacts.rs',
    r'zed\crates\collab\src\db\queries\extensions.rs',
    r'zed\crates\collab\src\db\queries\messages.rs',
    r'zed\crates\collab\src\db\queries\notifications.rs',
    r'zed\crates\collab\src\db\queries\projects.rs',
    r'zed\crates\collab\src\db\queries\rooms.rs',
    r'zed\crates\collab\src\db\queries\users.rs',
    # coolab_ui
    r'zed\crates\collab_ui\src\chat_panel\message_editor.rs',
    r'zed\crates\collab_ui\src\collab_panel\channel_modal.rs',
    r'zed\crates\collab_ui\src\collab_panel\contact_finder.rs',
    r'zed\crates\collab_ui\src\notifications\stories\collab_notification.rs',
    r'zed\crates\collab_ui\src\notifications\incoming_call_notification.rs',
    r'zed\crates\collab_ui\src\notifications\project_shared_notification.rs',
    r'zed\crates\collab_ui\src\channel_view.rs',
    r'zed\crates\collab_ui\src\chat_panel.rs',
    r'zed\crates\collab_ui\src\collab_panel.rs',
    r'zed\crates\collab_ui\src\collab_ui.rs',
    r'zed\crates\collab_ui\src\notification_panel.rs',
    # command_palette
    r'zed\crates\command_palette\src\command_palette.rs',
    # copilot
    r'zed\crates\copilot\src\copilot_chat.rs',
    r'zed\crates\copilot\src\copilot.rs',
    r'zed\crates\copilot\src\sign_in.rs',
    # db
    r'zed\crates\db\src\db.rs',
    r'zed\crates\db\src\query.rs',
    # diagnostics
    r'zed\crates\diagnostics\src\diagnostics_tests.rs',
    r'zed\crates\diagnostics\src\diagnostics.rs',
    r'zed\crates\diagnostics\src\items.rs',
    r'zed\crates\diagnostics\src\toolbar_controls.rs',
    # docs_preprocessor
    r'zed\crates\docs_preprocessor\src\main.rs',
    # editor
    r'zed\crates\editor\src\git\blame.rs',
    r'zed\crates\editor\src\git\project_diff.rs',
    r'zed\crates\editor\src\blame_entry_tooltip.rs',
    r'zed\crates\editor\src\clangd_ext.rs',
    r'zed\crates\editor\src\code_context_menus.rs',
    r'zed\crates\editor\src\display_map.rs',
    r'zed\crates\editor\src\editor_settings_controls.rs',
    r'zed\crates\editor\src\editor_tests.rs',
    r'zed\crates\editor\src\editor.rs',
    r'zed\crates\editor\src\element.rs',
    r'zed\crates\editor\src\git.rs',
    r'zed\crates\editor\src\hover_links.rs',
    r'zed\crates\editor\src\hover_popover.rs',
    r'zed\crates\editor\src\hunk_diff.rs',
    r'zed\crates\editor\src\indent_guides.rs',
    r'zed\crates\editor\src\inlay_hint_cache.rs',
    r'zed\crates\editor\src\inline_completion_tests.rs',
    r'zed\crates\editor\src\items.rs',
    r'zed\crates\editor\src\linked_editing_ranges.rs',
    r'zed\crates\editor\src\lsp_ext.rs',
    r'zed\crates\editor\src\mouse_context_menu.rs',
    r'zed\crates\editor\src\movement.rs',
    r'zed\crates\editor\src\persistence.rs',
    r'zed\crates\editor\src\proposed_changes_editor.rs',
    r'zed\crates\editor\src\rust_analyzer_ext.rs',
    # extensions
    r'zed\crates\extension\src\extension_builder.rs',
    r'zed\crates\extension\src\extension_host_proxy.rs',
    r'zed\crates\extension\src\extension_manifest.rs',
    r'zed\crates\extension\src\extension.rs',
    r'zed\crates\extension\src\types.rs',
    # extension_api
    r'zed\crates\extension_api\src\extension_api.rs',
    r'zed\crates\extension_api\src\http_client.rs',
    r'zed\crates\extension_api\src\settings.rs',
    # extension_cli
    r'zed\crates\extension_cli\src\main.rs',
    # extensions_ui
    r'zed\crates\extensions_ui\src\components\extension_card.rs',
    r'zed\crates\extensions_ui\src\components\feature_upsell.rs',
    r'zed\crates\extensions_ui\src\extension_suggest.rs',
    r'zed\crates\extensions_ui\src\extension_version_selector.rs',
    r'zed\crates\extensions_ui\src\extensions_ui.rs',
    # command_palette_hooks
    r'zed\crates\command_palette_hooks\src\command_palette_hooks.rs',
    # zed
    r'zed\crates\zed\src\main.rs',
    r'zed\crates\zed\src\reliability.rs',
    r'zed\crates\zed\src\zed.rs',
    r'zed\crates\zed\src\zed\app_menus.rs',
    r'zed\crates\zed\src\zed\mac_only_instance.rs',
    r'zed\crates\zed\src\zed\open_listener.rs',
    r'zed\crates\zed\src\zed\quick_action_bar.rs',
    r'zed\crates\zed\src\zed\windows_only_instance.rs',
    r'zed\crates\zed\src\zed\quick_action_bar\markdown_preview.rs',
    r'zed\crates\zed\src\zed\quick_action_bar\repl_menu.rs',
]
output_file_path = 'string.json'

# 初始化JSON数据
json_data = {}

# 遍历每个文件路径
for input_file_path in input_file_paths:
    # 读取文件内容
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式查找所有引号中的字符串
    pattern = r'"(.*?)"'
    matches = re.findall(pattern, content)

    # 构建JSON数据
    json_data[input_file_path.replace('\\', '/')] = {match: "" for match in matches}

# 将JSON数据写入文件
with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

print(f'Successfully extracted strings to {output_file_path}')