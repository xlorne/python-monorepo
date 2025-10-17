# Python Monorepo with PDM

一个基于 PDM (Python Dependency Manager) 构建的 Python monorepo 项目框架示例。

## 项目结构

```
python-monorepo/
├── app/                    # 应用程序包
│   ├── main.py             # 应用程序入口
│   └── pyproject.toml      # 应用程序配置
├── lib/                    # 共享库包
│   ├── math.py             # 数学工具库
│   └── pyproject.toml      # 库配置
├── pyproject.toml          # 根项目配置
├── pdm.lock                # 依赖锁定文件
└── README.md               # 项目说明
```

## 什么是 PDM Monorepo？

PDM 支持 workspace 功能，允许在单个仓库中管理多个 Python 包。这种 monorepo 结构特别适合：

- 多个相关的 Python 包需要一起开发和维护
- 需要在包之间共享代码和依赖
- 统一管理版本和发布流程
- 简化 CI/CD 和测试流程

## 环境要求

- Python >= 3.12
- PDM >= 2.0

## 安装 PDM

```bash
# 使用 pip 安装
pip install pdm

# 或使用 pipx 安装（推荐）
pipx install pdm

# 或使用 homebrew 安装（macOS）
brew install pdm
```

## 快速开始

### 1. 克隆项目

```bash
git clone git@github.com:xlorne/python-monorepo.git
cd python-monorepo
```

### 2. 安装依赖

```bash
# 安装所有包的依赖
pdm install

```

### 3. 运行应用程序

```bash
# 使用预定义脚本运行
pdm run run-app

# 或者直接运行
pdm run python -m app.main
```

### 4. 开发模式

```bash

# 运行测试
pdm run pytest

# 代码格式化
pdm run black .
pdm run isort .
```

## 项目配置说明

### 根项目配置 (`pyproject.toml`)

```toml
[project]
name = "python-monorepo"
version = "0.1.0"
description = "Default template for PDM package"
dependencies = ["requests>=2.32.5"]
requires-python = ">=3.12"

[tool.pdm.workspace]
members = ["lib", "app"]  # 定义工作空间成员

[tool.pdm.scripts]
run-app = "python -m app.main"  # 定义便捷脚本
```

### 应用包配置 (`app/pyproject.toml`)

```toml
[project]
name = "app"
dependencies = ["lib"]  # 依赖内部包

[tool.pdm]
editable-dependencies = ["lib"]  # 以可编辑模式安装依赖
```

### 库包配置 (`lib/pyproject.toml`)

```toml
[project]
name = "lib"
description = "A simple math library"
# 库包通常不依赖其他内部包
```

## 常用命令

### 依赖管理

```bash
# 添加新依赖到根项目
pdm add requests


# 移除依赖
pdm remove requests

# 更新依赖
pdm update
```

### 包管理

```bash
# 构建所有包
pdm build


# 检查包信息
pdm info
```

### 脚本运行

```bash
# 运行自定义脚本
pdm run <script-name>

# 运行 Python 模块
pdm run python -m app.main

# 进入 PDM shell
pdm shell
```

## 开发最佳实践

### 1. 版本管理

- 使用语义化版本控制
- 保持所有包的版本同步
- 使用 `pdm version` 命令统一管理版本

### 2. 依赖管理

- 根项目管理公共依赖
- 各子包管理特定依赖
- 使用版本范围而非固定版本

### 3. 代码组织

- 共享代码放在 `lib/` 包中
- 应用程序放在 `app/` 包中
- 使用相对导入引用内部包

### 4. 测试

```bash
# 运行所有测试
pdm run pytest

```

## 扩展项目

### 添加新包

1. 创建新的包目录：
```bash
mkdir new-package
cd new-package
```

2. 初始化包配置：
```bash
pdm init
```

3. 在根项目的 `pyproject.toml` 中添加新包：
```toml
[tool.pdm.workspace]
members = ["lib", "app", "new-package"]
```

### 添加开发工具

```bash
# 添加开发依赖
pdm add -dG dev pytest black isort mypy

# 配置开发工具
pdm run black .
pdm run isort .
pdm run mypy .
```

## 故障排除


### 调试命令

```bash
# 检查环境信息
pdm info --env

# 检查依赖树
pdm list --tree

```

## 更多资源

- [PDM 官方文档](https://pdm.fming.dev/)
- [Python 打包用户指南](https://packaging.python.org/)
- [Monorepo 最佳实践](https://monorepo.tools/)
