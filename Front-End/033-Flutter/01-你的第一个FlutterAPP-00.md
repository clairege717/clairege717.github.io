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
  - 这个示例的body由一个包含了**Text**子组件的**Center**组件组成。Center组件可以使其组件子树在屏幕中居中显示。

- 选择你的IDE提供的方式运行应用程序

## 第二步：使用packages



