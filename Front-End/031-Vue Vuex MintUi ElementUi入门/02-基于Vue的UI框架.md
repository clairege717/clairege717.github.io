# 基于Vue的UI框架

饿了么公司基于vue开的的vue的Ui组件库
- [Element Ui](http://element.eleme.io/)    基于vue  pc端的UI框架  
- [MintUi](http://mint-ui.github.io/#!/en) 基于vue  移动端的ui框架

## Mint UI
- Mint UI的使用
  1. 找官网

  2. 安装   npm install mint-ui -S         -S表示  --save

  3. 引入mint Ui的css 和 插件
      ```
      import Mint from 'mint-ui';

      Vue.use(Mint);

      import 'mint-ui/lib/style.css'
      ```

  4. 看文档直接使用。

  > **在mintUi组件上面执行事件的写法**
  > 
  > @click.native
  > 
  > `<mt-button @click.native="sheetVisible = true" size="large">点击上拉 action sheet</mt-button>`



## Element
- Element UI的使用

  1. 安装
   
        cnpm install babel-plugin-component -D    


  2. 找到.babelrc 配置文件
		把
        ```
		{
		  "presets": [
		    ["env", { "modules": false }],
		    "stage-3"
		  ]
		}

        ```
		改为  注意：
		```
		{
		  "presets": [["env", { "modules": false }]],
		  "plugins": [
		    [
		      "component",
		      {
			"libraryName": "element-ui",
			"styleLibraryName": "theme-chalk"
		      }
		    ]
		  ]
		}
        ```
  3. 
	import { Button, Select } from 'element-ui';

	Vue.use(Button)
	Vue.use(Select)


- Element UI组件的单独使用（第二种方法，按需引入）：
    ```
	import { Button, Select } from 'element-ui';

	Vue.use(Button)
	Vue.use(Select)
	```

	引入对应的css

		`import 'element-ui/lib/theme-chalk/index.css';`

	如果报错： webpack.config.js  配置file_loader
    ```
		{
			test: /\.(eot|svg|ttf|woff|woff2)(\?\S*)?$/,
			loader: 'file-loader'
	    }

    ```



