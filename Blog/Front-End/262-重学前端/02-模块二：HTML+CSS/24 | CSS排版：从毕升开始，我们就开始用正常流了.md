# [24 | CSS排版：从毕升开始，我们就开始用正常流了](https://time.geekbang.org/column/article/85745?utm_source=time_web&utm_medium=menu)

  **一句话描述正常流的排版行为：依次排列，排不下了换行。也是理解它最简单最源头的方式。**

## 正常流的行为

  **一句话描述正常流的排版行为：依次排列，排不下了换行。也是理解它最简单最源头的方式。**

  在正常流基础上，我们有float相关规则，使得一些盒占据来正常流需要的空间，我们可以把float理解为“**文字环绕**”

  我们还有vertical-align相关规则规定来如何在垂直方向对齐盒。vertical-align相关规则看起来复杂，但是实际上，基线、文字顶/底、行顶/顶部都是我们正常书写文字时需要用到的概念。

  下图展示来在不同的vertical-align设置时，盒与文字是如何混合排版的。为了方便理解，标注来基线、文字顶/底、行顶/底等概念。

  ![vertical-align](https://static001.geekbang.org/resource/image/aa/e3/aa6611b00f71f606493f165294410ee3.png)

  margin折叠。把margin理解为“**一个元素规定来自身周围至少需要的空间**”。
  

## 正常流的原理

  在CSS标准中，规定了如何排布每一个文字或者盒的算法，这个算法依赖一个排版的“当前状态”，CSS把这个当前状态称为“格式化上下文（formatting context）”。

  排版过程可以认为是这样的：

  > 格式化上下文 + 盒 / 文字 = 位置

  > formatting context + boxes/character = positions

  我们需要排版的盒，分为块级盒和行内盒，所以排版需要分别为她们规定了块级格式化上下文和行内级格式化上下文。

  当我们要把正常流中的一个盒或者文字排版，需要分为三种情况处理：
  - **当遇到块级盒**：排入块级格式化上下文
  - **当遇到行内级盒或者文字**：首先尝试排入行内级格式化上下文，如果排不下，那么创建一个行盒，先将行盒排版（行盒是块级，所以到第一种情况），行盒会创建一个行内级格式化上下文。
  - **遇到float**：把盒的顶部跟当前行内级上下文上边缘对齐，然后根据float的方向把盒的对应边缘对到块级格式化上下文的边缘，之后重排当前行盒。

  以上，讲的都是一个块级格式化上下文的排版规则，实际上，页面中的布局，一些元素会在其内部创建新的块级格式化上下文，这些元素有：
  1. 浮动元素
  2. 绝对定位元素
  3. 非块级但仍能包含块级元素的容器（如inline-blocks，table-cells，table-captions）
  4. 块级的能包含块级元素的容器，且属性overflow不为visible

  最后一条比较绕，可以换个思路：

  自身为块级，且overflow为visible的块级元素容器，它的块级格式化上下文盒外部的块级格式化上下文发生了融合，也就是说，如果不考虑盒模型相关的属性，这样的元素从排版的角度就好像根本不存在。

## 正常流的使用技巧

### 等分布局问题

```
<div class="outer">
    <div class="inner"></div>
    <div class="inner"></div>
    <div class="inner"></div>
</div>

.outer {
    width:101px;
    font-size:0;
}

.inner {
    width:33.33%;
    height:300px;
    display:inline-block;
    outline:solid 1px blue;
    font-size:30px;
}

.inner:last-child {
    margin-right:-5px;
}
```

> 使用百分比解决横向等分布局
> 因为“inline-block”属性，div间有空白，可修改outer的font-size为0
> 在某些浏览器中，因为像素计算精度的问题，会出现换行，给outer添加一个特定宽度
> 在某些旧版本浏览器中，会出现换行。为了保险起见，我们给最后一个div加上一个负的右margin值
> 

### 自适应宽

```
<div class="outer">
    <div class="fixed"></div>
    <div class="auto"></div>
</div>

.fixed {
    width:200px;
    display:inline-block;
    vertical-align:top;
}
.fixed, .auto {
    height:300px;
    outline:solid 1px blue;
}
.auto {
    margin-left:-200px;
    padding-left:200px;
    box-sizing:border-box;
    width:100%;
    display:inline-block;
    vertical-align:top;
}
```

> fixed的宽度已经被指定好。用正常流解决这个问题的思路是：利用负margin
> 只使用负margin，会导致auto中的内容位置不对，因此还要使用padding将内容挤出来。即：添加padding-left和box-sizing
