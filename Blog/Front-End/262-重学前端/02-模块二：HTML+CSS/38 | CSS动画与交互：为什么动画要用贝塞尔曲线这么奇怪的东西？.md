# [38 | CSS动画与交互：为什么动画要用贝塞尔曲线这么奇怪的东西？](https://time.geekbang.org/column/article/91325?utm_source=time_web&utm_medium=menu)

## 属性

### animation 属性和transition 属性

```
@keyframes mykf
{
  from {background: red;}
  to {background: yellow;}
}

div
{
    animation:mykf 5s infinite;
}
```

animation 分成六个部分：
- animation-name：动画的名称，这是一个keyframes 类型的值。（keyframes产生一种数据，用于定义动画的关键帧）
- animation-duration：动画的时长
- animation-timing-function：动画的时间曲线
- animation-delay：动画开始前的延迟
- animation-iteration-count：动画的播放次数
- animation-direction：动画的方向

#### 动画的时间曲线

- 三次贝塞尔曲线
  
  贝塞尔曲线是一种插值曲线，描述来两个点之间插值来形成连续点曲线形状点规则。

  一个量（可以是任何矢量或者标量）从一个值变化到另一个值，如果我们希望它按照一定时间平滑地过渡，就必须要对它进行插值。

  最基本的情况，我们认为这个变化是按照时间均匀进行的，这个时候，我们称其为线性插值。

  而实际上，线性插值不大能满足我们的需要，因此数学上出现了很多其它的插值算法，其中贝塞尔插值法是非常典型的一种。它根据一些变换中的控制点来决定值与时间的关系。

  贝塞尔曲线是一种被工业生产验证来很多年的曲线，它最大的特点就是“平滑”。

  时间曲线平滑，意味着较少突兀的变化，这是一般动画设计所追求的。

  k次贝塞尔插值算法需要k+1个控制点，最简单的一次贝塞尔插值就是线性插值，将时间表示为0到1的区间，一次贝塞尔插值公式是：

  ![一次贝塞尔插值公式](https://static001.geekbang.org/resource/image/d7/f8/d7e7c3bcc1e2b2ce72fde79956e872f8.png)

  “二次贝塞尔插值”有3个控制点。相当于对P0和P1，P1和P2分别做贝塞尔插值，再对结果做一次贝塞尔插值计算：

  ![二次贝塞尔插值公式](https://static001.geekbang.org/resource/image/14/84/14d6a5396b7c0cc696c52a9e06e45184.png)

  “三次贝塞尔插值”则是“两次‘二次贝塞尔插值’的结果，再做一次贝塞尔插值”：

  ![三次贝塞尔插值](https://static001.geekbang.org/resource/image/65/b2/65ff1dd9b8e5911f9dd089531acea2b2.png)

  贝塞尔曲线的定义中带有一个参数t，但是这个t并非真正的时间，实际上贝塞尔曲线的一个点（x, y），这里x轴才代表时间。

  浏览器中一般采用数值算法，其中公认做有效的是牛顿积分：

  ```
  function generate(p1x, p1y, p2x, p2y) {
    const ZERO_LIMIT = 1e-6;
    // Calculate the polynomial coefficients,
    // implicit first and last control points are (0,0) and (1,1).
    const ax = 3 * p1x - 3 * p2x + 1;
    const bx = 3 * p2x - 6 * p1x;
    const cx = 3 * p1x;

    const ay = 3 * p1y - 3 * p2y + 1;
    const by = 3 * p2y - 6 * p1y;
    const cy = 3 * p1y;

    function sampleCurveDerivativeX(t) {
        // `ax t^3 + bx t^2 + cx t' expanded using Horner 's rule.
        return (3 * ax * t + 2 * bx) * t + cx;
    }

    function sampleCurveX(t) {
        return ((ax * t + bx) * t + cx ) * t;
    }

    function sampleCurveY(t) {
        return ((ay * t + by) * t + cy ) * t;
    }

    // Given an x value, find a parametric value it came from.
    function solveCurveX(x) {
        var t2 = x;
        var derivative;
        var x2;

        // https://trac.webkit.org/browser/trunk/Source/WebCore/platform/animation
        // First try a few iterations of Newton's method -- normally very fast.
        // http://en.wikipedia.org/wiki/Newton's_method
        for (let i = 0; i < 8; i++) {
            // f(t)-x=0
            x2 = sampleCurveX(t2) - x;
            if (Math.abs(x2) < ZERO_LIMIT) {
                return t2;
            }
            derivative = sampleCurveDerivativeX(t2);
            // == 0, failure
            /* istanbul ignore if */
            if (Math.abs(derivative) < ZERO_LIMIT) {
                break;
            }
            t2 -= x2 / derivative;
        }

        // Fall back to the bisection method for reliability.
        // bisection
        // http://en.wikipedia.org/wiki/Bisection_method
        var t1 = 1;
        /* istanbul ignore next */
        var t0 = 0;

        /* istanbul ignore next */
        t2 = x;
        /* istanbul ignore next */
        while (t1 > t0) {
            x2 = sampleCurveX(t2) - x;
            if (Math.abs(x2) < ZERO_LIMIT) {
                return t2;
            }
            if (x2 > 0) {
                t1 = t2;
            } else {
                t0 = t2;
            }
            t2 = (t1 + t0) / 2;
        }

        // Failure
        return t2;
    }

    function solve(x) {
        return sampleCurveY(solveCurveX(x));
    }

    return solve;
}

```
  
- 贝塞尔曲线拟合

理论上，贝塞尔曲线可以通过分段的方式拟合任意曲线，但是一些特殊的曲线，是可以用贝塞尔曲线完美拟合的，比如抛物线：

```
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Simulation</title>
  <style>
    .ball {
      width:10px;
      height:10px;
      background-color:black;
      border-radius:5px;
      position:absolute;
      left:0;
      top:0;
      transform:translateY(180px);
    }
  </style>
</head>
<body>
  <label> 运动时间：<input value="3.6" type="number" id="t" />s</label><br/>
  <label> 初速度：<input value="-21" type="number" id="vy" /> px/s</label><br/>
  <label> 水平速度：<input value="21" type="number" id="vx" /> px/s</label><br/>
  <label> 重力：<input value="10" type="number" id="g" /> px/s²</label><br/>
  <button onclick="createBall()"> 来一个球 </button>
</body>
</html>
```

```
function generateCubicBezier (v, g, t){
    var a = v / g;
    var b = t + v / g;

    return [[(a / 3 + (a + b) / 3 - a) / (b - a), (a * a / 3 + a * b * 2 / 3 - a * a) / (b * b - a * a)],
        [(b / 3 + (a + b) / 3 - a) / (b - a), (b * b / 3 + a * b * 2 / 3 - a * a) / (b * b - a * a)]];
}

function createBall() {
  var ball = document.createElement("div");
  var t = Number(document.getElementById("t").value);
  var vx = Number(document.getElementById("vx").value);
  var vy = Number(document.getElementById("vy").value);
  var g = Number(document.getElementById("g").value);
  ball.className = "ball";
  document.body.appendChild(ball)
  ball.style.transition = `left linear ${t}s, top cubic-bezier(${generateCubicBezier(vy, g, t)}) ${t}s`;
  setTimeout(function(){ 
    ball.style.left = `${vx * t}px`; 
    ball.style.top = `${vy * t + 0.5 * g * t * t}px`; 
  }, 100);
  setTimeout(function(){ document.body.removeChild(ball); }, t * 1000);
}

```



