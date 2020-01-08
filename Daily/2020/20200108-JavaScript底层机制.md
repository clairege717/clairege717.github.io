# 20200108-JavaScript底层机制

- JavaScript执行过程-eventloop
```  
  setTimeout(function(){
      console.log('set1')// 3
  })

  new Promise((resolve)=>{
      console.log('pr1');// 0
      resolve();
  }).then(function(){
      console.log('then1')// 2
  })

  setTimeout(function(){
      console.log('set2')// 4
  })

  console.log(3)// 1
```

**开始执行**      <- 异步任务的回调回到主任务执行 <-
|                                             |
**逐步执行代码**                                |
|                                             |
**有代码异步操作**  -> 异步操作插入到队列 -> **异步队列**
|                                             ^  
**执行完毕**       -> 问询是否有异步    ----------| 


**微任务与宏任务**
  - 微任务: Promise, process.nextTick
  - 宏任务: 整体代码script, setTimeout, setInterval
  
  会先于宏任务执行，微任务队列空了，才会去执行下一个宏任务


- 作用域链与引用类型
```  
  var a = [1, 2, 3];
  function f(a){
      a[3] = 4 // **变量是数组，是引用类型**
      a = [100] // **参数在方法内，相当于一个局部变量**
      console.log(a);// [100]
  }
  f(a);
  console.log(a);// [1,2,3,4]
```

    js 查找变量，会从当前作用域逐级向上，直到window，如果window没有，就是undefined

    **JavaScript的数组并不是数据结构意义上的数组，为什么？**

    1. 数据结构意义上的数组，连续相等内存变量。大小、类型
    2. 真正的数组是不可以扩容的

- v8引擎回收机制
```  
  var size = 20*1024*1024;
  var arrAll = [];
  // v8引擎只有1.4g的内存可以支配，node可以使用C++的内存
  // node，写服务，只要服务开着，全局变量一直不会回收
  for(var i=0;i<20;i+=){
      arrAll.push(new Arrar(size));
  }
```

**内存如何回收**

    内存快接近满
    - 全局变量：不回收
    - 局部变量且失去引用：回收

**内存查看**

  v8引擎-只有1.4g的内存可以支配，node可以使用C++的内存

    - 浏览器：window.performance
    - Node：process.memoryUsage()

**容易引发内存使用不当的情景**

    - 滥用全局变量
    - 缓存不限制
    - 操作大文件