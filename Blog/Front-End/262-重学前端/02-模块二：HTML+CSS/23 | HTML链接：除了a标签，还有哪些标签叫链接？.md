# [23 | HTML链接：除了a标签，还有哪些标签叫链接？](https://time.geekbang.org/column/article/85341?utm_source=time_web&utm_medium=menu)

链接是HTML中的一种机制，是HTML文档和其它文档或者资源的连接关系。

[在HTML中，链接有两种类型。一种是超链接型标签，一种外部资源链接](https://static001.geekbang.org/resource/image/ca/51/caab7832c425b3af2b3adae747e6f551.png)

链接
- link标签
  - 超链接类link标签
    - canonical型link
    - alternate型link
    - prev型link
    - next型link
    - 其它超链接型link
      - author型
      - help型
      - license型
      - search型
  - 外部资源类link标签
    - icon型link
    - 预处理类link
      - dns-prefetch型link
      - preconnect型link
      - prefetch型link
      - preload型link
      - prerender型link
    - modulepreload型link
    - stylesheet型link
    - pingback型link
- a标签
  - alternate型a标签
  - author型a标签
  - help型a标签
  - license型a标签
  - next型a标签
  - prev型a标签
  - search型a标签
  - tag型a标签
  - bookmark型a标签
  - nofollow型a标签
  - opener型a标签
- area标签
  - alternate型area标签
  - author型area标签
  - help型area标签
  - license型area标签
  - next型area标签
  - prev型area标签
  - search型area标签
  - tag型area标签
  - bookmark型area标签
  - nofollow型area标签
  - opener型area标签

## 一、link标签

  link标签也是元信息类标签的一种。

  link标签会生成一个链接，它可能生成超链接，也可能生成外部资源链接。

  一些link标签会生成超链接，这些超链接又不会像a标签那样显示在网页中。这就是超链接型的link标签。

  在多数浏览器中，link标签不产生任何作用。但是，这些link标签能够被搜索引擎和一些浏览器插件识别，从而产生关键性作用。

  比如，到页面RSS的link标签，能够被浏览器的RSS订阅插件识别，提示用户当前页面是可以RSS订阅的。

  另外一些link标签会把外部的资源链接到文档中，即：会实际下载这些资源，并且做出一些处理，比如我们常见的用link引入样式表。

  link标签的链接类型主要通过rel属性来区分

### 1.1 超链接类link标签

  超链接类link标签是一种被动型链接，在用户不操作的情况下，他们不会被主动下载。

  link标签具有特定的rel属性，会成为特定类型的link标签。产生超链接类link标签包括：具有rel=“canonical”的link、具有rel=“alternate”的link、具有rel=“prev”、rel=“next”的link等。

#### 1.1.1 canonical型link

```
<link rel="canonical" href="...">
```
  
  提示页面它的主URL，在网站中常常有多个URL指向同一页面的情况，搜索引擎访问这类页面时会去掉重复的页面，这个link会提示搜索引擎保留哪个URL。

#### 1.1.2 alternate型link

```
<link rel="alternate" href="...">
```

  这个标签提示页面它的变成形式，这个所谓的变形可能是当前页面内容的不同格式、不同语言或者不同的设备设计的版本，这种link通常也是提供给搜索引擎来使用。

  典型应用场景，页面提供rss订阅时，可以用这样的link引入：

```
  <link rel="alternate" type="application/rss+xml" title="RSS" href="...">
```

#### 1.1.3 prev型link 和 next型link

  在互联网应用中，很多网页都属于一个序列，比如分页浏览的场景，或者图片展示的场景，每个网页是序列中的一个项。

  这种时候，就适合使用prev和next型的link标签，来告诉搜索引擎或者浏览器它的前一项和后一项，这有助于页面的批量展示。

  因为next型link告诉浏览器“这是很可能访问的下一个页面”，HTML标准建议对next型link做预处理（在本文后会讲到预处理类的link）

#### 1.1.4 其它超链接型link

  其它超链接类link标签都表示一个跟当前文档相关联的信息，可以把这样的link标签视为一种带链接功能的meta标签。

  - rel="author"链接到本页面的作者，一般是mailto:协议
  - rel="help"链接到本页面的帮助页
  - rel="license"链接到本页面的版权信息页
  - rel="search"链接到本页面的搜索页面（一般是站内提供搜索时使用）

### 1.2 外部资源类link标签

  外部资源类link会被主动下载，并且根据rel类型做不同的处理。

#### 1.2.1 icon型link

  表示页面的icon。多数浏览器会读取icon型link，并且把页面的icon展示出来。

  icon型link是唯一一个外部资源类的元信息link，其它元信息link都是超链接，这意味着，icon型link中的图标地址默认会被浏览器下载使用。

  如果没有指定这样的link，多数浏览器会使用域名根目录下的favicon.ico，即使它并不存在，所以从性能角度考虑，建议一定要保证页面中有icon型link。

  只有icon型link有有效的sizes属性，HTML标准允许一个页面出现多个icon型link，并且用sizes指定它适合的icon尺寸。

#### 1.2.2 预处理类link

  导航到一个网站，需要经过dns查询域名、建立连接、传输数据、记载内存和渲染等一系列步骤。

  预处理类link标签允许我们控制浏览器，提前针对一些资源去做这些操作，以提高性能（当然，如果乱用，性能反而更差）
  
  - dns-prefetch型link提前对一个域名做dns查询，这样的link里面的href实际上只有域名有意义
  - preconnect型link提前对一个服务器建立tcp连接
  - prefetch型link提前去href指定对url内容
  - preload型link提前加载href指定对url
  - prerender型link提前渲染href指定对url

#### 1.2.3 modulepreload型link

  预先加载一个JavaScript的模块。可以保证JS模块不必等到执行时才加载。

  这里的所谓加载，是指定完成下载并放入内存，并不会执行对应的JavaScript。

```
<link rel="modulepreload" href="app.js">
<link rel="modulepreload" href="helpers.js">
<link rel="modulepreload" href="irc.js">
<link rel="modulepreload" href="fog-machine.js">
<script type="module" src="app.js">
```

#### 1.2.4 stylesheet型link

```
<link rel="stylesheet" href="xxx.css" type="text/css">
```

  基本用法是从一个CSS文件创建一个样式表。这里的type属性可以没有，如果有，必须是“text/css”才生效。

  rel前可以加上alternate，成为rel="alternate stylesheet"，此时必须再指定title属性

  这样可以为页面创建一份变体样式。一些浏览器，如firefox3.0，支持从浏览器菜单中切换这些样式。（但是大部分浏览器不支持，因此仅仅从语义角度了解这种用法）

#### 1.2.5 pingback型link

  这样的link表示本网页被引用是，应该使用的pingback地址，这个机制是一份独立的标准，遵守pingback协议的网站在引用本页面时，会向这个pingback url发送一个消息。

## 二、a标签

  标识文档中的特定位置。

  a标签充当类链接和目标点的角色。当a标签有href属性时，它是链接，当它有name时，它是链接的目标。

  具有href的a标签跟一些link一样，会产生超链接，也就是在用户不操作的情况下，他们不会被主动下载的被动型链接。



## 三、area标签

  area标签与a标签非常相似，不同的是，a标签是文本型的链接，area标签是区域型的链接。

  