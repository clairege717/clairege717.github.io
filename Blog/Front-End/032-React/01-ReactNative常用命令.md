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

- 


### 常见错误

- error Failed to build iOS project. We ran "xcodebuild" command but it exited with error code 65. To debug build logs further, consider building your app with Xcode.app, by opening rn.xcodeproj

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

- 
