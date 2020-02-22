# 你的第一个Flutter APP（第一部分）

这是一个创建你的第一个Flutter app的操作指南。如果你已经熟悉了面向对象编码和基本编程概念类似于变量、循环、条件等，你可以完成这个教程。你无需具备Dart、mobile或者web编程经验。

这个操作指南是codelab的第一部分。你能在[Google Developers Codelabs](https://codelabs.developers.google.com/)中找到第二部分，当然也有第一部分的。

主要步骤
- 

## 在第一部分中要完成的内容

你将完成一个简单的移动应用，这个应该可以帮助初创公司生成建议名称。用户可以通过选择、取消选择来保存最佳的公司名称。代码自动生成公司名称。当用户上滑页面时，生成更多的公司名称。不限制用户可以滑多久。

> 
> ### 你会学到什么
> - 如何写出一个iOS、Android、Web三平台共通的Flutter应用
> - Flutter应用的基础结构
> - 查找并使用扩展功能所需的packages
> - 使用热加载进行快速开发周期
> - 如何创建有状态的widget
> - 如何创建无限的、惰性加载的列表
> 在这个codelab的第二部分中，你将为应用程序添加交互，修改主题，并且可以添加一个跳转到新页面的功能（在Flutter中称之为route）。
> 

>   
> ### 你需要用到什么
> 你需要两种软件来完成这次的实验：Flutter SDK，一个编辑器。codelab推荐使用Android Studio，当然你也可以使用你更喜欢的编辑器。
> 你可以使用以下任意设备运行这次代码实验：
> - 一个连接到你电脑并且设置成开发者模式的物理设备（Android或iOS）
> - iOS模拟器
> - Android仿真器
> - 浏览器（只有Chrome才能进行调试）
> 

## 第一步：创建Flutter app

使用入门教程，创建一个简单的模板化Flutter应用，命名为“startup_namer”。

在这个codelab中，你将主要编辑Dart代码所在的**lib/main.dart**文件。

- 替换**lib/main.dart**中的内容
  
  删除**lib/main.dart**中的所有代码，并用以下代码替代。

  ```
    // Copyright 2018 The Flutter team. All rights reserved.
    // Use of this source code is governed by a BSD-style license that can be
    // found in the LICENSE file.

    import 'package:flutter/material.dart';

    void main() => runApp(MyApp());

    class MyApp extends StatelessWidget {
        @override
        Widget build(BuildContext context) {
            return MaterialApp(
            title: 'Welcome to Flutter',
            home: Scaffold(
                appBar: AppBar(
                    title: Text('Welcome to Flutter'),
                ),
                body: Center(
                    child: Text('Hello World'),
                ),
            ),
            );
        }
    }
  ```

  以上代码，将在显示器中央显示“Hello World”。

  分析：
  - 这个示例创建了一个Material app。[Material](https://material.io/guidelines)是移动端和Web端的标准视觉设计语言。Flutter提供了丰富的Material组件。
  - **main()**方法使用了箭头(=>)符号。使用箭头方法表示单行函数或方法。
  - 这个app是一个扩展了**StatelessWideget**的组件。在Flutter中，一切皆组件，包括对齐、填充和布局。
  - Material库中的**Scaffold**组件，包含主屏幕的组件树，提供了应用程序默认的bar、title和body属性。这个组件的子树可能非常复杂。
  - 组件的主要任务是提供**build()**方法，这个方法描述了如何以其他较低级别的组件显示这个组件。
  - 这个示例的body由一个包含了**Text**子组件的**Center**组件组成。Center组件可以使其组件子树在屏幕中垂直居中显示。

- 选择你的IDE提供的方式运行应用程序

## 第二步：使用packages

这一步中，你将开始使用一个开源库：[english_words](https://pub.dev/packages/english_words)。这个库包含了几千个最常用的英语单词以及一些实用功能。

在[pub.dev](https://pub.dev/)中，可以找到**english_words**以及其他很多开源库。

- **pubspec.yaml**文件管理Flutter app的资源和依赖。在**pubspec.yaml**的dependencies列表下添加**english_words**(3.1.5或更高版本)：
  ```
  dependencies:            
    flutter:            
      sdk: flutter            
    cupertino_icons: ^0.1.2            
    english_words: ^3.1.5
  ```
- 当使用Android Studio的编辑器打开**pubspec.yaml**时，点击 **Packages get**，可以将库导入到项目中。在控制台中可以看到如下内容：
  ```
  flutter pub get
  Running "flutter pub get" in startup_namer...
  Process finished with exit code 0

  ```
  > Tips:
  > VSCode保存更改后会自动执行**Packages get**
  
  **Packages get**操作会自动生成**pubspec.lock**文件，文件内容是项目中所有已引入的包以及其对应的版本号。

- 在**lib/main.dart**引入新包
  ```
  import 'package:flutter/material.dart';
  import 'package:english_words/english_words.dart';
  ```

  在Android Studio中，会有import提示，引入后，因为未使用引入的包，这段文字显示为灰色。
- 使用english_words包生成的文本替换“Hello World”字符串。
  ```
  class MyApp extends StatelessWidget {
    @override
    Widget build(BuildContext context) {
      final wordPair = WordPair.random();
      return MaterialApp(
        title: 'Welcome to Flutter',
        home: Scaffold(
          appBar: AppBar(
            title: Text('Welcome to Flutter'),
          ),
          body: Center(
            child: Text(wordPair.asPascalCase),
          ),
        ),
      );
    }
  }
  ```

  > 备注：
  > "PascalCase"(upper camel case)意味着字符串中的每一个单词，都以大写字母开头。所以“uppercamelcase”变成“UpperCamelCase”。
- 若app是运行中，每次保存代码都能在显示器中看到不同的单词对。

## 第三部：添加一个有状态的组件（stateful widget）

无状态组件（stateless wideget）的属性不能被修改，所有值都是明确的，不变的。

有状态组件维持组件生命周期中可能变化的状态。声明有状态组件需要至少两个类：
  1. **StatefulWidget**类，创建一个实例。
  2. **State**类

StatefulWidget类本身是不可变的，但是State类在组件的生命周期中一直存在。

这步，将完成添加一个stateful widget：RandomWords，这个组件会创建它的State类：RandomWordsState。在**MyApp**这个无状态组件中添加子组件**RandomWords**。

  1. 创建一个最小状态类。将以下代码添加到**main.dart**文件最后：
   ```
    class RandomWordsState extends State<RandomWords> {
      // TODO Add build() method
    }
   ```

   **State<RandomWords>**：表示RandomWords的通用State类。

   这部分维持RandomWords组件的状态，大部分的应用的逻辑和状态都位于此处。RandomWordsState类存储随着用户滑动而无限增加生成的词对。

  2. 添加**RandomWords**有状态组件到**main.dart**文件。**RandomWords**组件只创建它的State类实例。
   ```
    class RandomWords extends StatefulWidget {
      @override
      RandomWordsState createState() => RandomWordsState();
    }
   ```

  3. 在**RandomWordsState**中添加**build()**方法
   ```
    class RandomWordsState extends State<RandomWords> {
      @override
      Widget build(BuildContext context) {
        final wordPair = WordPair.random();
        return Text(wordPair.asPascalCase);
      }
    }
   ```
  4. 按以下示例修改**MyApp**
   ```
    class MyApp extends StatelessWidget {            
      @override            
      Widget build(BuildContext context) {
        return MaterialApp(            
          title: 'Welcome to Flutter',            
          home: Scaffold(
              title: Text('Welcome to Flutter'),            
            ),            
            body: Center(
              child: RandomWords(),            
            ),            
          ),            
        );            
      }
   ```
  5. 重启项目。

## 第四步：创建一个可无限滚动的ListView


