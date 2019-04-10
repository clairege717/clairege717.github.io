# Angular介绍、环境搭建及Angular CLI 3的使用

## 一、Angular介绍

## 二、学习Angular必备基础

HTML、CSS、JS、ES6

## 三、Angular环境搭建

1. 安装nodeJS
2. [可选] 安装cnpm
3. 安装angular/cli

### 四、Angular创建项目
1. 打开要创建项目的目录
2. 创建

    ng new projectName

    如果要跳过npm i安装

    ng new projectName --skip-install
3. 运行

    cd projectName

    ng serve --open

### 五、Angular目录结构分析

- node_modules

    提供给整个工作区的 npm 包。
    
- .editorconfig

    代码编辑器配置
    
- .gitignore

    指定Git要忽略的非跟踪文件
    
- angular.json

    工作区中所有项目的默认 CLI 配置，包括 CLI 使用的构建选项、运行选项、测试工具选项（比如 TSLint、Karma、Protractor）等。
    
- package.json

    配置用于工作区中所有项目的包依赖项。
    
- package-lock.json

    为 npm 客户端安装到 node_modules 中的所有软件包提供版本信息。
    
- README.md
- tsconfig.json

    工作区中所有应用的默认 TypeScript 配置。包括 TypeScript 选项和 Angular 模板编译器选项。
    
- tslint.json

    工作区中所有应用的默认 TSLint 配置。

- e2e

  子目录包含一组初始应用所对应的端到端测试的配置文件和源文件。

  - src
    - app.e2e-spec.ts
    - app.po.ts
  - protractor.conf.js
  - tsconfig.e2e.json
  
- src

    子目录包含该初始应用的源文件（应用逻辑、数据和资源）以及配置文件。
    
  - app

    包含组件文件，其中定义了应用逻辑和数据。

    - app-routing.module.ts
    - app.component.css
    - app.component.html
    - app.component.spec.ts
    - app.component.ts
    - app.module.ts

  - assets

    包含图像文件和其它文件，当构建应用时会被原样复制到构建目标中。
    
  - environments

    包含针对特定目标环境的配置选项。默认情况下有一个未命名的标准开发环境和一个名叫 "prod" 的产品环境。你可以定义一些额外的目标环境配置。
    
  - browserslist

    配置各个目标浏览器和 Node.js 版本之间的市场占有率，供各种前端工具使用。

  - favicon.ico

    一个用在书签栏上的应用图标。

  - index.html

    当有人访问你的应用时给出的主 HTML 文件，你通常不用手动在这里添加任何 \<script> 或\<link> 标签。

  - karma.conf.js
  - main.ts

    应用的主入口点。使用 JIT 编译器编译应用，并引导应用的根模块 AppModule 来运行在浏览器中。你也可以为 CLI 的 build 和 serve 命令添加 --aot 标志，来使用 AOT 编译器 而不必修改任何代码。

  - polyfills.ts

    为浏览器支持提供腻子脚本（polyfill）。

  - styles.css

    列出为项目提供样式的 CSS 文件。其扩展名和你为项目配置的样式预处理器保持一致。

  - test.ts

    单元测试的主入口点，其中带有一些特定于 Angular 的配置。

  - tsconfig.app.json

    继承自工作区级的 tsconfig.json 文件。

  - tsconfig.spec.json

    继承自工作区级的 tsconfig.json 文件。
    
  - tslint.json

    继承自工作区级的 tsconfig.json 文件。

