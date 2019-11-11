# Javascript DOM 编程艺术

## DOM

window对象对应着浏览器窗口本身，这个对象的属性和方法通常统称为BOM（浏览器对象模型）

- ### 文档：DOM中的D(document)
- ### 对象：DOM中的O(object)
- ### 模型：DOM中的M(model)
- ### 节点(node)

  1. 元素节点(element node):\<body\>等
  2. 文本节点(text node):文本节点总是被包含在元素节点内部。并非所有元素节点都有文本节点。
  3. 属性节点(attribute node):属性节点用来对元素做出更具体对描述，属性节点总是被放在起始标签，所有属性节点总是被包含在元素节点中。并非所有元素都包含属性节点。
  4. CSS（层叠样式表）
    继承（inheritance）是CSS技术中一项强大功能。
    4.1. class属性
    4.2. id属性

  5. 获取元素
     5.1. getElementById：返回一个对象，对应着文档里的一个特定的元素节点
     5.2. getElementsByTagName：返回一个对象数组
     5.3. getElementsByClassName：返回一个对象数组

- ### 获取和设置属性
  - getAttribute:**object**.getAttribute(attribute)
  - setAttribute:**object**.setAttribute(attribute,value)；是“第1级DOM”（DOM Level 1）的组成部分；可以设置任意元素节点的任意属性，也可以直接通过元素属性进行设置。

> **DOM Level 1 Core**
> 
> &nbsp;&nbsp;&nbsp;&nbsp;The W3C's DOM Level 1 Core is a powerful object model for changing the content tree of documents. It is supported in all major browsers including Mozilla Firefox and Microsoft Internet Explorer. It is a powerful base for scripting on the web.
> 
> &nbsp;&nbsp;&nbsp;&nbsp;W3C的DOM Level 1 核心是修改文档内容树的一个强大的对象模型。它被所有主要的浏览器支持，包括Firefox、IE。它是web脚本的强大的基础。
> 
> &nbsp;&nbsp;&nbsp;&nbsp;The W3C DOM Level 1 allows you to change the content tree any way you want. It is powerful enough to build any HTML document from scratch. It allows authors to change anything in the document from script, at any time. The easiest way for web page authors to change the DOM dynamically is using JavaScript. In JavaScript, the document is accessible the same way it has been in older browsers: from the document property of the global object. This document object implements the Document interface from the W3C's DOM Level 1 spec.
> 
> &nbsp;&nbsp;&nbsp;&nbsp;W3C的DOM Level 1允许你以任何方式修改内容树。它足够强大来从头开始创建HTML文档。它允许作者使用脚本来修改文档中的任意内容。对于网页开发人员来说，最简单的动态修改DOM的方式是JavaScript。在旧版的浏览器中，都可以使用JavaScript访问全局的document对象的属性来得到文档。这个文档对象实现了W3C的DOM Level 1定义的文档接口。

DOM还提供里许多其他的属性和方法：如nodeName、nodeValue、childNodes、nextSibling、parentNode