# clairege717

葛燕丹的个人博客（知识点记录、练习），基于 Jekyll 4 搭建。

## 项目包含内容

- 文章与笔记
  - `Daily/`：日常记录、工作/生活小记
  - `Front-End/`：前端技术栈学习笔记
  - `7788/`：杂七杂八的信息记录
  - `_posts/`：按时间发布的文章（Jekyll 默认文章目录）
- 页面与布局
  - `_layouts/`：页面布局（home/page/about/archives 等）
  - `_includes/`：可复用片段（head/nav/footer 等）
  - `about.md`、`archive.md`、`404.html`：站点页面
- 静态资源
  - `assets/`：Bootstrap/jQuery/Ionicons 及自定义 CSS/JS、图片等
- 构建与依赖
  - `Gemfile` / `Gemfile.lock`：Ruby 依赖（已包含 `webrick` 以兼容 Ruby 3）
  - `_config.yml`：Jekyll 配置（站点信息、分页、插件等）
  - `blogpull.sh`：拉取更新并重启本地服务的脚本（如有使用场景）

## 本地运行

### 环境要求

- Ruby（建议 3.x）
- Bundler（如未安装：`gem install bundler`）

### 安装依赖

```bash
bundle install
```

### 启动开发服务

```bash
bundle exec jekyll serve --livereload
```

默认访问：<http://127.0.0.1:4000>

> 如果提示缺少 `webrick`，请重新执行 `bundle install`，并确认 `Gemfile` 中已包含 `webrick` 依赖。

### 构建静态文件

```bash
bundle exec jekyll build
```

输出目录：`_site/`

## TODO

- [ ] 整理目录命名与分类（如 `Front-End`、`Daily` 的归档规则）
- [ ] 增加站内搜索/标签页
- [ ] 增加评论系统（例如 Giscus/Disqus）
- [ ] 优化页面性能与资源体积（图片压缩、按需加载）
- [x] 部署到 Netlify / GitHub Pages，并补充部署文档

## 部署 (Deployment)

本项目使用 GitHub Actions 自动构建并部署到 GitHub Pages。

- **触发条件**：推送到 `master` 分支。
- **构建流程**：
  1. 拉取代码
  2. 安装 Ruby 依赖
  3. 执行 `jekyll build` 生成静态文件
  4. 将 `_site` 目录部署到 `gh-pages` 分支

**注意**：请在 GitHub 仓库设置中（Settings -> Pages），将 **Source** 设置为 `Deploy from a branch`，并选择 `gh-pages` 分支。
