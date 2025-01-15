import json
import yaml

# 定义文件路径
json_file_path = 'string.json'
yaml_file_path = 'del.yaml'

# 读取JSON文件内容
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

# 读取YAML文件内容
with open(yaml_file_path, 'r', encoding='utf-8') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

# 获取全局删除规则
global_keys_to_delete = yaml_data.get('global', [])

# 遍历JSON数据并删除全局规则中的键
for file_path, file_data in json_data.items():
    for key in global_keys_to_delete:
        if key in file_data:
            del file_data[key]

# 遍历YAML数据并删除JSON数据中的对应项
for file_path, keys_to_delete in yaml_data.items():
    if file_path == 'global':
        continue
    if file_path in json_data:
        for key in keys_to_delete:
            if key in json_data[file_path]:
                del json_data[file_path][key]

# 将修改后的内容写回JSON文件
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

print('Successfully deleted specified keys from string.json')
