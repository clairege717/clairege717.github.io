# [22 | 浏览器DOM：你知道HTML的节点有哪几种吗？](https://time.geekbang.org/column/article/85031?utm_source=time_web&utm_medium=menu)

这里要介绍的DOM，指的是狭义的文档对象模型

## DOM API介绍

文档对象模型：是用来描述文档，这里的文档，是特指HTML文档（也用于XML文档，但是本课程不讨论XML）。同时它又是一个“对象模型”，这意味着它使用的是对象这样的概念来描述HTML文档。

HTML文档是一个由标签嵌套而成的树形结构，因此，DOM也是使用树形的对象模型来描述一个HTML文档。

DOM API大致包含4个部分：
- 节点：DOM树形结构中的节点相关API
- 事件：触发和监听事件相关API
- Range：操作文字范围相关API
- 遍历：遍历DOM需要的API

本篇文章重点介绍节点和遍历相关API

### 节点

DOM的树形结构所有的节点有统一的接口Node

![按照继承关系，介绍节点类型：](https://static001.geekbang.org/resource/image/6e/f6/6e278e450d8cc7122da3616fd18b9cf6.png)

#### Node

Node
- Element：元素型节点，跟标签相对应
  - HTMLElement
    - HTMLAnchorElement
    - HTMLAppletElement
    - HTMLAreaElement
    - HTMLAudioElement
    - HTMLBaseElement
    - HTMLBodyElement
    - ...
  - SVGElement
    - SVGAElement
    - SVGAltGlyphElement
    - ...
- Document：文档根节点
- CharacterData：字符数据
  - Text：文本节点
    - CDATASection：CDATA节点
  - Comment：注释
  - ProcessingInstruction：处理信息
- DocumentFragment：文档片段
- DocumentType：文档类型

在这些节点中，除了Document和DocumentFragment，都有与之对应的HTML写法

```
Element: <tagname>...</tagname>
Text: text
Comment: <!-- comments -->
DocumentType: <!Doctype html>
ProcessingInstruction: <?a 1?>
```

Node是DOM树继承关系的根结点，定义了DOM节点在DOM树上的操作。

首先，Node提供了一组属性，来表示它在DOM树中的关系，他们是：

- parentNode
- childNode
- firstNode
- lastNode
- nextSibling
- previousSibling
  
Node也提供了操作DOM树的API，主要有：
- appendChild
- insertBefore
- removeChild
- replaceChild
  
Node还提供了一些高级API
- compareDocumentPosition是一个用于比较两个节点中关系的函数
- contains检查一个节点是否包含另一个节点的函数
- isEqualNode检查两个节点是否完全相同
- isSameNode检查两个节点是否是同一个节点，实际上在JavaScript中可以用“===”
- cloneNode复制一个节点，如果传入参数true，则会连同子元素做深拷贝

DOM标准规定了节点必须从文档的create方法创建出来，不能够使用原生的JavaScript的new运算。于是，document对象有这些方法：
- createElement
- createTextNode
- createCDATASection
- createComment
- createProcessingInstruction
- createDocumentFragment
- createDocumentType

### Element 与 Attribute

Element表示元素，是Node的子类。

元素对应了HTML中的标签，它既有子节点，又有属性。所以Element子类中，有一系列操作属性的方法。

对DOM而言，Attribute和Property是完全不同的含义，只有特性场景下，两者才会互相关联。

首先，我们可以把元素的Attribute当作字符串来看待，有以下API：
- getAttribute
- setAttribute
- removeAttribute
- hasAttribute

如果追求极致的性能，还可以把Attribute当作节点：
- getAttributeNode
- setAttributeNode

如果喜欢property一样访问attribute，可以使用attributes对象，比如：document.body.attributes.class="a"等效于document.body.setAttribute("class","a")

### 查找元素

document节点提供了查找元素的能力。比如：
- querySelector
- querySelectorAll
- getElementById
- getElementsByName
- getElementsByTagName
- getElementsByClassName

getElementById、getElementsByName、getElementsByTagName、getElementsByClassName

### 遍历

通过Node的相关属性，我们可以用Javascript遍历树。

实际上，DOM API中还提供了NodeIterator和TreeWalker来遍历树。

NodeIterator的基本用法示例：

```
var iterator = document.createNodeIterator(document.body, NodeFilter.SHOW_TEXT | NodeFilter.SHOW_COMMENT, null, false);
var node;
while(node = iterator.nextNode())
{
    console.log(node);
}
```

TreeWalker的用法：

```
var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_ELEMENT, null, false)
var node;
while(node = walker.nextNode())
{
    if(node.tagName === "p")
        node.nextSibling();
    console.log(node);
}
```

## Range

Range API表示一个HTML上的范围，这个范围是以文字为最小单位的，所以Range不一定包含完整的节点，它可能是Text节点中的一段，也可以是头尾两个Text的一部分加上中间的元素。



