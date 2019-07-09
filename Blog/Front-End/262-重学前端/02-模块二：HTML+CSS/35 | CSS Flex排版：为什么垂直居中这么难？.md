# [35 | CSS Flex排版：为什么垂直居中这么难？](https://time.geekbang.org/column/article/90148?utm_source=time_web&utm_medium=menu)

Flex 布局
- 设计
- 原理
- 应用
  
### Flex 的设计

### Flex 的原理

排版算法

主轴、交叉轴

Flex 排版的三个步骤：分行、计算主轴、计算交叉轴

### Flex 的应用

- 垂直居中

```
<div id="parent">
  <div id="child">
  </div>
</div>
```

```
#parent {
  display:flex;
  width:300px;
  height:300px;
  outline:solid 1px;
  justify-content:center;
  align-content:center;
  align-items:center;
}
#child {
  width:100px;
  height:100px;
  outline:solid 1px;
}
```

- 两列等高

```
<div class="parent">
  <div class="child" style="height:300px;">
  </div>
  <div class="child">
  </div>
</div>
<br/>
<div class="parent">
  <div class="child" >
  </div>
  <div class="child" style="height:300px;">
  </div>
</div>
```

```
.parent {
  display:flex;
  width:300px;
  justify-content:center;
  align-content:center;
  align-items:stretch;
}
.child {
  width:100px;
  outline:solid 1px;
}
```

- 自适应宽

```
<div class="parent">
  <div class="child1">
  </div>
  <div class="child2">
  </div>
</div>
```

```
.parent {
  display:flex;
  width:300px;
  height:200px;
  background-color:pink;
}
.child1 {
  width:100px;
  background-color:lightblue;
}
.child2 {
  width:100px;
  flex:1;
  outline:solid 1px;
}
```
