# [37 | 浏览器API（小实验）：动手整理全部API](https://time.geekbang.org/column/article/90998?utm_source=time_web&utm_medium=menu)

按照每个API所在的标准分类。

用代码来反射浏览器环境中全局对象的属性，然后用JavaScript的filter方法来逐步过滤掉已知的属性。

整理API的方法如下：
- 从Window的属性中，找到API名称
- 查询MDN或者Google，找到API所在的标准
- 阅读标准，手工或者用代码整理出标准中包含的API
- 用代码在Window的属性中过滤掉标准中涉及的API

重复上面的过程，我们可以找到所有的API对应的标准。

## JavaScript中规定API 

大部分的API属于Window对象（或者说全局对象）。

首先调用：Object.getOwnPropertyNames(window)。

这里包含来JavaScript标准规定的属性，做一下过滤：
```
{
    let js = new Set();
    let objects = ["BigInt", "BigInt64Array", "BigUint64Array", "Infinity", "NaN", "undefined", "eval", "isFinite", "isNaN", "parseFloat", "parseInt", "decodeURI", "decodeURIComponent", "encodeURI", "encodeURIComponent", "Array", "Date", "RegExp", "Promise", "Proxy", "Map", "WeakMap", "Set", "WeakSet", "Function", "Boolean", "String", "Number", "Symbol", "Object", "Error", "EvalError", "RangeError", "ReferenceError", "SyntaxError", "TypeError", "URIError", "ArrayBuffer", "SharedArrayBuffer", "DataView", "Float32Array", "Float64Array", "Int8Array", "Int16Array", "Int32Array", "Uint8Array", "Uint16Array", "Uint32Array", "Uint8ClampedArray", "Atomics", "JSON", "Math", "Reflect", "escape", "unescape"];
    objects.forEach(o => js.add(o));
    let names = Object.getOwnPropertyNames(window)
    names = names.filter(e => !js.has(e));
}
```

## DOM 中的元素构造器

DOM 中部分包含了document属性和一系列的构造器，我们可以用JavaScript的prototype来过滤构造器。

```
    names = names.filter( e => {
        try { 
            return !(window[e].prototype instanceof Node)
        } catch(err) {
            return true;
        }
    }).filter( e => e != "Node")
```
这里把所有Node的子类都过滤掉，再把Node本身也过滤掉。

## Window对象上的属性

[Window对象的定义](https://html.spec.whatwg.org/#window)

这里有一个Window接口，是使用WebIDL定义的，整理出函数和属性：

```
 window,self,document,name,location,history,customElements,locationbar,menubar, personalbar,scrollbars,statusbar,toolbar,status,close,closed,stop,focus, blur,frames,length,top,opener,parent,frameElement,open,navigator,applicationCache,alert,confirm,prompt,print,postMessage
```

编写代码，把这些函数和属性，从浏览器Window对象的属性中去掉：
```
{
    let names = Object.getOwnPropertyNames(window)
    let js = new Set();
    let objects = ["BigInt", "BigInt64Array", "BigUint64Array", "Infinity", "NaN", "undefined", "eval", "isFinite", "isNaN", "parseFloat", "parseInt", "decodeURI", "decodeURIComponent", "encodeURI", "encodeURIComponent", "Array", "Date", "RegExp", "Promise", "Proxy", "Map", "WeakMap", "Set", "WeakSet", "Function", "Boolean", "String", "Number", "Symbol", "Object", "Error", "EvalError", "RangeError", "ReferenceError", "SyntaxError", "TypeError", "URIError", "ArrayBuffer", "SharedArrayBuffer", "DataView", "Float32Array", "Float64Array", "Int8Array", "Int16Array", "Int32Array", "Uint8Array", "Uint16Array", "Uint32Array", "Uint8ClampedArray", "Atomics", "JSON", "Math", "Reflect", "escape", "unescape"];
    objects.forEach(o => js.add(o));
    names = names.filter(e => !js.has(e));

    names = names.filter( e => {
        try { 
            return !(window[e].prototype instanceof Node)
        } catch(err) {
            return true;
        }
    }).filter( e => e != "Node")

    let windowprops = new Set();
    objects = ["window", "self", "document", "name", "location", "history", "customElements", "locationbar", "menubar", " personalbar", "scrollbars", "statusbar", "toolbar", "status", "close", "closed", "stop", "focus", " blur", "frames", "length", "top", "opener", "parent", "frameElement", "open", "navigator", "applicationCache", "alert", "confirm", "prompt", "print", "postMessage", "console"];
    objects.forEach(o => windowprops.add(o));
    names = names.filter(e => !windowprops.has(e));
}
```

还要过滤掉所有的事件，也就是on开头的属性：
```
names = names.filter( e => !e.match(/^on/))
```

过滤掉webkit前缀的私有属性：
```
names = names.filter( e => !e.match(/^webkit/))
```

过滤掉在HTML标准中能找到的所有接口：
```

    let interfaces = new Set();
    objects = ["ApplicationCache", "AudioTrack", "AudioTrackList", "BarProp", "BeforeUnloadEvent", "BroadcastChannel", "CanvasGradient", "CanvasPattern", "CanvasRenderingContext2D", "CloseEvent", "CustomElementRegistry", "DOMStringList", "DOMStringMap", "DataTransfer", "DataTransferItem", "DataTransferItemList", "DedicatedWorkerGlobalScope", "Document", "DragEvent", "ErrorEvent", "EventSource", "External", "FormDataEvent", "HTMLAllCollection", "HashChangeEvent", "History", "ImageBitmap", "ImageBitmapRenderingContext", "ImageData", "Location", "MediaError", "MessageChannel", "MessageEvent", "MessagePort", "MimeType", "MimeTypeArray", "Navigator", "OffscreenCanvas", "OffscreenCanvasRenderingContext2D", "PageTransitionEvent", "Path2D", "Plugin", "PluginArray", "PopStateEvent", "PromiseRejectionEvent", "RadioNodeList", "SharedWorker", "SharedWorkerGlobalScope", "Storage", "StorageEvent", "TextMetrics", "TextTrack", "TextTrackCue", "TextTrackCueList", "TextTrackList", "TimeRanges", "TrackEvent", "ValidityState", "VideoTrack", "VideoTrackList", "WebSocket", "Window", "Worker", "WorkerGlobalScope", "WorkerLocation", "WorkerNavigator"];
    objects.forEach(o => interfaces.add(o));

    names = names.filter(e => !interfaces.has(e));

```

## 其它属性

把过滤代码抽象成一个函数：
```
function filterOut(names, props) {
    let set = new Set();
    props.forEach(o => set.add(o));
    return names.filter(e => !set.has(e));
}
```

查看剩余属性：

### [ECMAScript 2018 Internationalization API](http://www.ecma-international.org/ecma-402/5.0/index.html#Title)

### [Streams 标准](https://streams.spec.whatwg.org/#blqs-class)

### [WebGL](https://www.khronos.org/registry/webgl/specs/latest/1.0/#5.15)

### [Web Audio API](https://www.w3.org/TR/webaudio/)

### [Encoding 标准](https://encoding.spec.whatwg.org/#dom-textencoder)

### [Web Background Synchronization](https://wicg.github.io/BackgroundSync/spec/#sync-manager-interface)

### [Web Cryptography API](https://www.w3.org/TR/WebCryptoAPI/)

### [Media Source Extensions](https://www.w3.org/TR/media-source/)

### [The Screen Orientation API](https://www.w3.org/TR/screen-orientation/)





