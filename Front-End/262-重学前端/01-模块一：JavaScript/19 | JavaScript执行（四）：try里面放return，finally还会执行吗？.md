# [19 | JavaScript执行（四）：try里面放return，finally还会执行吗？](https://time.geekbang.org/column/article/83860?utm_source=time_web&utm_medium=menu)

  语句

  常见语句：变量声明、表达式、条件、循环等

  JavaScript语句执行机制涉及的一种基础类型：Completion类型

## Completion类型

```
function foo(){
  try{
    return 0;
  } catch(err) {

  } finally {
    console.log("a")
  }
}

console.log(foo());
```

  finally执行，return语句也生效，foo()返回来结果0。

```
function foo(){
  try{
    return 0;
  } catch(err) {

  } finally {
    return 1;
  }
}

console.log(foo());
```

  finally中的return“覆盖”了try中的return。

  面对如此怪异的行为，可以把它当作一个孤立的知识去记忆，但是实际上，这背后有一套机制在运作。

  这一机制的基础正是JavaScript语句执行的完成状态，我们用一个标准类型来表示：Completion Record（在类型一节中提到过，Completion Record用于描述异常、跳出等语句执行过程）。

  **Completion Record 表示一个语句执行完之后的结果**，有三个字段：
  - [[type]]表示完成的类型，有break continue return throw 和 normal几种类型
  - [[value]]表示语句的返回值，如果语句没有，则是empty
  - [[target]]表示语句的目标，通常是一个JavaScript标签（标签在后文会有介绍）
  
  JavaScript正是依靠语句的Completion Record类型，方才可以在语句的复杂嵌套结构中，实现各种控制。

  接下来，了解JavaScript使用Completion Record类型，控制语句执行的过程。

## 语句的几种分类

![语句的几种分类](https://static001.geekbang.org/resource/image/98/d5/98ce53be306344c018cddd6c083392d5.jpg)

- ### 普通语句
  
  不带控制能力的语句

  - 声明类语句
    - var声明
    - const声明
    - let声明
    - 函数声明
    - 类声明
  
  - 表达式语句
  - 空语句
  - with语句
  - debugger语句
  
  这些语句在执行时，从前到后顺序执行（这里先忽略var和函数声明的预处理机制），没有任何分支或者重复执行逻辑。

  普通语句执行后，会得到[[type]]为normal的Completion Record，JavaScript引擎遇到这一的Completion Record，会继续执行下一条语句。

  这些语句中，只有表达式语句会产生[[value]]，当然，从引擎控制的角度，这个value并没有什么用处。

  如果你经常使用Chrome自带的调试工具，可以知道，输入一个表达式，在控制台可以得到结果，但是在前面加上var，就变成来undefined。

  Chrome控制台显示的正是语句的Completion Record的[[value]]。

- ### 语句块

  语句块就是拿大括号括起来的一组语句，它是一种语句的复合结构，可以嵌套。

  如果语句块内部的语句的Completion Record的[[type]]如果不为normal，会打断语句块后续的语句执行。


  
- ### 控制型语句

  控制型语句带有if、switch关键字，他们会对不同类型的Completion Record产生反应。
  
  - if
  - switch
  - for
    - for
    - for...of
    - for-await-of
    - for...in
  
  - while
    - while
    - do-while
  
  - continue
  - break
  - return
  - throw
  - try

  控制类语句分成两部分，一类是对其内部造成影响，如if、switch、while/for、try。另一类是对外部造成影响，如break、continue、return、throw，这两类语句的配合，会产生控制代码执行顺序和执行逻辑的效果，也是我们编程的主要工作。

  一般来说，for/while-break/continue和try-throw这样比较符合逻辑的组合，是大家熟悉的。

  但是，实际上，我们需要控制语句跟break、continue、return、throw四种类型与控制语句两两组合产生的效果。

  ![break、continue、return、throw四种类型与控制语句两两组合](https://static001.geekbang.org/resource/image/77/d3/7760027d7ee09bdc8ec140efa9caf1d3.png)

  最开始的例子中，因为finally中的内容必须保证执行，所以try/catch执行完毕，即使得到的结果是非normal型的完成记录，也必须要执行finally。

  而当finally执行也得到来非 normal记录，则会使finally中的记录作为整个try结构的结果。

- ### 带标签的语句

  Completion Record的最后一个字段：target，涉及来JavaScript中的一个语法，带标签的语句。

  实际上，任何JavaScript语句是可以加标签的，在语句前加冒号即可：

```
    firstStatement: var i = 1;
```

  大部分的时候，这个东西类似于注释，没有任何用处。

  唯一有作用的时候：与完成记录类型中的target相配合，用于跳出多层循环。

```
    outer: while(true) {
      inner: while(true) {
          break outer;
      }
    }
    console.log("finished")
```

  break/continue 语句如果后跟了关键字，会产生带target的完成记录。一旦完成记录带了target，那么只有拥有对应label的循环语句会消费它。



## 结语

因为JavaScript语句存在这嵌套关系，所以执行过程实际上主要在一个树形结构上进行，树形结构的每一个节点执行后产生Completion Record，根据语句的结构和Completion Record，JavaScript实现了各种分支和跳出逻辑。


