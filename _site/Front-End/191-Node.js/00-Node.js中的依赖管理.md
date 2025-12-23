# Node.js中的依赖管理

整理自：知乎 [Node.js中的依赖管理](https://zhuanlan.zhihu.com/p/56002037)

nodejs中的5种依赖：
- dependencies（常用）
- devDependencies（常用）
- peerDependencies（我没用过）
- bundledDependencies（我没用过）
- optionalDependencies（我没用过）

以下，是这5中依赖的信息整理

- ## dependencies

    项目正常运行时所需的依赖。

    命令：npm i xxx -S || npm i xxx --save

    注：npm 5.x 开始可以省略 --save，即可以执行 npm install xxx，一样把包的依赖添加到package.json。

- ## devDependencies

    开发中需要的依赖项，线上不需要的。

    命令：npm i xxx -D || npm i xx --save-dev

    注：npm i --production 忽略开发依赖，只安装依赖

    常用的开发依赖可归纳为：
    - 构建工具：webpack、rollup、grunt、gulp等

        这些构建工具，会生成生产环境的代码，之后线上就直接使用这些压缩过的代码。

    - 预处理器

        对源代码进行一定的处理，生成最终代码的工具。

        比较典型的有CSS 中的less、stylus、sass、scss等；JS 中的coffee-script、bable等。

    - 测试工具

        测试和开发同属于“线上状态不需要的依赖“这一特性，因此测试工具可以归入开发依赖。

        常用的如：chai、e2e、karma、coveralls等。
        
    - 开发工程中的7788

        就是真的“只有开发过程才需要”的依赖。上线时要么已经打包成最终代码，要么是不需要使用了。
        
        如：webpack-dev-server支持开发热加载，线上是不用的；babel-register因为性能原因，也不能用于线上。

- ## peerDependencies

    peerDependencies、bundleDependencies、optionalDependencies这三种，是作为包的发布者会用到的。因此之后的描述，以发布者的身份进行。




- ## bundleDependencies


- ## optionalDependencies



