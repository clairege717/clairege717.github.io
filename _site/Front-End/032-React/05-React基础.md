# React基础

- Fragment
- export {default as AA} from './AA.js'
- PropTypes
  
  PropTypes.arrayOf(PropTypes.shape())

- props,state
  
  props:外部传入

  state:内部数据

- constructor(props){super(props);this.state={...}}
- this.state.todos.map((item=>{...}))
- dangerouslySetInnerHTML
  
  是 React 为浏览器 DOM 提供 innerHTML 的替换方案。通常来讲，使用代码直接设置 HTML 存在风险，因为很容易无意中使用户暴露于跨站脚本（XSS）的攻击。因此，你可以直接在 React 中设置 HTML，但当你想设置 dangerouslySetInnerHTML 时，需要向其传递包含 key 为 __html 的对象，以此来警示你。

  ```
function createMarkup() {
  return {__html: 'First &middot; Second'};
}

function MyComponent() {
  return <div dangerouslySetInnerHTML={createMarkup()} />;
}
  ```

- setState 异步
  
  setState(()=>{set...},()=>{callback...})

- 事件
  
  注意this的指向。使用bind(this)或箭头函数。

- ref
  
  createRef：创建一个能够通过 ref 属性附加到 React 元素的 ref

  ```
  class MyComponent extends React.Component {
    constructor(props) {
        super(props);

        this.inputRef = React.createRef();
    }

    render() {
        return <input type="text" ref={this.inputRef} />;
    }

    componentDidMount() {
        this.inputRef.current.focus();
    }
  }
  ```
  
- AJAX
  
  axios
  
- hooks
- context
  
  createContxt，是react提供的用于跨组件传值的方法。

  createContxt方法返回一个对象，里面有两个组件:{Provider,Consumer}。

  ```
  const {
      Privoder,
      Consumer: CounterConsumer // 解构出来重新赋值给一个CounterConsumer的组件
  } = createContext()
  ```
  
  Provider用于提供状态。

  ```
  // 封装一个基本的Provider，因为直接使用Provider，不方便管理状态
  class CounterProvider extends Component{
      constructor(){
          super()
          // 这里的状态就是共享的，任何CounterProvider的后代组件都可以通过CounterConsumer来接收这个值
          this.state = {
              count: 100
          }
      }

      // 使用Provider必须有一个value值，这个value里可以传递任何的数据。一般还是传递一个对象比较合理
      <Provider value={{
          count: this.state.count
      }}>
        {this.props.children}
      </Provider>
  }
  ```
  
  Consumer用于接收状态。
  
  Consumer的children必须是一个方法，这个方法有一个参数，这个参数就是Provider的value。

  ```
  <CounterConsumer>
  {
      ({count})=>{
          return <span>{count}</span>
      }
  }
  </ConterConsumer>
  ```
  

- HOC和CFA
  
  HOC：高阶组件 Higher

  [JS函数式编程指南](https://legacy.gitbook.com/book/llh911001/mostly-adequate-guide-chinese/details)
- 