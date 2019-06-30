# [18 | JavaScript执行（三）：你知道现在有多少种函数吗？](https://time.geekbang.org/column/article/83719?utm_source=time_web&utm_medium=menu)

## 函数

### 第一种，普通函数：用function关键字定义的函数
```
function foo(){
    // code
}
```

### 第二种，箭头函数：用=>运算符定义的函数
```
const foo = () => {
    // code
}
```

### 第三种，方法：在class中定义的函数
```
class C {
    foo(){
        //code
    }
}
```

### 第四种，生成器函数：用function * 定义的函数
```
function* foo(){
    // code
}
```

### 第五种，类：用class定义的类，实际上也是函数
```
class Foo {
    constructor(){
        //code
    }
}
```

### 第六/七/八种，异步函数：普通函数、箭头函数和生成器函数加上async关键字
```
async function foo(){
    // code
}
const foo = async () => {
    // code
}
async function foo*(){
    // code
}
```

  **对于普通变量而言，这些函数并没有本质区别，都是遵循了“继承定义时环境”的规则，他们的一个行为差异在于this关键字。**

## this关键字的行为

  this是JavaScript中的一个关键字，它的使用方法类似于一个变量（但是this跟变量的行为有很多不同）。

  **this是执行上下文中很重要的一个组成部分。同一个函数调用方式不同，得到的this值也不同。**

```
function showThis(){
    console.log(this);
}

var o = {
    showThis: showThis
}

showThis(); // global
o.showThis(); // o
```
  
  普通函数的this值，由”调用它所使用的引用“决定，其中的奥秘在于：我们获取函数的表达式，它实际上返回的并非函数本身，而是一个Reference类型。

  Reference类型由两部分组成：一个对象和一个属性值。

  当做一些算数运算（或者其他运算时），Reference类型会被解引用，即获取真正当值（被引用当内容）来参与运算，而类似函数调用、delete等操作，都需要用到Reference类型中都对象。

  即：**调用函数时使用都引用，决定来函数执行时刻都this值**。

  实际上从运行时的角度来看，this跟面向对象毫无关联，它是与函数调用时使用的表达式相关。

  如果，把例子中的普通函数改为箭头函数：

```
const showThis = () => {
    console.log(this);
}

var o = {
    showThis: showThis
}

showThis(); // global
o.showThis(); // global
```
  
  不论用什么引用调用，都不影响this值。

  接下来看方法：

```
class C {
    showThis() {
        console.log(this);
    }
}
var o = new C();
var showThis = o.showThis;

showThis(); // undefined
o.showThis(); // o
```

  以上，生成器函数、异步生成器函数和异步普通函数跟普通函数行为一致，异步箭头函数跟箭头函数行为一致。

## this 关键字的机制

  函数能够引用定义时的变量，如上文分析，函数也能记住定义时的this。因此，函数内部必定有一个机制来保存这些信息。

  在JavaScript标准中，为函数规定来用来保存**定义时上下文的私有属性[[Environment]]**

  当一个函数**执行时**，会创建一条新的执行环境记录，记录的**外层词法环境（outer lexical environment）会被设置成函数的[[Environment]]**。

  这个动作就是**切换上下文**。例如：

```
var a = 1;
foo();

在别处定义了 foo：

var b = 2;
function foo(){
    console.log(b); // 2
    console.log(a); // error
}
```

  这里的foo能够访问b（定义时词法环境），却不能访问a（执行时的词法环境），这就是执行上下文的切换机制了。

  JavaScript用一个栈来管理执行上下文，这个栈中的每一项又包含一个链表。如下图：

  ![执行上下文-栈及链表](https://static001.geekbang.org/resource/image/e8/31/e8d8e96c983a832eb646d6c17ff3df31.jpg)

  当函数调用时，会入栈一个新的执行上下文，函数调用结束时，执行上下文被出栈。

  而this则是一个更为复杂的机制，JavaScript标准定义了[[thisMode]]私有属性。

  [[thisMode]]私有属性有三个取值：
  - lexical：表示从上下文中找出this，这对应来箭头函数
  - global：表示当this为undefined时，取全局对象，对应来普通函数
  - strict：当严格模式时使用，this严格按照调用时传入的值，可能为null或者undefined
  
  方法的行为跟普通函数有差异，恰恰是因为class设计成了默认按strict模式执行。

```
"use strict"
function showThis(){
    console.log(this);
}

var o = {
    showThis: showThis
}

showThis(); // undefined
o.showThis(); // o
```

  此时，普通函数跟方法效果一样。

  函数创建新的执行上下文中的词法环境记录时，会根据[[thisMode]]来标记新记录的[[ThisBindingStatus]]私有属性。

  代码执行遇到this时，会逐层检查当前词法环境记录中的[[ThisBindingStatus]]，当找到有this的环境记录时获取this的值。

  这样的规则的实际效果是，嵌套的箭头函数中的代码都指向外层this。例如：

```
var o = {}
o.foo = function foo(){
    console.log(this);
    return () => {
        console.log(this);
        return () => console.log(this);
    }
}

o.foo()()(); // o, o, o
```

  在这个例子中，我们定义来三层嵌套的函数，最外层为普通函数，两层都是箭头函数。

  这里调用三个函数，获得的this值是一致的，都是对象o。

## 操作this的内置函数

  Function.prototype.call和Function.prototype.apply可以指定函数调用时传入的this值。

```
function foo(a, b, c){
    console.log(this);
    console.log(a, b, c);
}
foo.call({}, 1, 2, 3);
foo.apply({}, [1, 2, 3]);
```

  这里call和apply作用一样，只是传参方式有区别。

  Function.prototype.bind，可以生成一个绑定过的函数，这个函数的this值固定来参数。

```
function foo(a, b, c){
    console.log(this);
    console.log(a, b, c);
}
foo.bind({}, 1, 2, 3)();
```

  call、bind、apply用于不接受this的函数类型如箭头、class都不会报错，这个时候，他们无法实现改变this的能力，但是可以实现传参。







