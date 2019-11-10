# [20 | CSS 选择器：如何选中svg里的a元素？](https://time.geekbang.org/column/article/84365?utm_source=time_web&utm_medium=menu)

选择器是由CSS最先引入的一个机制（但随着document.querySelector等API的加入，选择器已经不仅仅是CSS的一部分了）。

选择器的基本意义是：**根据一些特征，选中元素树上的一批元素**。

选择器的结构，由简单到复杂可以分为以下几类：
- 简单选择器：针对某一特征判断是否为选中元素
- 复合选择器：连续写在一起的简单选择器，针对元素自身特征选择单个元素
- 复杂选择器：有“（空格）”“>”“~”“+”等符号连接的复合选择器，根据父元素或者前序元素检查单个元素
- 选择器列表：由逗号分隔的复杂选择器，表示“或”的关系

## 简单选择器

![针对某一特征判断是否为选中元素](https://static001.geekbang.org/resource/image/4c/ce/4c9ac78870342dc802137ea9c848c0ce.png)

- ### 类型选择器
  
  根据一个元素的标签名来选中元素

  html和xml元素的命名空间。

  svg和html中都有a元素，若要区分，必须使用带命名空间的类型选择器。

```
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>JS Bin</title>
</head>
<body>
<svg width="100" height="28" viewBox="0 0 100 28" version="1.1"
     xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <desc>Example link01 - a link on an ellipse
  </desc>
  <a xlink:href="http://www.w3.org">
    <text y="100%">name</text>
  </a>
</svg>
<br/>
<a href="javascript:void 0;">name</a>
</body>
</html>

@namespace svg url(http://www.w3.org/2000/svg);
@namespace html url(http://www.w3.org/1999/xhtml);
svg|a {
  stroke:blue;
  stroke-width:1;
}

html|a {
  font-size:40px
}
```

- ### 全体选择器
  
  “*”：可以选中任意元素。用法跟类型选择器完全一致

- ### id选择器
  
  针对特定属性的选择器，“#”后面跟随id名

- ### class选择器
  
  针对特定属性的选择器，“.”后面跟随class名

```
#myid {
  stroke:blue;
  stroke-width:1;
}

.mycls {
  font-size:40px
}
```

- ### 属性选择器
  - [att]
  
  检查元素是否具有这个属性，只要元素有，不论是什么值，都可以被选中

  - [att=val]
  
  精确匹配，检查一个元素属性的值是否是val

  - [att~=val]
  
  多种匹配，检查一个元素的值是否是若干值之一，这里的val不是一个单一的值来，可以是用空格分隔的一个序列

  - [att|=val]
  
  开头匹配，检查一个元素的值是否是以val开头，它跟精确匹配的区别是属性只要以val开头即可。

  有些HTML属性含有特殊字符，可以把val用引号括起来，形成CSS字符串。

  CSS字符串允许使用单引号来规避特殊字符，也可以用反斜杠转义。
  
- ### 伪类选择器
  - 树结构关系伪类选择器
    - :root类表示树的根元素
    - :empty
    - :nth-child 和 :nth-last-child
    - :first-child :last-child
    - :only-child
  
  - 链接与行为伪类选择器
    - :any-link 
    - :link
    - :visited
    - :hover
    - :active
    - :focus
    - :target
  
  - 逻辑伪类选择器
    - :not
  
  - 其他伪类选择器
    - 国际化：用于处理国际化和多语言问题
      - dir
      - lang
    - 音频/视频：用于区分音视频播放状态
      - play
      - pause
    - 时序：用于配合读屏软件等时序性客户端的伪类
      - current
      - past
      - future
    - 表格：用于处理table的列的伪类
      - nth-child
      - nth-last-col


