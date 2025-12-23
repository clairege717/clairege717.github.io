# [31 | JavaScript语法（三）：什么是表达式语句？](https://time.geekbang.org/column/article/88827?utm_source=time_web&utm_medium=menu)

事实上，真正能干活的就只有表达式语句，其它语句的作用都是产生各种结构，来控制表达式语句执行，或者改变表达式语句的意义。

## 什么是表达式语句

表达式语句实际上就是一个表达式，它是由运算符连接变量或者直接量构成的。

### PrimaryExpression 主要表达式

表达式的原子项：Primary Expression。是表达式的最小单位，所涉及的语法结构也是优先级最高的。

Primary Expression 包含量各种“直接量”。直接量就是直接用某种语法写出来的具有特定类型的值。通俗的讲，直接量就是在代码中把它们写出来的语法。

- **一些基本类型的直接量**：

```
"abc";
123;
null;
true;
false;
```

- **JavaScript还能直接量的形式定义对象，针对函数、类、数组、正则表达式等特殊对象类型，JavaScript提供了语法层面的支持**：

```
({});
(function(){});
(class{ });
[];
/abc/g;
```

> 注：
> 在语法层面，function、{ 和class 开头的表达式语句与声明语句有语法冲突，所以，我们想要使用这样的表达式，必须加上括号来回避语法冲突。

在JavaScript标准中，这些结构有的被称作直接量（Literal），有的被称作表达式（**Expression），这边都理解成直接量。

- **Primary Expression 还可以是this或者变量，在语法上，把变量称作“标识符引用”**：

```
this;
myVar;
```

- **任何表达式加上圆括号，都被认为是Primary Expression，这个机制使得圆括号成为改变运算优先顺序的手段**：

```
(a + b);
```

### MemberExpression 成员表达式

MemberExpression通常用于访问对象成员。有几种形式：

```
a.b;// 用标识符的属性访问
a["b"];// 用字符串的属性访问
new.target;// 新加入的语法，用于判断函数是否是被new调用
super.b;// super是构造函数中，用于访问父类的属性的语法
```

从语法结构需要，以下两种在JavaScript标准中当作Member Expression

1. 带函数的模板：

```
f`a${b}c`;
```

这个带函数名的模板表示把模板的各个部分算好后传递给一个函数

2. 带参数列表的new 运算

```
new Cls();
```

> 注：不带参数列表的new运算优先级更低，不属于Member Expression。

- **NewExpression NEW 表达式**

- **CallExpression 函数调用表达式**
- **LeftHandSideExpression 左值表达式**
- **AssignmentExpression 赋值表达式**
- **Expression 表达式**
