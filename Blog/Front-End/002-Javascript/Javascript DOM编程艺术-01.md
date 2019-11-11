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
  - setAttribute:**object**.setAttribute(attribute,value)


DOM还提供里许多其他的属性和方法：如nodeName、nodeValue、childNodes、nextSibling、parentNode