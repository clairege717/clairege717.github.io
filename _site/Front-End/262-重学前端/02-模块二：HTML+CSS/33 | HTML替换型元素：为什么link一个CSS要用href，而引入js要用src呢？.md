# [33 | HTML替换型元素：为什么link一个CSS要用href，而引入js要用src呢？](https://time.geekbang.org/column/article/89491?utm_source=time_web&utm_medium=menu)

引入文件的方案：
- 链接
  - link
  - a
  - area
  
- 替换型元素
  
  把文件的内容引入，替换掉自身位置的一类标签

  - script
  - img
  - picture
  - audio
  - video
  - iframe

### script 标签

script 标签既可作为替换型标签，又可不作为替换型标签的元素。

```

// 1. 直接把脚本代码写在script标签之间
<script type="text/javascript">
console.log("Hello world!");
</script>

// 2. 把代码放到独立的js文件中，用src属性引入
<script type="text/javascript" src="my.js"></script>

```

**凡事替换型元素，都是使用src属性来引用文件的。链接型元素是使用href标签。**

### img 标签

引入一张图片。有src属性才有意义。

如果不想引入独立文件，可以使用data uri：
```
 <img src='data:image/svg+xml;charset=utf8,<svg version="1.1" xmlns="http://www.w3.org/2000/svg"><rect width="300" height="100" style="fill:rgb(0,0,255);stroke-width:1;stroke:rgb(0,0,0)"/></svg>'/>
```

img 标签可以使用width和height指定宽高。只指定宽度，图片被**等比例缩放**，适用于既要限制图片尺寸，又要保持图片比例的场景。

```
 <img src='data:image/svg+xml;charset=utf8,<svg width="600" height="400" version="1.1"
xmlns="http://www.w3.org/2000/svg"><ellipse cx="300" cy="150" rx="200" ry="80"
style="fill:rgb(200,100,50);
stroke:rgb(0,0,100);stroke-width:2"/></svg>' width="100"/>
```

**如果从性能的角度考虑，建议同时给出图片的宽高，因为替换型元素加载完成后，如果尺寸发生变换，会触发重排版。**

alt属性！对于视障用户非常重要。可以说，给img加上alt属性，已经做完来可访问性的一半。

srcset和sizes，是src属性的升级版。这两个属性的作用是在不同的屏幕大小和特性下，使用不同的图片源。

```
<img srcset="elva-fairy-320w.jpg 320w,
             elva-fairy-480w.jpg 480w,
             elva-fairy-800w.jpg 800w"
     sizes="(max-width: 320px) 280px,
            (max-width: 480px) 440px,
            800px"
     src="elva-fairy-800w.jpg" alt="Elva dressed as a fairy">
```

### picture 

picture元素可以根据屏幕的条件为其中的img元素提供不同的源，基本用法如下：

```
<picture>
  <source srcset="image-wide.png" media="(min-width: 600px)">
  <img src="image-narrow.png">
</picture>
```

使用source元素来指定图片源，并且支持多个。media属性是media query，跟CSS的@media规则一致。

### video

可以使用source标签来指定接入多个视频源。

```
<video controls="controls" >
  <source src="movie.webm" type="video/webm" >
  <source src="movie.ogg" type="video/ogg" >
  <source src="movie.mp4" type="video/mp4">
  You browser does not support video.
</video>
```

video 标签的内容默认会被当做不支持video的浏览器显示的内容，因此，如果要支持更古老的浏览器，还可以在其中加入object或者embed标签。

video 中还支持一种标签：track。

track是一种播放时序相关的标签，它最常见的用途就是字幕。

track标签中，必须使用srclang来指定语言。

track具有kind属性：
- subtitles：字幕
- captions：报幕内容
- descriptions：视频描述内容，适合视障人士或者没有视频播放功能的终端打开视频时了解视频内容
- chapters：用于浏览器视频内容
- metadata：给代码提供的元信息

### audio

```
<audio controls>
  <source src="song.mp3" type="audio/mpeg">
  <source src="song.ogg" type="audio/ogg">
  <p>You browser does not support audio.</p>
</audio>
```

### iframe

能够嵌入一个完整的网页

在移动端，无法指定大小，内容会被完全平铺到父级页面

很多网页也会通过http协议头禁止自己被放入iframe中。

在新标准中，为iframe加入来sandbox模式和srcdoc属性，这样，给iframe带来了一定的新场景。

```
<iframe sandbox srcdoc="<p>Yeah, you can see it <a href="/gallery?mode=cover&amp;amp;page=1">in my gallery</a>."></iframe>
```

这个例子，使用srcdoc属性创建来一个新的文档，嵌入在iframe中展示，并且使用来sandbox来隔离。这样，这个iframe就不涉及任何跨域问题来。



