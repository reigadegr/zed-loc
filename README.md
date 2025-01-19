<!---![zed](https://avatars.githubusercontent.com/u/79345384?s=200&v=4)--->
# 🌏 zed-loc (Zed 汉化)

简体中文|[English](README.en.md)

## 项目简介

`zed-loc` 是一个用于本地化 [Zed 编辑器](https://github.com/zed-industries/zed)的工具。它提取源代码中的字符串并生成 JSON 文件，以便进行翻译和本地化，同时支持替换后直接构建可执行文件。

## 特性

- 自动提取源代码中的字符串
- 生成 JSON 文件，便于翻译
- GitHub Actions 集成，自动构建和发布
- 目前每晚手动执行一次汉化构建

## 运行
### 配置
请确保您已安装 Python3 和 Rust。

运行以下命令克隆项目，或直接点击右上角“代码”下载压缩包：

```bash
git clone https://github.com/tc999/zed-loc.git
cd zed-loc
```
### 提取词条

> [!note]
>
> 注意：提取词条只能在 Windows 系统上运行，在 Linux，Macos 上会报错。

首先你需要自行同步 Zed 源码到本地：

```bash
git clone https://github.com/zed-industries/zed.git
```

提取词条，默认保存至`strings.json`文件：
```bash
python3 extract.py
```
删除多余词条，删除规则保存在`del.yaml`文件中：
```bash
python3 delete.py
```

### 翻译词条
> [!caution]
>
> 警告：提取脚本规则是将引号内所有内容全部提取，翻译时请对照 Zed 源码翻译，同时留意不需要翻译的内容。
> 如有不需要翻译的词条请直接删除

翻译方法：丢给 GPT 机翻，再进行人工修正

然后将`strings.json`文件另存为，以目标语言代码为文件名，词条翻译完成后，执行以下命令替换词条：
```bash
python3 replace.py
```

### 构建
如果编译报错，删除 Zed 源码后重新克隆

```bash
cd zed
cargo run
```

确保能够正常编译运行。

# 鸣谢

- [Zed](https://github.com/zed-industries/zed) - Zed 编辑器的所有贡献者
- [deevus/zed-windows-builds](https://github.com/deevus/zed-windows-builds) - Zed Windows 构建脚本参考
- [Nriver/zed-translation](https://github.com/Nriver/zed-translation) - 提供思路
- [GitHub Copilot](https://github.com/copilot) - 脚本编写

## 感谢所有贡献者

一如既往，感谢我们出色的贡献者❤️！

<a href="https://github.com/TC999" title="陈生杂物房">
  <img src="https://avatars.githubusercontent.com/u/88823709?v=4" width="42;" alt="陈生杂物房"/>
</a>
<a href="https://github.com/shenjackyuanjie" title="shenjack">
  <img src="https://avatars.githubusercontent.com/u/54507071?v=4" width="42;" alt="shenjack"/>
</a>

# 许可证

本项目基于 [MIT 许可证](LICENSE)发布，允许任何组织和个人免费使用。
