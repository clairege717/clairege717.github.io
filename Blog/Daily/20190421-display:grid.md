# 20190421 小记

部分摘录引用自：
- [写给自己看的display: grid布局教程-张鑫旭](https://www.zhangxinxu.com/wordpress/2018/11/display-grid-css-css3/)

## CSS display:grid

display:grid网格布局

### 背景

&emsp;&emsp;实现一个真正的网格布局。以前一直用的float，后来会了flex就放弃float了。今天这个，还是grid更适合，所以，又复习了一遍。

```
div {
    display: grid;
}
```

&emsp;&emsp;此时该div就是“grid容器”，其子元素称为“grid子项”。

&emsp;&emsp;在Grid布局中，所有相关CSS属性正好分为两拨，一拨作用在grid容器上，还有一拨作用在grid子项上。

### 作用在grid容器上的CSS属性

- grid-template-columns和grid-template-rows
- grid-template-areas
- grid-template
- grid-column-gap和grid-row-gap
- grid-gap
- justify-items
- align-items
- place-items
- justify-content
- align-content
- place-content
- grid-auto-columns和grid-auto-rows
- grid-auto-flow
- grid

### 作用在grid子项上的CSS属性

- grid-column-start, grid-column-end, grid-row-start和grid-row-end
- grid-column和grid-row
- grid-area
- justify-self
- align-self
- place-self

### 其他Grid注意点

- 在Grid布局中，float，display:inline-block，display:table-cell，vertical-align以及column-*这些属性和声明对grid子项是没有任何作用的。
- Grid布局则适用于更大规模的布局（二维布局），而Flexbox布局最适合应用程序的组件和小规模布局（一维布局）
- 命名虽然支持中文，但由于CSS文件中文存在乱码的风险，所以……
- IE10-IE15虽然名义上支持Grid布局，但支持的是老版本语法（本文是介绍的全是2.0全新语法），还需要加-ms-私有前缀。。。具体IE下的使用，待研究


实际代码示例

```

<style scoped>
.label-list {
  max-width: 300px;
  margin-top: 20px;
  display: grid;
  grid-gap: 0;
  grid-template-columns: repeat(auto-fit, minmax(75px, 1fr));
  border-left: 1px solid #e9e9e9;
  border-top: 1px solid #e9e9e9;
}
.col-4 {
  grid-template-columns: repeat(4, 1fr);
}
.col-3 {
  grid-template-columns: repeat(3, 1fr);
}
.label-item {
  text-align: center;
  padding-top: 8px;
  padding-bottom: 8px;
  position: relative;
  cursor: pointer;
  border-right: 1px solid #e9e9e9;
  border-bottom: 1px solid #e9e9e9;
  user-select: none;
  -moz-user-select: none;
}
.label-item.l-hover,
.label-item:hover {
  background-color: #efefef;
}
</style>

```



