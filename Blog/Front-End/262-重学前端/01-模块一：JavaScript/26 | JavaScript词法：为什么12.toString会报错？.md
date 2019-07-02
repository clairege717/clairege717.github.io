# [26 | JavaScript词法：为什么12.toString会报错？](https://time.geekbang.org/column/article/86400?utm_source=time_web&utm_medium=menu)

接下来几节，了解JavaScript的文法部分。

一般来说，文法分成词法和语法两种。

词法规定了语言的最小语义单元：token，可以翻译成“标记”或者“词”。本专栏文章中，统一翻译成词。

从字符到词的整个过程是没有结构的，只要符合词的规则，就构成词。一般来说，词法设计不会包含冲突。

词法分析技术上可以使用状态机或者正则表达式来进行。

## 词法概述

JavaScript源代码中的输入，可以这样分类
- WhiteSpace 空白字符
- LineTerminator 换行符
- Comment 注释
- Token 词
  - IdentifierName 标识符名称，典型案例是我们使用的变量名，注意这里的关键字也包含在内
  - Punctuator 符号，我们使用的运算符和大括号等符号
  - NumericLiteral 数字直接量，就是我们写的数字
  - StringLiteral 字符串直接量，就是我们用单引号或者双引号引起来的直接量
  - Template 字符串模板，用反引号`括起来的直接量


## WhiteSpace 空白字符


## LineTerminator 换行符


## Comment 注释


## Token 词
  
  
  ### IdentifierName 标识符名称，典型案例是我们使用的变量名，注意这里的关键字也包含在内
  
  
  ### Punctuator 符号，我们使用的运算符和大括号等符号
  
  
  ### NumericLiteral 数字直接量，就是我们写的数字
  
  
  ### StringLiteral 字符串直接量，就是我们用单引号或者双引号引起来的直接量
  
  
  ### Template 字符串模板，用反引号`括起来的直接量


