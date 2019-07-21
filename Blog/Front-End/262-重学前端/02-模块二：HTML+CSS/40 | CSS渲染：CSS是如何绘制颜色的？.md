# [40 | CSS渲染：CSS是如何绘制颜色的？](https://time.geekbang.org/column/article/92663?utm_source=time_web&utm_medium=menu)

## 颜色的原理

color
background-color

### RGB 颜色

RGB颜色，**符合光谱三原色理论：红、绿、蓝三种颜色的光可以构成所有的颜色。**

![三原色](https://static001.geekbang.org/resource/image/7f/a1/7f5bf39cbe44e36758683a674f9fcfa1.png)

### CMYK 颜色

在印刷行业，使用的是这样的三原色（品红、黄、青）来调配油墨，这种颜色的表示法叫做CMYK，用一个四元组来表示颜色。

颜料三原色（红、绿、蓝的补色）：品红、黄、青。

![品红、黄、青](https://static001.geekbang.org/resource/image/15/1b/15fefe9f80ec8e1f7bd9ecd223feb61b.png)


### HSL 颜色

HSL 这样的颜色模型被设计出来了，它用一个值来表示人类认知中的颜色，我们用专业的术语叫做色相（H）。加上颜色的纯度（S）和明度（L），构成一种颜色表示。

![HSL颜色](https://static001.geekbang.org/resource/image/a3/ce/a3016a6ff178870d6dba23f807b0dfce.png)

### 其它颜色

RGBA：Red（红色）、Green（绿色）、Blue（蓝色）和Alpha的色彩空间。

## 渐变

background-image，可以设为渐变。

CSS 中，支持两种渐变：
- **线性渐变**
  
```
linear-gradient(direction, color-stop1, color-stop2, ...);
```

  direction 可以是方向，也可以是具体的角度：
  - to bottom
  - to top
  - to left
  - to right
  - to bottom left
  - to bottom right
  - to top left
  - to top right
  - 120deg
  - 3.14rad

  color-stop 是一个颜色和一个区段：
  - rgba(255,0,0,0)
  - orange
  - yellow 10%
  - green 20%
  - lime 28px

  金色背景：
  ```
  <style>
    #grad1 {
        height: 200px;
        background: linear-gradient(45deg, gold 10%, yellow 50%, gold 90%); 
    }
  </style>
  <div id="grad1"></div>
  ```

- **放射性渐变**

```
radial-gradient(shape size at position, start-color, ..., last-color);
```

  当我们应用的每一种颜色都是HSL颜色时，就产生来一些非常有趣的效果。比如，我们可以通过变量来调整一个按钮的风格：

```
<style>
.button {
    display: inline-block;
    outline: none;
    cursor: pointer;
    text-align: center;
    text-decoration: none;
    font: 14px/100% Arial, Helvetica, sans-serif;
    padding: .5em 2em .55em;
    text-shadow: 0 1px 1px rgba(0,0,0,.3);
    border-radius: .5em;
    box-shadow: 0 1px 2px rgba(0,0,0,.2);
    color: white;
    border: solid 1px ;
}

</style>
<div class="button orange">123</div>
```

```
var btn = document.querySelector(".button");
var h = 25;
setInterval(function(){
  h ++;
  h = h % 360;
  btn.style.borderColor=`hsl(${h}, 95%, 45%)`
  btn.style.background=`linear-gradient(to bottom,  hsl(${h},95%,54.1%),  hsl(${h},95%,84.1%))`
},100);
```

## 形状

- border
- box-shadow
- border-radius

> 这些形状的属性非常有趣，我们也能看到很多利用他们来产生的CSS黑魔法。
> 然而，这边建议，仅仅把他们用于基本用途，即：border用于边框、阴影用于阴影、圆角用于圆角。
> **所有其它的场景，都有一个更好的替代品：datauri+svg。**

