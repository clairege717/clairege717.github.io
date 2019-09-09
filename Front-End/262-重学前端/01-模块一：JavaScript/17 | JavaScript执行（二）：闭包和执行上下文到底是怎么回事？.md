# [17 | JavaScript执行（二）：闭包和执行上下文到底是怎么回事？](https://time.geekbang.org/column/article/83302?utm_source=time_web&utm_medium=menu)

函数的执行过程相关的知识
- 闭包
- 作用域链
- 执行上下文
- this值

## 闭包
  
  closure：编程语言领域，表示一种函数

  简单理解下：闭包其实只是一个绑定了执行环境的函数。

  闭包与普通函数的区别是，它携带了执行的环境。

  闭包组成部分
  - 环境部分
    - 环境：函数的词法环境（执行上下文的一部分）
    - 标识符列表：函数中用到的未声明的变量
  - 表达式部分：函数体

  

## 执行上下文：执行的基础设施

  JavaScript标准把一段代码（包括函数），执行所需的所有信息定义为：“执行上下文”。

  **执行上下文在ES3中**，包含三个部分：
  - scope：作用域，也常常被叫做作用域链
  - variable object：变量对象，用于存储变量的对象
  - this value：this值
  
  **在ES5中**，改进了命名方式，把执行上下文最初的三个部分改为下面的样子：
  - lexical environment：词法环境，当获取变量时使用
  - variable environment：变量环境，当声明变量时使用
  - this value：this值
  
  在ES2018中，执行上下文又有改变，this值被归入lexical environment，但是增加了不少内容：
  - lexical environment：词法环境，当获取变量或者this值时使用
  - variable environment：变量环境，当声明变量时使用
  - code evaluation state：用于恢复代码执行位置
  - Function：执行的任务是函数时使用，表示正在执行的函数
  - Realm：使用的基础库和内置对象实例
  - Generator：仅生成器上下文有这个属性，表示当前生成器
  
```
var b = {}
let c = 1
this.a = 2;
```

  想要正确执行这段代码，我们需要知道：
  1. var 把 b 声明到哪里
  2. b 表示哪个变量
  3. b 的原型是哪个对象
  4. let 把 c 声明到哪里
  5. this 指向哪个对象

### var声明与赋值

```
var b = 1
```

  声明b，并赋值为1。

  var 声明作用域函数执行的作用域。也就是说，var 会穿透 for 、if 等语句

  在只有var，没有let 的JavaScript时代，诞生了一个技巧：立即执行的函数表达式（IIFE：immediately invoked functional expression）：通过创建一个函数，并且立即执行，来构造一个新的域，从而控制var的范围。

```
;(function(){
    var a;
    //code
}())


;(function(){
    var a;
    //code
})()

```
  由于语法规定了function关键字开头是函数声明，所以要想让函数变成函数表达式，我们可以加括号。

  但是，如果上一行代码不写分号，括号会被解释为上一行代码最末的函数调用。所以，一些代码风格规范，会要求在括号前加上分号。

```
void function(){
    var a;
    //code
}();
```
  
  可以加void。有效避免了语法问题。同时，语义上void运算表示忽略后面表达式的值，变成undefined，我们确实不关心IIFE的返回值，所以语义也更为合理。

### let

 let是ES6开始引入的新的变量声明模式。

 为了实现let，JavaScript在运行时引入了块级作用域。即：在let出现之前，JavaScript的if for等语句皆不产生作用域。

 以下为会产生let使用的作用域：
 - for
 - if
 - switch
 - try/catch/finally

### Realm

  在新的标准（9.0）中，JavaScript引入了一个新的概念Realm，中文意思是“国度”“领域”“范围”。这个英文用法有点比喻的意思，几个翻译都不太适合，这里不翻译。

```
var b = {}
```

  在ES2016前的版本中，标准中很少提及{}的原型问题。但在实际但前端开发中，通过iframe等方式创建多window环境并非罕见的操作，所以才促成了新概念Realm的引入。

  Realm中包含一组完整的内置对象，而且是复制关系。

  对于不同Realm中的对象操作，会有一些需要格外注意的问题，比如instanceOf几乎是失效的。

  以下代码展示了在浏览器环境中，获取来自两个Realm的对象，他们跟本土的Object及instanceOf时会产生差异：

```
var iframe = document.createElement('iframe')
document.documentElement.appendChild(iframe)
iframe.src="javascript:var b = {};"

var b1 = iframe.contentWindow;
var b2 = {};

console.log(typeof b1, typeof b2); //object object

console.log(b1 instanceof Object, b2 instanceof Object); //false true
```

  由于b1、b2由同样的代码"{}"在不同的Realm中执行，所以表现出了不同的行为。