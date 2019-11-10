# [44 | HTML·ARIA：可访问性是只给盲人用的特性么](https://time.geekbang.org/column/article/93777?utm_source=time_web&utm_medium=menu)

ARIA：Accessible Rich Internet Applications，表现为一组属性，是用于可访问性的一份标准。

ARIA 的角色对于我们UI 系统的设计有重要的参考意义。

## 综述

ARIA 给HTML 元素添加的一个核心属性就是role：

```
<span role="checkbox" aria-checked="false" tabindex="0" aria-labelledby="chk1-label">
</span> <label id="chk1-label">Remember my preferences</label>
```

这里，我们给span添加了checkbox 角色，表示这个span 被用于checkbox。这意味着，我们可能已经用JS 代码绑定了这个span 的click事件，并且以checkbox 的交互方式来处理用户操作。

同时，ARIA 系统还提供来一系列ARIA 属性给checkbox 这个role。这意味着，我们可以通过HTML 属性变化来理解这个JavaScript 组件的状态，读屏软件等第三方客户端，就可以理解我们的UI 变化。这正是ARIA 标准的意义。





