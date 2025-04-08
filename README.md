<!---![zed](https://avatars.githubusercontent.com/u/79345384?s=200&v=4)--->
# 🌏 zed-loc (Zed 汉化)

 [![Crowdin][crowdin-image]][crowdin-url]
 [![GitHub issues][issues-image]][issues-url]
 [![Github Pulls][pulls-image]][pulls-url]
 [![GitHub stars][stars-image]][stars-url]
 [![GitHub forks][forks-image]][forks-url]
 [![Github Downloads][download-image]][download-url]
 [![license][license-image]][license-url]
 ![repo-size][repo-size-image]

简体中文|[English](README.en.md)|[日本語](README.ja.md)

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
<a href="https://github.com/oper0" title="oper0">
  <img src="https://avatars.githubusercontent.com/u/204131036?v=4" width="42;" alt="oper0"/>
</a>

# 许可证

本项目基于 [MIT 许可证](LICENSE)发布，允许任何组织和个人免费使用。

[crowdin-url]: https://zh.crowdin.com/project/zed-editor
[crowdin-image]: https://badges.crowdin.net/zed-editor/localized.svg

[issues-url]: https://github.com/TC999/zed-loc/issues "议题"
[issues-image]: https://img.shields.io/github/issues/TC999/zed-loc?style=flat-square&logo=github&label=议题

[pulls-url]: https://github.com/TC999/zed-loc/pulls "拉取请求"
[pulls-image]: https://img.shields.io/github/issues-pr-raw/TC999/zed-loc?style=flat&logo=github&%3Fcolor%3Dgreen&label=%E6%8B%89%E5%8F%96%E8%AF%B7%E6%B1%82

[stars-url]: https://github.com/TC999/zed-loc/stargazers "星标"
[stars-image]: https://img.shields.io/github/stars/TC999/zed-loc?style=flat-square&logo=github&label=星标

[forks-url]: https://github.com/TC999/zed-loc/fork "复刻"
[forks-image]: https://img.shields.io/github/forks/TC999/zed-loc?style=flat-square&logo=github&label=复刻

[discussions-url]: https://github.com/TC999/zed-loc/discussions "讨论"

[hits-url]: https://hits.dwyl.com/ "访问量"
[hits-image]: https://custom-icon-badges.demolab.com/endpoint?url=https%3A%2F%2Fhits.dwyl.com%2FTC999%2Fzed-loc.json%3Fcolor%3Dgreen&label=%E8%AE%BF%E9%97%AE%E9%87%8F&logo=graph

[repo-url]: https://github.com/TC999/zed-loc "仓库地址"

[repo-size-image]:https://img.shields.io/github/repo-size/TC999/zed-loc?style=flat-square&label=%E4%BB%93%E5%BA%93%E5%A4%A7%E5%B0%8F


[download-url]: https://github.com/TC999/zed-loc/releases/latest "下载"
[download-image]: https://img.shields.io/github/downloads/TC999/zed-loc/total?style=flat-square&logo=github&label=%E6%80%BB%E4%B8%8B%E8%BD%BD%E6%95%B0 "总下载数"

[license-url]: https://github.com/TC999/zed-loc/blob/master/LICENSE "许可证"
[license-image]: https://custom-icon-badges.demolab.com/github/license/TC999/zed-loc?style=flat&logo=law&label=%E8%AE%B8%E5%8F%AF%E8%AF%81
