# 20200517-ontouchstart

body中添加ontouchstart:`<body ontouchstart="">`，active兼容处理 即伪类:active失效

方法一：body添加ontouchstart:`<body ontouchstart="">`

方法二：js给 document 绑定 touchstart 或 touchend 事件
```
<style>
   a {
     color:#000;
   }
   a:active {
      color:#fff;
    }
    </style>
    <a herf=foo >bar</a>
 <script>
    document.addEventListener('touchstart',function(){},false);
</script>
```