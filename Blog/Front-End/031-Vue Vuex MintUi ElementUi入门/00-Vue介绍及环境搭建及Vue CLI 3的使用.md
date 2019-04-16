# Vue介绍、环境搭建及Vue CLI 3的使用

## 一、介绍
Vue和Angular、React都是前端框架
- 单页面应用
- 基于模块化、组件化的开发工具

Vue灵活、简单，很多中小型企业里面用的非常多。

## 二、环境搭建
- 必须安装Node.js
- 搭建Vue开发环境，安装Vue脚手架工具，官方命令工具
  - npm install --global vue-cli
- 创建项目
  - vue init webpack vue-demo00
  - cd vue-demo0
  - npm install  （如果创建项目的时候没有报错，这步可以省略）
  - npm run dev
- 另一种创建
  - vue init webpack-simple vue-demo01 （中小项目创建，目录结构简单）
  - cd vue-demo0
  - npm install
  - npm run dev

## 三、Vue CLI 3.x的使用
1. 关于Vue CLI3和Vue CLI2以及Vue 2.x和Vue 3.x

    Vue CLI是安装Vue的脚手架工具，也是官方命令行工具，可以用命令快速创建项目。
    注意：Vue CLI3是Vue CLI2的升级版本，并不是Vue3.0。Vue CLI3与老版本的Vue CLI创建项目的方式不一样，创建项目的用法是一样的。Vue CLI3在编译速度上做了优化。

2. 关于Vue CLI老版本安装及创建项目（目前Vue CLI3仍未发布，老版本仍可使用）
   - 搭建Vue的开发环境，安装Vue脚手架工具，官方命令行工具
     - npm install --global vue-cli
   - 创建项目
     - vue init webpack vue-demo00
     - cd vue-demo0
     - npm install  （如果创建项目的时候没有报错，这步可以省略）
     - npm run dev
   - 另一种创建
     - vue init webpack-simple vue-demo01 （中小项目创建，目录结构简单）
     - cd vue-demo0
     - npm install
     - npm run dev
   -  
3. Vue CLI新版本安装及创建
    - 关于旧版本：如果已经全局安装了旧版本的 vue-cli (1.x 或 2.x)，需要先卸载。
      - npm uninstall vue-cli -g 
      - yarn global remove vue-cli
    - Node.js版本：需要 Node.js 8.9 或更高版本 (推荐 8.11.0+)。你可以使用 nvm 或 nvm-windows 在同一台电脑中管理多个 Node 版本。
    - 安装新版本
      - npm install -g @vue/cli
      - yarn global add @vue/cli
    - 检查版本
      - vue --version
    - 创建项目
      1. 命令行创建
        vue create hello-world
      2. 图形化创建
        vue ui
    - 运行
      - npm run serve
    - 编译
      - npm run build

4. Vue CLI 3.x和2.x之间桥接工具

  ```
  npm install -g @vue/cli-init
  # `vue init` 的运行效果将会跟 `vue-cli@2.x` 相同
  vue init webpack my-project
  ```

