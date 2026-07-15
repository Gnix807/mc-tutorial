# Minecraft 从入门到精通

一份面向新手的 Minecraft Java 版图文教程，从零开始带你逐步掌握这款游戏的方方面面。

## 关于本教程

这份教程的灵感来自 [《你缺失的那门计算机课》](https://www.criwits.top/missing/)。我们希望用同样亲切、专业、平易近人的方式，为 Minecraft 新手提供一份高质量的入门指南。

- **零门槛**：从购买安装开始，假设你从未玩过 Minecraft
- **有深度**：不仅教「怎么做」，还讲「为什么」
- **重实战**：每一步都有截图和操作指引
- **持续更新**：跟进最新正式版（当前 26.2）

## 内容概览

| 章节 | 内容 |
|---|---|
| 第一章 · 基础入门 | 购买安装、启动器选择、游戏设置 |
| 第二章 · 生存指南 | 第一天→采集合成→采矿→农牧→村民交易→战斗→附魔药水→下界末地 |
| 第三章 · 建造美学 | 建筑基础、风格设计、地形改造、家具、屋顶、配色 |
| 第四章 · 红石工程 | 红石基础、逻辑电路、自动化农场、活塞机械、存储分类 |
| 第五章 · 服务器与联机 | 联机方式、服务器搭建、领域服、PvP 入门 |
| 第六章 · 模组与资源包 | 模组加载器、光影材质、优化模组、整合包入门 |
| 第七章 · 命令与指令方块 | 基础命令、指令方块、数据包、命令速查 |

## 技术栈

- [Hugo](https://gohugo.io/) v0.164+ 静态站点生成器
- [Book](https://github.com/alex-shpak/hugo-book) 主题
- Markdown 编写，Hugo 短代码扩展

## 本地运行

```bash
# 克隆仓库
git clone https://github.com/你的用户名/仓库名.git
cd 仓库名

# 初始化主题子模块
git submodule update --init

# 启动开发服务器
hugo server --bind 0.0.0.0 --port 1313
```

浏览器打开 `http://localhost:1313/` 即可预览。

## 贡献指南

欢迎任何形式的贡献！无论是撰写新章节、修正错误、优化排版，还是提供截图和插图。

详细的贡献流程请参阅 [CONTRIBUTING.md](./CONTRIBUTING.md)。

**当前急需**：

- 第二章 2.2~2.8 的内容撰写
- 第三章至第七章的内容填充
- 各章节的游戏内截图
- 错误指正与数据核实

## 许可

本教程所有原创内容以 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 协议授权。你可以自由分享、复制本教程内容及基于此进行二次创作，但须注明原作者与出处，且不得用于商业用途。

本教程中出现的 Minecraft 相关商标与游戏素材归 Mojang Studios / Microsoft 所有。引用仅用于教学与介绍目的。

## 致谢

- [《你缺失的那门计算机课》](https://www.criwits.top/missing/) —— 写作风格参考
- [Minecraft Wiki](https://zh.minecraft.wiki/) —— 游戏资料参考
- [MC百科](https://www.mcmod.cn/) —— 模组信息参考
- [HMCL](https://hmcl.huangyuhui.net/) / [PCL2](https://github.com/Hex-Dragon/PCL2) / [BakaXL](https://www.bakaxl.com) 启动器文档
