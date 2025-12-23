# Vue基础内容相关

## Vue项目目录结构分析
使用 vue init webpack-simple vuedemo01 创建
- vuedemo01
  - node_modules
  - src
    - assets
    - App.vue：Vue根组件
      - template
        > 注：Vue模板里，所有内容要被一个根节点包含起来。 
        ```
        <template>
            <div id="app">
                balabala...
            </div>
        </template>
        ```
      - script
        ```
        <script>
            export default {
                name: 'app',
                data () { 
                    // 业务逻辑里定义的数据
                    return {
                        msg: 'Welcome to Your Vue.js App'
                    }
                },
                components:{
                    // 挂载组件
                    // 组件名称不能与HTML标签重复
                },
                methods:{
                    // 数据操作
                },
                mounted:{
                    // 生命周期函数，vue页面刷新就会触发的方法
                }
            }
        </script>
        ```
      - style

        ```
        <style lang="scss" scoped>
            /*css  局部作用域  scoped*/
            h2{
                color:red
            }
        </style>
        ```

        - CSS
        - SCSS
        - SASS
    - main.js
  - .babelrc
  - .editorconfig
  - .gitignore
  - index.html
  - package-lock.json
  - package.json
  - README.md
  - webpack.config.js

## Vue模板语法
##### {{}},v-text,v-html,v-bind:[attribute],v-on[event],v-for,v-if
1. #### 插值
   - 文本：**{{}}** **v-text**
  
        `<span>Message: {{ msg }}</span>`
    > - Mustache 标签将会被替代为对应数据对象上 msg 属性的值。无论何时，绑定的数据对象上 msg 属性发生了改变，插值处的内容都会更新。
    > - 通过使用 **v-once** 指令，你也能执行一次性地插值，当数据改变时，插值处的内容不会更新。但请留心这会影响到该节点上的其它数据绑定：
    > 
    >   `<span v-once>这个将不会改变: {{ msg }}</span>`



   - 原始HTML：**v-html**
        ```
        <p>Using mustaches: {{ rawHtml }}</p>
        <p>Using v-html directive: <span v-html="rawHtml"></span></p>
        ```
        这个 span 的内容将会被替换成为属性值 rawHtml，直接作为 HTML——会忽略解析属性值中的数据绑定。注意，你不能使用 v-html 来复合局部模板，因为 Vue 不是基于字符串的模板引擎。反之，对于用户界面 (UI)，组件更适合作为可重用和可组合的基本单位。 
        > 你的站点上动态渲染的任意 HTML 可能会非常危险，因为它很容易导致 XSS 攻击。请只对可信内容使用 HTML 插值，绝不要对用户提供的内容使用插值。

   - 特性
    
        HTML特性时，使用 **v-bind** 指令：
        
            `<div v-bind:id="dynamicId"></div>`

        在布尔特性的情况下，它们的存在即暗示为 true，v-bind 工作起来略有不同，在这个例子中：

            `<button v-bind:disabled="isButtonDisabled">Button</button>`

        如果 isButtonDisabled 的值是 null、undefined 或 false，则 disabled 特性甚至不会被包含在渲染出来的 `<button>` 元素中。
        
   - 使用JavaScript表达式

        对于所有的数据绑定，Vue.js 都提供了完全的 JavaScript 表达式支持。
        ```
            {{ number + 1 }}
            {{ ok ? 'YES' : 'NO' }}
            {{ message.split('').reverse().join('') }}
            <div v-bind:id="'list-' + id"></div>
        ```
        > 注： 
        > - 每个绑定都只能包含单个表达式
        > - 模板表达式都被放在沙盒中，只能访问全局变量的一个白名单，如 Math 和 Date 。你不应该在模板表达式中试图访问用户定义的全局变量。

2. #### 指令：指令 (Directives) 是带有 v- 前缀的特殊特性。
   
   指令特性的值预期是单个 JavaScript 表达式 (v-for 是例外情况，稍后我们再讨论)。
   
   指令的职责是，当表达式的值改变时，将其产生的连带影响，响应式地作用于 DOM。

   - 参数

        一些指令能够接收一个“参数”，在指令名称之后以冒号表示。
        
        `<a v-bind:href="url">...</a>`

        v-bind 指令可以用于响应式地更新 HTML 特性。在这里 href 是参数，告知 v-bind 指令将该元素的 href 特性与表达式 url 的值绑定。
        
        `<a v-on:click="doSomething">...</a>`

        v-on 指令，它用于监听 DOM 事件。在这里参数是监听的事件名。

   - 动态参数

        `<a v-bind:[attributeName]="url"> ... </a>`
        
        **用方括号括起来的 JavaScript 表达式作为一个指令的参数。**
        
        这里的 attributeName 会被作为一个 JavaScript 表达式进行动态求值，求得的值将会作为最终的参数来使用。例如，如果你的 Vue 实例有一个 data 属性 attributeName，其值为 "href"，那么这个绑定将等价于 v-bind:href。

        `<a v-on:[eventName]="doSomething"> ... </a>`

        **可以使用动态参数为一个动态的事件名绑定处理函数。**

        当 eventName 的值为 "focus" 时，v-on:[eventName] 将等价于 v-on:focus。

        > 约束：
        > - **对动态参数的值的约束**
        > 
        >   动态参数预期会求出一个字符串，异常情况下值为 null。这个特殊的 null 值可以被显性地用于移除绑定。任何其它非字符串类型的值都将会触发一个警告。
        > - **对动态参数的表达式的约束**
        > 
        >   动态参数表达式有一些语法约束，因为某些字符，例如空格和引号，放在 HTML 特性名里是无效的。
        > 
        >   例如，下面的代码是无效的：
        >   ```
        >   <!-- 这会触发一个编译警告 -->
        >   <a v-bind:['foo' + bar]="value"> ... </a>
        >   ```
        >   变通的办法是使用没有空格或引号的表达式，或用计算属性替代这种复杂表达式。

   - 修饰符

        修饰符 (modifier) 是以半角句号 . 指明的特殊后缀，用于指出一个指令应该以特殊方式绑定。

        `<form v-on:submit.prevent="onSubmit">...</form>`

        .prevent 修饰符告诉 v-on 指令对于触发的事件调用 event.preventDefault()

3. #### 缩写
   
   Vue 为 v-bind 和 v-on 这两个最常用的指令，提供了特定简写
   - v-bind缩写

        ```
        <!-- 完整语法 -->
        <a v-bind:href="url">...</a>

        <!-- 缩写 -->
        <a :href="url">...</a>
        ```
   - v-on缩写

        ```
        <!-- 完整语法 -->
        <a v-on:click="doSomething">...</a>

        <!-- 缩写 -->
        <a @click="doSomething">...</a>
        ```

## Class与Style绑定(v-bind:class,v-bind:style)

1. 绑定HTML Class
    - 对象语法
        - 一个对象，一个或多个class

            `<div v-bind:class="{ active: isActive }"></div>`
            
            `<div class="static" v-bind:class="{ active: isActive, 'text-danger': hasError }"></div>`

            ```
            data: {
                isActive: true,
                hasError: false
            }
            ```
        - 在模板中定义数据对象

            `<div v-bind:class="classObject"></div>`

            ```
            data: {
            classObject: {
                active: true,
                'text-danger': false
            }
            }
            ```
        - 绑定一个返回对象的计算属性

            `<div v-bind:class="classObject"></div>`

            ```
            data: {
                isActive: true,
                error: null
            },
            computed: {
                classObject: function () {
                    return {
                        active: this.isActive && !this.error,
                        'text-danger': this.error && this.error.type === 'fatal'
                    }
                }
            }
            ```

    - 数组语法
      - 把一个数组传给 v-bind:class

        `<div v-bind:class="[activeClass, errorClass]"></div>`
        ```
        data: {
        activeClass: 'active',
        errorClass: 'text-danger'
        }
        ```
      - 用三元表达式根据条件切换列表中的 class

        `<div v-bind:class="[isActive ? activeClass : '', errorClass]"></div>`

      - 在数组语法中也可以使用对象语法：
        
        `<div v-bind:class="[{ active: isActive }, errorClass]"></div>`

    - 用在组件上

        当在一个自定义组件上使用 class 属性时，这些类将被添加到该组件的根元素上面。这个元素上已经存在的类不会被覆盖。

        例如，如果你声明了这个组件：

            ```Vue.component('my-component', {
            template: '<p class="foo bar">Hi</p>'
            })```
        然后在使用它的时候添加一些 class：

            `<my-component class="baz boo"></my-component>`
        HTML 将被渲染为:

            `<p class="foo bar baz boo">Hi</p>`

        对于带数据绑定 class 也同样适用：

            `<my-component v-bind:class="{ active: isActive }"></my-component>`
        当 isActive 为 truthy 时，HTML 将被渲染成为：

            `<p class="foo bar active">Hi</p>`


        > #### ***truthy***:
        > 
        > 在 JavaScript 中，Truthy (真值)指的是在 布尔值 上下文中转换后的值为真的值。所有值都是真值，除非它们被定义为 falsy (即除了 false，0，""，null，undefined 和 NaN 外)。
        > 
        > JavaScript 在布尔值上下文中使用强制类型转换（coercion）。
        > 
        > JavaScript 中的真值示例如下（将被转换为 true，if 后的代码段将被执行）：
        > 
        > ```if (true)
        > if ({})
        > if ([])
        > if (42)
        > if ("foo")
        > if (new Date())
        > if (-42)
        > if (3.14)
        > if (-3.14)
        > if (Infinity)
        > if (-Infinity)
        > ```
        > <br/>



2. 绑定内联式样
    - 对象语法

        v-bind:style 的对象语法十分直观——看着非常像 CSS，但其实是一个 JavaScript 对象。CSS 属性名可以用驼峰式 (camelCase) 或短横线分隔 (kebab-case，记得用单引号括起来) 来命名：

        `<div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>`

        ```
        data: {
            activeColor: 'red',
            fontSize: 30
        }
        ```

        直接绑定到一个样式对象通常更好，这会让模板更清晰：

        `<div v-bind:style="styleObject"></div>`

        ```
        data: {
        styleObject: {
            color: 'red',
            fontSize: '13px'
        }
        }
        ```

        同样的，对象语法常常结合返回对象的计算属性使用。


    - 数组语法

        v-bind:style 的数组语法可以将多个样式对象应用到同一个元素上：

        `<div v-bind:style="[baseStyles, overridingStyles]"></div>`

    - 自动添加前缀

        当 v-bind:style 使用需要添加浏览器引擎前缀的 CSS 属性时，如 transform，Vue.js 会自动侦测并添加相应的前缀。

    - 多重值

        从 2.3.0 起你可以为 style 绑定中的属性提供一个包含多个值的数组，常用于提供多个带前缀的值，例如：

        `<div :style="{ display: ['-webkit-box', '-ms-flexbox', 'flex'] }"></div>`
        这样写只会渲染数组中最后一个被浏览器支持的值。在本例中，如果浏览器支持不带浏览器前缀的 flexbox，那么就只会渲染 display: flex。

## 双向数据绑定-MVVM

MVVM：M-model，V-view

model改变会影响view，view反过来影响model

双向数据绑定（v-model）必须在表单（`<input>`、`<textarea>` 及 `<select>`等表单元素）中使用

v-model 在内部使用不同的属性为不同的输入元素并抛出不同的事件：

- text 和 textarea 元素使用 value 属性和 input 事件；
- checkbox 和 radio 使用 checked 属性和 change 事件；
- select 字段将 value 作为 prop 并将 change 作为事件。

## 通过ref获取DOM节点

`<input type='text' ref='userinfo'>`

```
methods:{
    getInputValue(){
        //  获取ref定义的DOM节点
        console.log(this.$refs.userinfo);
        console.log(this.$refs.userinfo.value);// DOM属性
    }
}
```

## Vue事件

- v-on:click='getInputValue()'
- @click='getInputValue()'
- 事件对象：@click='eventFn($event)' data-aid='aaa'

    ```
    methods:{
        eventFn(e){
            console.log(e);
            console.log(e.srcElement.dateset);
        }
    }
    ```


## 封装storage
```
// storage.js
//封装操作localstorage本地存储的方法   模块化的文件
// nodejs  基础

var storage={
    set(key,value){
        localStorage.setItem(key, JSON.stringify(value));
    },
    get(key){
        return JSON.parse(localStorage.getItem(key));
    },remove(key){
        localStorage.removeItem(key);
    }
}
export default storage;

```

import storage from 'storage.js'

## Vue组件

组件是可复用的 Vue 实例，且带有一个名字

一个组件的 data 选项必须是一个函数，因此每个实例可以维护一份被返回对象的独立的拷贝

通常一个应用会以一棵嵌套的组件树的形式来组织

全局注册和局部注册

```
// 定义一个名为 button-counter 的新组件
Vue.component('button-counter', {
  data: function () {
    return {
      count: 0
    }
  },
  template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
})
```

```
<div id="components-demo">
  <button-counter></button-counter>
</div>
```

1. 引入组件

    import Button from 'button-counter.vue'
2. 挂载组件

    components:{
        'v-button-counter':Button
    }

3. 在模板中使用
   
    `<v-button-counter></v-button-counter>`


## 生命周期函数（生命周期钩子函数）

组件挂载、组件更新、组件销毁的时候触发的一系列方法，这些方法就叫做生命周期函数。

```
beforeCreate(){   
},
created(){   
},
beforeMount(){   
},
mounted(){   
},
beforeUpdate(){   
},
updated(){   
},
beforeDestroy(){   
},
destroyed(){   
}
```


## 请求数据
#### 请求数据的模板
- vue-resource 官方提供的vue插件
  - 需要安装vue-resource模块，  注意加上  --save

    `npm install vue-resource --save /  cnpm install vue-resource --save`

  - main.js引入 vue-resource

    `import VueResource from 'vue-resource';`

  - main.js  
    `Vue.use(VueResource);`


  - 在组件里面直接使用
    ```
        this.$http.get(地址).then(function(){
        })
    ```
- axios
  - 安装  cnpm  install  axios --save
  - 哪里用哪里引入axios
    ```
    Axios.get(api).then((response)=>{
        this.list=response.data.result;
    }).catch((error)=>{
        console.log(error);

    })
    ```
- fetch-jsonp


## 组件间传值
### 父子组件传值
- 父组件给子组件传值
  - 父组件调用子组件的时候 绑定动态属性

    `<v-header :title="title"></v-header>`
  - 在子组件里面通过 props接收父组件传过来的数据

    props:['title']

    props:{
        'title':String      
    }

  - 直接在子组件里面使用

- 父组件主动获取子组件的数据和方法：
  - 调用子组件的时候定义一个ref

       `<v-header ref="header"></v-header>`
  - 在父组件里面通过
    ```
    this.$refs.header.属性
    this.$refs.header.方法
    ```

- 子组件主动获取父组件的数据和方法：  

    ```
    this.$parent.数据
    this.$parent.方法
    ```

### 非父子组件间传值
- 新建一个js文件   然后引入vue  实例化vue  最后暴露这个实例
    VueEvent.js
    
    ```
    import Vue from 'vue';

    var VueEvent = new Vue();
    
    export default VueEvent;
    ```
- 在要广播的地方引入刚才定义的实例
    ```
    import VueEvent from '../model/VueEvent.js';

    ```
- 通过 VueEvent.$emit('名称','数据')

    ```
        methods:{
            emitHome(){ 

                //广播

                VueEvent.$emit('to-home',this.msg)
            }

        }
    ```

- 在接收收数据的地方通过 $on接收广播的数据
    ```
        mounted(){

            VueEvent.$on('to-news',function(data){
                console.log(data);
            })
        }
    ```


## Vue路由

- vue 路由配置
  - 安装

    npm install vue-router  --save   / cnpm install vue-router  --save
  - 引入并Vue.use(VueRouter)   (main.js)
    ```
		import VueRouter from 'vue-router'

		Vue.use(VueRouter)
    ```
  - 配置路由
    - 创建组件，引入组件

    ```
        import Home from './components/Home.vue';
        import News from './components/News.vue';

    ```
    - 配置路由   注意：名字
    ```
    const routes = [
        { path: '/home', component: Home },
        { path: '/news', component: News },

        { path: '/content/:aid', component: Content },   /*动态路由*/

        { path: '*', redirect: '/home' }   /*默认跳转路由*/
    ]
    ```

    - 实例化VueRouter  注意：名字
    ```
    const router = new VueRouter({
        routes // （缩写）相当于 routes: routes
    })

    ```


    - 挂载路由
    ```
    new Vue({
        el: '#app',
        router,
        render: h => h(App)
    })
    ```
    - 在根组件的模板里使用路由

        `<router-view></router-view> 放在 App.vue`

    - 路由跳转

	    `<router-link to="/foo">Go to Foo</router-link>`

- vue 动态路由，get传值
  - 不同路由传值：动态路由
    - 配置路由
      
      `{ path: '/content/:aid', component: Content },   /*动态路由*/`

    - 在对应页面，获取动态路由传值

      ```
          mounted(){
              console.log(this.$route.params);  /*获取动态路由传值*/

          }
      ```

    - 
  - get传值

    `<router-link to="/pcontent?aid=123">Go to Foo</router-link>`
    ```
    mounted(){
        //获取get传值
        console.log(this.$route.query);
    }
    ```

- 路由结合请求数据

    ```
        mounted(){

               // console.log(this.$route.params);  /*获取动态路由传值*/

                var aid=this.$route.params.aid;

                //调用请求数据的方法

                this.requestData(aid);

        },
        methods:{

            requestData(aid){

                //get请求如果跨域的话 后台php java 里面要允许跨域请求

                var api='http://www.phonegap100.com/appapi.php?a=getPortalArticle&aid='+aid;


                this.$http.get(api).then((response)=>{
                        console.log(response);

                        this.list=response.body.result[0];

                },(err)=>{

                    console.log(err)
                })
            }
        }
    ```

- 路由编程式导航

  - 第一种跳转方式
    ```
        // this.$router.push({ path: 'news' })
        // this.$router.push({ path: '/content/495' });
    ```

  - 另一种跳转方式
    ```
        //{ path: '/news', component: News,name:'news' },
        // router.push({ name: 'news', params: { userId: 123 }})
        this.$router.push({ name: 'news'})
    ```

- hash模式路由

    ```
        const router = new VueRouter({
            mode: 'history',   /*hash模式改为history*/
            routes // （缩写）相当于 routes: routes
        })
    ```
- 路由的嵌套
  - 配置路由
   ```
   {
      path: '/user',

      component: User,
      children:[
        { path: 'useradd', component: UserAdd },
        { path: 'userlist', component: Userlist }
      ]
    }
    ```
  - 父路由里面配置子路由显示的地方   `<router-view></router-view>`

- 路由模块化

    `router.js`

    ```
    import Vue from 'vue';

    //配置路由
    import VueRouter from 'vue-router';
    Vue.use(VueRouter);

    //1.创建组件
    import Home from '../components/Home.vue';

    //2.配置路由   注意：名字

    const routes = [
        { path: '/home', component: Home },
        { path: '*', redirect: '/home' }   /*默认跳转路由*/
    ]

    //3.实例化VueRouter  注意：名字

    const router = new VueRouter({
        mode: 'history',   /*hash模式改为history*/
        routes // （缩写）相当于 routes: routes
    })

    //5 <router-view></router-view> 放在 App.vue

    export default router;

    ```

