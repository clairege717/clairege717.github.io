# React Native常用内容

- react-native init AwesomeProject

    创建名为"AwesomeProject"的新项目

- react-native run-ios

    运行iOS虚拟机

- Props(属性)
- State(状态)

- React Navigation


- react-native-vector-icons -npm

    react-native link react-native-vector-icons

    添加新的依赖

- node_modules

    cd到项目的根目录，执行下列命令

    npm install --force

    npm cache clean && npm install

    npm start

- 安卓打包

    cd到项目的安卓文件夹下，执行下列命令

    ./gradlew clean

    ./gradlew assembleRelease

- 安装 release 版的应用

    cd到项目的安卓文件夹下，执行下列命令

    react-native run-android --variant=release

### 常见错误

- error Failed to build iOS project. We ran "xcodebuild" command but it exited with error code 65. To debug build logs further, consider building your app with Xcode.app, by opening rn.xcodeproj

  - The following build commands failed:
    CompileC /Users/claire/Documents/workspace/car-app/ios/build/rn/Build/Intermediates.noindex/React.build/Debug-iphonesimulator/React.build/Objects-normal/x86_64/RCTMultipartStreamReader.o Base/RCTMultipartStreamReader.m normal x86_64 objective-c com.apple.compilers.llvm.clang.1_0.compiler
    
    备注：
    命令行编译版本报错：CompileC /Users/claire/Documents/workspace/car-app/ios/build/rn/Build/Intermediates.noindex/React.build/Debug-iphonesimulator/React.build/Objects-normal/x86_64/RCTMultipartStreamReader.o Base/RCTMultipartStreamReader.m normal x86_64 objective-c com.apple.compilers.llvm.clang.1_0.compiler

    在模拟器和真机上运行没有问题，用archive菜单打包App Store版本上传也没有问题。但是用命令行运行就报这个错误。

    待解决！
    
    ~~~经过版本回退来逐步排除代码，最终发现因为变量赋值的时候，类型错误，而编译器没有检查出来。~~~

    ~~~代码如下：~~~

    ~~~BOOL permitUserControl = @1;//这个错误，编译器没有检查出来。~~~

    ~~~正确的代码：~~~

    ~~~BOOL permitUserControl = YES;~~~
    
    解决方法

    - 删除项目依赖包以及 yarn 缓存
        
        rm -rf node_modules && yarn cache clean

    - 重新装包
        
        yarn install

    - 清除 React-Native 缓存
        
        rm -rf ~/.rncache

    - 下载 React-Native IOS 运行依赖
        
        直接运行下载脚本，若直接下载完成，后面的步骤就不用看了，直接运行项目 react-native run-ios 即可

        node_modules/react-native/scripts/ios-install-third-party.sh

