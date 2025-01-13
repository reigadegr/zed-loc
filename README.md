![zed](https://avatars.githubusercontent.com/u/79345384?s=200&v=4)
# 🌏 zed-localization (Zed 本地化)
## 项目简介

`zed-loc` 是一个用于本地化 Zed 编辑器的工具。它提取源代码中的字符串并生成 JSON 文件，以便进行翻译和本地化。

## 特性

- 自动提取源代码中的字符串
- 生成 JSON 文件，便于翻译
- GitHub Actions 集成，自动构建和发布

## 运行
### 配置
请确保您已安装 Python3 和 Rust。

运行以下命令克隆项目，或直接点击右上角“代码”下载压缩包：

```bash
git clone https://github.com/tc999/zed-loc.git
cd zed-loc
```
### 提取词条 && 替换

> [!note]
> 
> 注意：提取、替换词条只能在 Windows 系统上运行，在Linux，Macos 上会报错。

首先你需要自行同步 Zed 源码到本地：

```bash
git clone https://github.com/zed-industries/zed.git
```

提取词条，默认保存至`strings.json`文件：
```bash
python3 extract.py
```

> [!caution]
> 
> 警告：提取脚本规则是将引号内所有内容全部提取，翻译时请留意不需要翻译的内容。
> 如有不需要翻译的词条请直接删除

然后将`strings.json`文件另存为，以目标语言代码为文件名，词条翻译完成后，执行以下命令替换词条：
```bash
python3 replace.py
```

编译测试，

```bash
cd zed
cargo run
```

确保能够正常编译运行。

# 许可证

本项目基于 [MIT 许可证](LICENSE)发布，允许任何组织和个人免费使用。