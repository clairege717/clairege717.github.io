# [【React踩坑记】React项⽬目报错Can't perform a React state update on an unmounted component](https://blog.csdn.net/twodogya/article/details/86620289)


    意思为:我们不不能在组件销毁后设置state，防⽌止出现内存泄漏漏的情况 分析出现问题的原因:

我这⾥里里在组件加载完成的钩⼦子函数⾥里里调⽤用了了⼀一个EventBus的异步⽅方法， 如果监听到异步⽅方法，则会更更新state中isShowNav的值。

    解决⽅方法 我们应该在组件销毁的时候将异步⽅方法撤销


# Can't perform a React state update on an unmounted component.

https://blog.csdn.net/u010395357/article/details/87990271 

字面意思是：无法对卸载的的组件执行响应状态更新，也就是卸载后的组件不能设置state状态。

警告详情：

> ​    Can't perform a React state update on an unmounted component. 
> This is a no-op, but it indicates a memory leak in your application.
>
> ​    To fix, cancel all subscriptions and asynchronous tasks in the componentWillUnmount method

#### 这种问题一般是由于延时设置state值，或者是异步状态下设置state值导致的。

解决方案代码如下：

- 如果代码中有定时器一类的延时设置state状态的代码，可以在组件销毁时清除定时器

  ```js
  componentWillUnmount() {
      clearTimeout(timer);
  }
  ```

- 如果有异步设置state值的情况，在组件销毁时清除所有的state状态

  ```javascript
  componentWillUnmount() {
      this.setState = (state, callback) => {
          return
      }
  }
  ```

  
# RN 常⻅见问题
   ExceptionsManager.js:74 (0 , _redux.default) is not a function

In Reducer (Index.js), change the import statement to import { combineReducers } from "redux"

   ExceptionsManager.js:74 (0 , _redux.default) is not a function

1. combineReducers
    
    import { combineReducers } from "redux"
    
2. connect
    
    import { connect } from 'react-redux'
    
3. actions
    
    In my case adding {} to the import from my actions resolved this issue!
    
     