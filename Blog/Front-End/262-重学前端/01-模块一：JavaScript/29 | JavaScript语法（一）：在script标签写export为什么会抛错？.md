# [29 | JavaScript语法（一）：在script标签写export为什么会抛错？](https://time.geekbang.org/column/article/87808?utm_source=time_web&utm_medium=menu)


本节介绍JavaScript语法的一些基本规则

## 脚本和模块

JavaScript有两种源文件，一种叫做脚本，一种叫做模块。

这个区分是在ES6引入了模块机制开始的，在ES5和之前的版本中，就只有一种源文件类型（即脚本）。

脚本是可以由浏览器或者node环境引入执行的，而模块只能由JavaScript代码用import引入执行。

从概念上，可以认为，脚本具有主动性的JavaScript代码段，是控制宿主完成一定任务的代码；而模块是被动性的JavaScript代码段，是等待被调用的库。

对标准中的语法产生式做一些对比，可以发现，模块和脚本之间的区别仅仅在于是否包含import和export。

脚本是一种兼容之前的版本的定义。在这个模式下，没有import就不需要处理加载“.js”文件问题。

现代浏览器，可以支持使用script标签引入模块或者脚本，如果要引入模块，必须给script标签添加type="module"。如果引入脚本，则不需要type。

```
<script type="module" src="xxxxx.js"></script>
```

脚本中可以包含语句。模块中可以包含三种内容：import声明，export声明和语句。

![脚本中可以包含语句。模块中可以包含三种内容：import声明，export声明和语句。](https://static001.geekbang.org/resource/image/43/44/43fdb35c0300e73bb19c143431f50a44.jpg)


## 三种语法结构

- import声明
- export声明
- 函数体

### import声明

```
import "mod"; // 引入一个模块
import v from "mod";  // 把模块默认的导出值放入变量 v
```
  
   保证这个模块代码被执行，引用它的模块是无法获得它的任何信息的

- 直接import一个模块

- 带from的import，能引入模块里的一些信息
  
  引入模块中的一部分信息，可以把他们变成本地的变量

  - import x from "./a.js" 引入模块中导出的默认值
    - import d,{a as x,modify} from "a.js"
    - import d.* as x from "a.js"

        语法要求，不带as的默认值永远在最前

  - import {a as x,modify} from "a.js" 引入模块中的变量
  - import * as x from "a.js" 把模块中所有的变量以类似对象属性的方式引入


### export声明

- 独立使用export声明

```
export {a, b, c};
```

- 直接在声明型语句前添加export关键字
  - var 
  - function(含async和generator)
  - class
  - let
  - const
- 跟default联合使用
  
  export default表示导出一个默认变量值。可用于function和class。

  这里导出的变量是没有名称的，可以使用import x from "./a.js"在模块中引入。
  - export default function
  - export default class
  
  export default 后面可以跟一个表达式。
  - export default 表达式
  
  ```
  var a = {};
  export default a;
  ```

  这里的行为跟导出变量是不一致的，这里导出的是值，导出的就是普通变量a的值，以后a的变化与导出的值就无关了，修改变量a，不会使得其它模块中引入的default值发生改变。


在import语句前无法加入export，但是我们可以直接使用export from语法

```
export a from "a.js"
```



JavaScript引擎除了执行脚本和模块之外，还可以执行函数。而函数体跟脚本和模块有一定的相似之处。

### 函数体

执行函数的行为，通常是在JavaScript代码执行时，注册宿主环境的某些事件触发的，而执行过程，就是执行函数体。

```
setTimeout(function(){
    console.log("go go go");
}, 10000)
```

这段代码通过setTimeout函数注册了一个函数给宿主，当一定时间之后，宿主就会执行这个函数。

当我们学习了语法后，我们可以认为，宏任务中可能会执行的代码包括“脚本（script）”“模块（module）”和函数体（function body）“。

函数体其实也是一个语句列表。跟脚本和模块比起来，函数体的语句列表中多了return语句可以使用。

四种函数体
- 普通函数体
  ```
  function foo(){
    //Function body
  }
  ```

- 异步函数体

```
async function foo(){
    //Function body
}
```

- 生成器函数体

```
function *foo(){
    //Function body
}
```

- 异步生成器函数体

```
async function *foo(){
    //Function body
}
```

四种函数体的区别在于：能否使用await和yield语句。

关于函数体、模块和脚本能使用的语句：

类型 | yield | await | return | import & export
--- | ----- | ----- | ------ | ---------------
普通函数体 | N | N | Y | N
异步函数体 | N | Y | Y | N
生成器函数体 | Y | N | Y | N
异步生成器函数体 | Y | Y | Y | N
脚本 | N | N | N | N 
模块 | N | N | N | Y 


## 全局语法机制
- 预处理
- 指令序言

不理解预处理机制，就无法理解var等声明类语句的行为。

不理解指令序言，就无法解释严格模式。

### 预处理

JavaScript执行前，会对脚本、模块和函数体中的语句进行预处理。预处理过程将会提前处理var、函数声明、class、const和let这些语句，以确定其中变量的意义。

- **var声明**
  
  var声明永远作用于脚本、模块和函数体这个级别，在预处理阶段，不关心赋值的部分，只管在当前作用域声明这个变量。

```
var a = 1;// 脚本级别的a

function foo() {
    console.log(a);// 函数体级别的变量a此时还没赋值，所以是undefined
    var a = 2;// 函数体级别的a。预处理过程在执行前，所以有函数体级别的变量a，就不会去访问外层作用域中的变量a。
}

foo();// undefined
```

```
var a = 1;

function foo() {
    var o= {a:3}
    with(o) {// 用with(o)创建了一个作用域，并把o对象加入词法环境，在其中使用了var a = 2;语句
        var a = 2;
    }
    console.log(o.a);// 
    console.log(a);// 
}

foo();// 2 和 undefined
```

  因为早年JavaScript没有let和const，只能用var，又因为var除了脚本和函数体都会穿透，所以发明了“立即执行的函数表达式（IIFE）”这一用法，用来产生作用域。

```
//  为文档添加20个div元素，并绑定click事件，打印他们的序号。
for(var i = 0; i < 20; i ++) {
    void function(i){
        var div = document.createElement("div");
        div.innerHTML = i;
        div.onclick = function(){
            console.log(i);
        }
        document.body.appendChild(div);
    }(i);
}

```

  如果不用IIFE：
```
for(var i = 0; i < 20; i ++) {
    var div = document.createElement("div");
    div.innerHTML = i;
    div.onclick = function(){
        console.log(i);
    }
    document.body.appendChild(div);
}
```

这段代码的结果将会是点每个div都打印20，因为全局只有一个i，执行完循环后，i变成了20。


- **function声明**
  
  function声明的行为原本跟var非常相似，但是在最新的JavaScript标准中，对他进行了一定的修改，这让情况变复杂了。

  在全局（脚本、模块和函数体），function声明表现跟var相似。不同之处在于，function声明不但在作用域中加入变量，还会给他赋值。

```
console.log(foo);// ƒ foo(){}
function foo(){

}
```

  function 声明出现在if等语句中的情况有点复杂，它仍然作用于脚本、模块和函数体级别，在预处理阶段，仍然会产生变量，它不再被提前赋值。

```
console.log(foo);// undefined。如果没有函数声明，则会抛出错误。
if(true) {
    function foo(){

    }
}
```
  
  这段说明function在预处理阶段仍然发生了作用，在作用域中产生了变量，没有产生赋值，赋值行为发生在了执行阶段。

  出现在if等语句中的function，在if创建的作用域中仍然会被提前，产生赋值效果。


- **class声明**
  
  class声明在全局的行为跟function和var都不一样。
  
  在class声明之前使用class名，会抛错。

  class的声明作用不会穿透if等语句结构，所以只有写在全局环境才会有声明作用。


### 指令序言机制

  这里的指令序言最早是为了use strict设计的，它规定了一种给JavaScript代码添加元信息的方式。

```
"use strict";
function f(){
    console.log(this);
};
f.call(null);// null
```

  这段代码展示了严格模式的用法。

  定义了f，f中打印this值，然后用call的方法调用f，传入null作为this值，我们可以看到最终结果是null被当作this值打印，这是严格模式的特征。

  如果去掉严格模式，打印的结果将会是global。

  “use strict”是JavaScript标准中规定的唯一一种指令序言，设计指令序言的目的是，留给JS的引擎和实现者一些统一的表达方式，在静态扫描时指定JS代码的一些特性。

  例如：假设我们要设计一种声明本文件不需要进行lint检查的指令，可以这样设计：

```
"no lint";
"use strict";
function doSth(){
    //......
}
//......
```

  JavaScript的指令序言是只有一个字符串直接量的表达式语句，它只能出现在脚本、模块和函数体的最前面。

  



