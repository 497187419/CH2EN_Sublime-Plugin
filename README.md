# CH2EN Sublime Plugin

一个用于 Sublime Text 的中文转英文翻译插件，基于百度翻译 API，适用于快速翻译变量名、函数名等场景。

## 功能特点

- 支持划词翻译
- 中文快速转换为英文
- 适用于变量命名、函数命名等场景
- 使用百度翻译 API，翻译质量有保证

## 安装步骤

1. 找到 Sublime Text 的 Packages 目录
   - Windows: `%APPDATA%\Sublime Text 3\Packages`
   - macOS: `~/Library/Application Support/Sublime Text 3/Packages`
   - Linux: `~/.config/sublime-text-3/Packages`

2. 在 Packages 目录下创建 `CH2EN` 文件夹

3. 将以下文件复制到 `CH2EN` 目录：
   - ch2en.py
   - Default.sublime-keymap (Windows/Linux)
   - Default (OSX).sublime-keymap (macOS)

## 使用方法

1. 在代码中选中需要翻译的中文文本
2. 按下快捷键 `Ctrl+T`（Windows/Linux）或 `Cmd+T`（macOS）
3. 选中的中文将被翻译成对应的英文

## 注意事项

- 确保已连接网络
- 选中的文本长度需要大于1个字符
- 翻译服务基于百度翻译 API

## 许可证

MIT License
