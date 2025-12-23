# [41 | CSS小实验：动手做，用代码挖掘CSS属性](https://time.geekbang.org/column/article/93110?utm_source=time_web&utm_medium=menu)

## 浏览器中已经实现的属性

```
Object.keys(document.body.style).filter(e => !e.match(/^webkit/))
```

枚举document.body.style 上的所有属性，并且去掉webkit 前缀的私有属性。

W3C 是TR 页面：
[https://www.w3.org/TR/?tag=css](https://www.w3.org/TR/?tag=css)



