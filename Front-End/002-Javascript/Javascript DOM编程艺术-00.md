# Javascript DOM 编程艺术

W3C对DOM的定义：一个与系统平台和编程语言无关的接口，程序和脚本可以通过这个接口动态地访问和修改文档的内容、结构和样式。

## Javascript语法

- ### 语法

语言结构方面的各项规则

  - 语句（statement）
  - 注释（comment）
  - 变量（variable）
    
    Javascript允许直接对变量赋值而无需事先声明。如果对某个变量赋值前未声明，赋值操作将自动声明该变量。

    弱类型语言（weakly typed）

  - 数据类型

    1. 字符串(\转义escaping)
    2. 数值
    3. 布尔值
    
    字符串、数值和布尔值都是标量（scalar）：**a variable quantity that cannot be resolved into components**

  - 数组
  - 对象

- ### 操作

- ### 条件语句
- ### 循环语句
- ### 函数

**变量的作用域（scope）**

  - 全局变量（global variable）
  
    可以在脚本的任何位置被引用（全局变量的作用域是整个脚本）

  - 局部变量（local variable）
    
    只存在于声明它的那个函数的内部（局部变量的作用域仅限于某个特定的函数）

**用var关键字明确地为函数变量设定作用域。**

  - 如果在某个函数中使用量var，那个变量将被视为一个局部变量，只存在于这个函数的上下文中
  - 如果没有使用var，那个变量将被视为一个全局变量。如果一个脚本里已经存在一个与之同名的全局变量，这个函数就会改变那个全局变量的值。

- ### 对象（Object）

对象是自包的数据集合，包含在对象里的数据可以通过两种形式访问：
  - 属性（property）
    
    属性是隶属于某个特定对象的变量（Object.property）

  - 方法（method）
    
    方法是只有某个特定对象才能调用的函数（Object.method()）

  1. 内建对象：一系列预先定义好对对象（Array、Date、Math）
  2. 宿主对象：由运行环境提供的预定义对象，Web应用中，环境即浏览器（Form、Image、Element、**document**）

- 

