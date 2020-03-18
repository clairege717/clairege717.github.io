# React Native热更新-本地code push server部署相关

参考：[*https://blog.csdn.net/u011975949/article/details/83989733*](https://blog.csdn.net/u011975949/article/details/83989733)

### 服务端

- 安装mysql并启动
- 下载code-push-server
  - 下载code-push-server代码，并下载资源
    ```
    // clone代码
    git clone https://github.com/lisong/code-push-server.git

    // 进入项目并安装资源
    cd code-push-server && npm instal
    ```
  - 修改config/config.js，添加数据库信息
    ```
    db: {
        username: process.env.RDS_USERNAME || "root",  //数据库账户
        password: process.env.RDS_PASSWORD || "root123456",  //数据库账户密码，需要自己设置
        database: process.env.DATA_BASE || "codepush",  //新建的数据库表名
        host: process.env.RDS_HOST || "127.0.0.1",
        port: process.env.RDS_PORT || 3306,
        dialect: "mysql",
        logging: false
    },
    ```
  - 在code-push-server目录下，执行以下命令，创建数据库表
    ```
    // 初始化mysql数据库
    ./bin/db init --dbhost localhost --dbuser root --dbpassword 数据库密码

    或者
    ./bin/db init --dbhost 127.0.0.1 --dbuser root --dbpassword  数据库密码
    ```

    若出现以下错误：
    ```
    Error: Client does not support authentication protocol requested by server; consider upgrading MySQL client
    ```

    解决方案如下：

    1. 配置mysql环境变量

        ```
        alias mysql=/usr/local/mysql/bin/mysql
        alias mysqladmin=/usr/local/mysql/bin/mysqladmin
        ```

    2. 登录mysql，执行以下命令
        ```
        //登录MySQL	
        mysql -u root -p
        #接着输入你的数据库密码

        //一次执行下面三条语句
        ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '数据库密码';
        ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '数据库密码';
        SELECT plugin FROM mysql.user WHERE User = 'root';
        ```
 - 修改config/config.js，配置打包后的bundle存储地址，这边配置local。如果存储类型**storageType**为local，只需要修改db、local、common的配置就行。需要创建storage和data文件夹，用来保存打包好的资源，供用户更新下载。

    ```
    config.development = {
        // Config for database, only support mysql.
        db: {
            username: process.env.RDS_USERNAME || "root",  //数据库账户
            password: process.env.RDS_PASSWORD || "root123456",  //数据库账户密码，需要自己设置
            database: process.env.DATA_BASE || "codepush",  //新建的数据库表名
            host: process.env.RDS_HOST || "127.0.0.1",
            port: process.env.RDS_PORT || 3306,
            dialect: "mysql",
            logging: false,
            operatorsAliases: false,
        },
        // Config for local storage when storageType value is "local".
        // 如果存储类型"storageType"为"local"则更新包放在本地，需要配置相关信息
        local: {
            // Binary files storage dir, Do not use tmpdir and it's public download dir.
            //需要自己创建一个文件路径，把你的路径填上去或者按给定的路径创建文件夹
            storageDir: process.env.STORAGE_DIR || "/Users/hhb/Desktop/workspaces/storage",
            // Binary files download host address which Code Push Server listen to. the files storage in storageDir.
            //下载地址，自己设备对应的ip，如果是模拟器的话，无须更改
            downloadUrl: process.env.LOCAL_DOWNLOAD_URL || "http://192.168.100.46:3000/download",
            // public static download spacename.
            public: '/download'
        },
        common: {
            /*
            * tryLoginTimes is control login error times to avoid force attack.
            * if value is 0, no limit for login auth, it may not safe for account. when it's a number, it means you can
            * try that times today. but it need config redis server.
            */
            tryLoginTimes: 0,
            // CodePush Web(https://github.com/lisong/code-push-web) login address.
            //codePushWebUrl: "http://127.0.0.1:3001/login",
            // create patch updates's number. default value is 3
            diffNums: 3,
            // data dir for caclulate diff files. it's optimization.
            //需要自己创建一个文件路径，把你的路径填上去或者按给定的路径创建文件夹
            dataDir: process.env.DATA_DIR || "/Users/hhb/Desktop/workspaces/data",
            // storageType which is your binary package files store. options value is ("local" | "qiniu" | "s3"| "oss" || "tencentcloud")
            //选择存储类型，目前支持"local"， "qiniu"，"s3"，"oss"，"tencentcloud"
            storageType: process.env.STORAGE_TYPE || "local",
            // options value is (true | false), when it's true, it will cache updateCheck results in redis.
            updateCheckCache: false,
            // options value is (true | false), when it's true, it will cache rollout results in redis
            rolloutClientUniqueIdCache: false,
        },
    }
    ```
 - 在code-push-server目录下，执行以下命令，启动服务

    ```
    ./bin/www
    ```


### 客户端

- 安装code-push-cli
  
    ```
    npm install -g code-push-cli
    ```
- 登录code-push-server，使code push和自建的服务器关联
  - 检查当前是否登录。新服务，要先保证没有别的帐号正在登录。

    ```
    //查看是否登录
    code-push whoami
    ```

    若已登录，要注销当前帐号

    ```
    //注销当前账号
    code-push logout
    ```
  - 执行登录指令。浏览器会自动打开本地服务登录页，默认帐号密码是：admin，123456；登录后获取token并复制到命令行中，回车确认。

    ```
    //登录指令
    code-push login http://localhost:3000
    ```
    
- 添加应用，获取Deployment Key

  ```
  //添加应用
  //code-push app add <appName> <os> <platform>
  //示例
  code-push app add react_native_demo ios react-native
  ```

┌────────────┬───────────────────────────────────────┐
│ Name       │ Deployment Key                        │
├────────────┼───────────────────────────────────────┤
│ Production │ PFXevrcFnsyvrRFbSNDRbw28KkMW4ksvOXqog │
├────────────┼───────────────────────────────────────┤
│ Staging    │ xvy0BEzZJMoIiIsN3POZ3NUoYRfw4ksvOXqog │
└────────────┴───────────────────────────────────────┘

┌────────────┬───────────────────────────────────────┐
│ Name       │ Deployment Key                        │
├────────────┼───────────────────────────────────────┤
│ Production │ o6pBwOINIDsPeswKtFb3JjduRPTg4ksvOXqog │
├────────────┼───────────────────────────────────────┤
│ Staging    │ 7x3yIgHKdUalWGkfGCkHCkv4GdDE4ksvOXqog │
└────────────┴───────────────────────────────────────┘

### React Native

- 安装react-native-code-push
- Android配置
- iOS配置