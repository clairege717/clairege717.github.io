# 16 | JavaScript执行（一）：Promise里的代码为什么比setTimeout先执行？

**微观任务优先于宏观任务！**

**JavaScript引擎发起的任务优先于宿主浏览器环境API发起的任务**

这一部分我们来讲一讲 JavaScript 的执行。

首先我们考虑一下，如果我们是浏览器或者 Node 的开发者，我们该如何使用JavaScript引擎。

当拿到一段JavaScript代码时，浏览器或者Node环境首先要做的就是：传递给JavaScript引擎，并且要求它去执行。

然而，宿主环境当遇到一些事件时，会继续把一段代码传递给JavaScript引擎去执行，此外，我们可能还会提供API给JavaScript引擎，比如setTimeOut这样的API，它会运行JavaScript在特定的时机执行。

所以，我们首先应该形成一个感性的认知：**一个JavaScript引擎会常驻于内存中，它等待着我们（宿主）把JavaScript代码或者函数传递给它执行**。

由于我们在这里主要讲JavaScript语言，那么采纳JSC引擎的术语，我们**把宿主发起的任务称为宏观任务，把JavaScript引擎发起的任务称为微观任务**。

## 宏观任务和微观任务
  
  **JavaScript 引擎等待宿主环境分配宏观任务**，在操作系统中，通常等待的行为都是一个事件循环，所以在Node术语中，也会把这个部分称为事件循环。

  在底层的C/C++代码中，这个事件循环是一个跑在独立线程中的循环，我们用伪代码来表示，大概为：
  
  ```
  while(TRUE) {
    r = wait();
    execute(r);
  }
  ```
  
  整个循环的过程，基本就是反复“等待-执行”。当然，实际的代码中，还有要判断循环是否结束、宏观任务队列等逻辑。

  这里每次的执行过程，其实都是一个宏观任务。可以大致理解：**宏观任务的队列就相当于事件循环**。

  在宏观任务中，JavaScript的Promise还会产生异步代码，JavaScript必须保证这些异步代码在一个宏观任务中完成，因此，每个宏观任务中又包含来一个微观任务队列。

  有了宏观任务和微观任务机制，我们就可以实现JS引擎级和宿主级的任务了。例如：**Promise永远在队列尾部添加微观任务。setTimeout等宿主API，则会添加宏观任务**。

## Promise
  
  Promise 是 JavaScript语言提供的一种标准化的异步管理方式，它的总体思想是，**需要进行io、等待或者其他异步操作的函数，不返回真实结果，而返回一个“承诺”，函数的调用方可以在合适的时机，选择等待这个承诺对象（即Promise的then方法的回调）**。

  Promise的基本用法示例如下：
  ```
  function sleep(duration) {
    return new Promise(function(resolve, reject) {
        setTimeout(resolve,duration);
    })
  }
  sleep(1000).then( ()=> console.log("finished"));
  ```

  异步执行顺序
  1. 首先分析有多少个宏任务
  2. 在每个宏任务中，分析有多少个微任务
  3. 根据调用次序，确定宏任务中的微任务执行次序
  4. 根据宏任务的出发规则和调用次序，确定宏任务的执行次序
  5. 确定整个顺序
  
  复杂示例：
   ```
    function sleep(duration) {
        return new Promise(function(resolve, reject) {
            console.log("b");
            setTimeout(resolve,duration);
        })
    }
    console.log("a");
    sleep(5000).then(()=>console.log("c"));
   ```
   
   这是一段非常常用的封装方法，利用Promise把setTimeout封装成可以用于异步的函数

## 新特性 async和await
  
  async函数必定返回Promise，我们把所有返回Promise的函数都可以认为是异步函数。

  async函数是一种特殊语法，特征是在function 关键字之前加上async关键字，这样，就定义了一个async函数，我们可以在其中使用await来等待一个Promise。

```
function sleep(duration) {
    return new Promise(function(resolve, reject) {
        setTimeout(resolve,duration);
    })
}
async function foo(){
    console.log("a")
    await sleep(2000)
    console.log("b")
}
```

  


