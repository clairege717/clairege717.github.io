# [28 | JavaScript语法（预备篇）：到底要不要写分号呢？](https://time.geekbang.org/column/article/87179?utm_source=time_web&utm_medium=menu)

### 自动插入分号规则

自动插入分号规则其实独立于所有的语法产生式定义，它的规则有三条：
- 要有换行符，且下一个符号是不符合语法的，那么就尝试插入分号
- 有换行符，且语法中规定此处不能有换行符，那么就自动插入分号
- 源代码结束处，不能形成完整的脚步或者模块结构，那么就自动插入分号


### no LineTerminator here 规则

no LineTerminator here 规则表示它所在的结构中的这一位置不能插入换行符

自动插入分号规的第二条：有换行符，且语法中规定此处不能有换行符，那么就自动插入分号。这个跟 no LineTerminator here 规则强相关。

no LineTerminator here 规则
- 带标签的continue语句，不能在continue后插入换行
- 带标签带break语句，不能在break后插入换行
- return后不能插入换行
- 后自增、后自减运算符不能插入换行
- throw和Exception之间不能插入换行
- 凡是async关键字，后面不能插入换行
- 箭头函数的箭头前，不能插入换行
- yield之后，不能插入换行

以上为所有标准中的 no LineTerminator here 规则，实际上， no LineTerminator here 规则的存在，多数情况是为了保证自动插入分号行为是符合预期的

### 不写分号需要注意的情况

- **以括号开头的语句**
  
```
(function(a){
    console.log(a);
})()/* 这里没有被自动插入分号 */
(function(a){
    console.log(a);
})()
```
  这段代码看似是两个独立执行的函数表达式，但是其实第三组括号被理解为传参，导致抛出错误

- **以数组开头的语句**

```
var a = [[]]/* 这里没有被自动插入分号 */
[3, 2, 1, 0].forEach(e => console.log(e))
```
  这段代码的本意是一个变量a赋值，然后对一个数组执行forEach，但是因为没有自动插入分号，被理解为下标运算符和逗号表达式。

- **以正则表达式开头的语句**

```
var x = 1, g = {test:()=>0}, b = 1/* 这里没有被自动插入分号 */
/(a)/g.test("abc")
console.log(RegExp.$1)
```
  这段代码本意是声明三个变量，然后测试一个字符串中是否含有字母a，但是因为没有自动插入分号，正则的第一个斜杠被理解成了除号，后面的意思都变了。

- **以Template开头的语句**

```
var f = function(){
  return "";
}
var g = f/* 这里没有被自动插入分号 */
`Template`.match(/(a)/);
console.log(RegExp.$1)
```
  这段代码本意是声明函数f，然后赋值给g，再测试Template中是否含有字母a。但是因为没有自动插入分号，函数f被认为跟Template是一体的，进而被莫名其妙执行了一次


