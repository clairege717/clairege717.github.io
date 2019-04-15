# Angular基础内容相关

- 模块(ngModule)
- 组件
  - 模板与视图
  - 组件元数据
  - 数据绑定
  - 指令
  - 管道
- 服务与依赖注入(DI)
  - 路由


## app.module.ts

    ```

    /*这个文件是Angular 根模块，告诉Angular如何组装应用*/
    app.module.ts

    //BrowserModule，浏览器解析的模块
    import { BrowserModule } from '@angular/platform-browser';  
    //Angular核心模块
    import { NgModule } from '@angular/core';
    //根组件
    import { AppComponent } from './app.component';
    import { NewsComponent } from './components/news/news.component';
    import { HomeComponent } from './components/home/home.component';
    import { HeaderComponent } from './components/header/header.component';

    /*@NgModule装饰器, @NgModule接受一个元数据对象，告诉 Angular 如何编译和启动应用*/
    @NgModule({
    declarations: [    
        /*配置当前项目运行的的组件*/
        AppComponent, NewsComponent, HomeComponent, HeaderComponent
    ],
    imports: [  
        /*配置当前模块运行依赖的其他模块*/
        BrowserModule
    ],
    providers: [
        /*配置项目所需要的服务*/
    ],  
    bootstrap: [
        AppComponent
    ]    
    })

    //根模块不需要导出任何东西，   因为其它组件不需要导入根模块
    export class AppModule { }


    ```



## Angular目录结构分析

- node_modules

    提供给整个工作区的 npm 包。
    
- .editorconfig

    代码编辑器配置
    
- .gitignore

    指定Git要忽略的非跟踪文件
    
- angular.json

    工作区中所有项目的默认 CLI 配置，包括 CLI 使用的构建选项、运行选项、测试工具选项（比如 TSLint、Karma、Protractor）等。
    
- package.json

    配置用于工作区中所有项目的包依赖项。
    
- package-lock.json

    为 npm 客户端安装到 node_modules 中的所有软件包提供版本信息。
    
- README.md
- tsconfig.json

    工作区中所有应用的默认 TypeScript 配置。包括 TypeScript 选项和 Angular 模板编译器选项。
    
- tslint.json

    工作区中所有应用的默认 TSLint 配置。

- e2e

  子目录包含一组初始应用所对应的端到端测试的配置文件和源文件。

  - src
    - app.e2e-spec.ts
    - app.po.ts
  - protractor.conf.js
  - tsconfig.e2e.json
  
- src

    子目录包含该初始应用的源文件（应用逻辑、数据和资源）以及配置文件。
    
  - app

    包含组件文件，其中定义了应用逻辑和数据。

    - app-routing.module.ts
    - app.component.css
    - app.component.html
    - app.component.spec.ts
    - app.component.ts
    - app.module.ts

  - assets

    包含图像文件和其它文件，当构建应用时会被原样复制到构建目标中。
    
  - environments

    包含针对特定目标环境的配置选项。默认情况下有一个未命名的标准开发环境和一个名叫 "prod" 的产品环境。你可以定义一些额外的目标环境配置。
    
  - browserslist

    配置各个目标浏览器和 Node.js 版本之间的市场占有率，供各种前端工具使用。

  - favicon.ico

    一个用在书签栏上的应用图标。

  - index.html

    当有人访问你的应用时给出的主 HTML 文件，你通常不用手动在这里添加任何 \<script> 或\<link> 标签。

  - karma.conf.js
  - main.ts

    应用的主入口点。使用 JIT 编译器编译应用，并引导应用的根模块 AppModule 来运行在浏览器中。你也可以为 CLI 的 build 和 serve 命令添加 --aot 标志，来使用 AOT 编译器 而不必修改任何代码。

  - polyfills.ts

    为浏览器支持提供腻子脚本（polyfill）。

  - styles.css

    列出为项目提供样式的 CSS 文件。其扩展名和你为项目配置的样式预处理器保持一致。

  - test.ts

    单元测试的主入口点，其中带有一些特定于 Angular 的配置。

  - tsconfig.app.json

    继承自工作区级的 tsconfig.json 文件。

  - tsconfig.spec.json

    继承自工作区级的 tsconfig.json 文件。
    
  - tslint.json

    继承自工作区级的 tsconfig.json 文件。


## Angular基本语法

- 创建组件

    ng g component componentName

- 绑定数据

    1. 数据文本绑定-{{}}

    ```
    <h1>
        {{title}}
    </h1>
    <div>
        1+1={{1+1}}
    </div>
    ```
    1. 绑定html-[innerHTML]
    
    ```
    .component.ts:
    this.h="<h2>这是一个 h2 用[innerHTML]来解析</h2>"
    
    .component.html:
    <div [innerHTML]="h"></div>
    ```

- 绑定属性

    ```
    <div [id]="id" [title]="title"></div>
    ```
- 数据循环 *ngFor

    1、*ngFor 普通循环
    ```
    <ul>
        <li *ngFor="let item of list">
            {{item}}
        </li> 
    </ul>
    ```
    2、循环的时候设置 key
    ```
    <ul>
        <li *ngFor="let item of list;let i = index;">
            {{item}} --{{i}}
        </li> 
    </ul>
    ```
    1. template 循环数据
    ```
    <ul>
        <li template="ngFor let item of list">
            {{item}}
        </li> 
    </ul>
    ```

- 条件判断 *ngIf

    ```
    <p *ngIf="list.length > 3">这是 ngIF 判断是否显示</p>
    
    <p template="ngIf list.length > 3">这是 ngIF 判断是否显示</p>
    ```
- *ngSwitch

    ```
    <ul [ngSwitch]="score">
        <li *ngSwitchCase="1">已支付</li>
        <li *ngSwitchCase="2">订单已经确认</li> <li *ngSwitchCase="3">已发货</li>
        <li *ngSwitchDefault>无效</li>
    </ul>
    ```
- 执行事件 (click)="getData()"

    ```

    .component.html:
    <button class="button" (click)="getData()"> 点击按钮触发事件 </button>
    <button class="button" (click)="setData()"> 点击按钮设置数据 </button>
    
    .component.ts:
    getData(){ 
        /*自定义方法获取数据*/
        alert(this.msg); //获取
    } 
    setData(){
        //设置值
        this.msg='这是设置的值'; 
    }

    ```  
    
- [ngClass]、[ngStyle]
  - [ngClass]

    ```

    <div [ngClass]="{'red': true, 'blue': false}"> 这是一个 div </div>

    public flag=false;

    <div [ngClass]="{'red': flag, 'blue': !flag}"> 这是一个 div </div>

    public arr = [1, 3, 4, 5, 6];
    <ul>
        <li *ngFor="let item of arr, let i = index"> 
            <span [ngClass]="{'red': i==0}">{{item}}</span> 
        </li> 
    </ul>

    ```

  - [ngStyle]

    ```

    <div [ngStyle]="{'background-color':'green'}">你好 ngStyle</div>

    .component.ts:
    public attr='red';

    .component.html:
    <div [ngStyle]="{'background-color':attr}">你好 ngStyle</div>

    ```

- 管道

    ```
    .component.ts:
    public today=new Date();

    .component.html:
    <p>{{today | date:'yyyy-MM-dd HH:mm:ss' }}</p>
    ```

- 表单事件-事件对象

    keyup、keydown

    ```

    .component.html:
    <input type="text" (keyup)="keyUpFn($event)"/>

    .component.ts:
    keyUpFn(e){
        console.log(e)
    }
    ```

- 双向数据绑定-MVVM，只是针对表单

    model改变影响view，view改变影响model

    > 注意引入:FormsModule
    ```

    app.module.ts:
    import { FormsModule } from '@angular/forms'; 

    @NgModule({
        declarations: [
            AppComponent,
            HeaderComponent,
            FooterComponent,
            NewsComponent
        ], imports: [
            BrowserModule,
        FormsModule
        ],
        providers: [],
        bootstrap: [AppComponent]
    })
    export class AppModule { }

    .component.html:
    <input type="text" [(ngModel)]="inputValue"/> 
    {{inputValue}}
    
    ```
  
## Angular服务

&emsp;&emsp;服务是一个广义的概念，它包括应用所需的任何值、函数或特性。狭义的服务是一个明确定义了用途的类。它应该做一些具体的事，并做好。

&emsp;&emsp;组件应该把诸如从服务器获取数据、验证用户输入或直接往控制台中写日志等工作委托给各种服务。通过把各种处理任务定义到可注入的服务类中，你可以让它被任何组件使用。 通过在不同的环境中注入同一种服务的不同提供商，你还可以让你的应用更具适应性。

&emsp;&emsp;Angular 不会强迫你遵循这些原则。Angular 只会通过依赖注入来帮你更容易地将应用逻辑分解为服务，并让这些服务可用于各个组件中。

- 创建服务

    ng g service myService

- 在app.module.ts 里面引入创建的服务，并且声明
    ```
    import { StorageService } from './services/storage.service'

    providers: [StorageService]
    ```


- 在用到的组件里面引入服务，注册服务


    ```
    //引入服务
    import { StorageService } from '../../services/storage.service';

    //初始化
    constructor(private storage:StorageService) { 
        let s=this.storage.get();
        console.log(s);
    }

    addData(){
        // alert(this.username);
        this.list.push(this.username); 
        this.storage.set('todolist',this.list);
    }

    removerData(key){
        console.log(key); 
        this.list.splice(key,1); 
        this.storage.set('todolist',this.list);
    }
    ```



