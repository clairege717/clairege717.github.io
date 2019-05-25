# Vue的坑

- [Vue数据改变，视图未更新](https://www.cnblogs.com/YuKiee/p/9681151.html)

    [Vue深入响应式原理](https://cn.vuejs.org/v2/guide/reactivity.html)

  - 对象更改检测

    在一个组件实例中，只有在data里初始化的数据才是响应的，Vue不能检测到对象属性的添加或删除，没有在data里声明的属性不是响应的。

    Vue不允许在已经创建的实例上动态添加根级响应式属性，但是可以使用$set方法将相应属性添加到嵌套的对象上。

    用Vue.set(**object**, key, value) 【或 this.$set(**object**,key,value)】 方法将响应属性添加到嵌套的对象上。注意：**object** 必须是在data中已经声明的对象。

    Vue.set(object,key,value)方法一次只能添加一个属性，如果需要向嵌套对象上添加多个属性，可以用**Object.assign**方法。**object.assign**方法用于将所有可枚举属性的值从一个或多个源对象复制到目标对象，并返回目标对象。


  - 数组渲染问题

    通过改动两种方式改动数组时，Vue检测不到变动：1.利用索引直接设置一个项；2.修改数组长度。

    this.trees[idx] = 'x'//无响应

    this.$set(this.trees,idx,'x')//有响应

    this.trees.splice(idx,1,'x')//有响应





