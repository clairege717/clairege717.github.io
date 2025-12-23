# react坑

## 一、fetch

- ### Already read

  已经调用了 `response.json()`，这个时候重复调用该方法时就会报错。（实际上，再次调用其它任何转换方法，如 `.text()` 也会报错）

- ### fetch请求对某些错误http状态不会reject

  fetch返回的promise在某些错误的http状态下如400、500等不会reject

  ```javascript
  function checkStatus(response) {
    if (response.status >= 200 && response.status < 300) {
      return response;
    }
    const error = new Error(response.statusText);
    error.response = response;
    throw error;
  }
  function parseJSON(response) {
    return response.json();
  }
  export default function request(url, options) {
    let opt = options||{};
    return fetch(url, {credentials: 'include', ...opt})
      .then(checkStatus)
      .then(parseJSON)
      .then((data) => ( data ))
      .catch((err) => ( err ));
  }
  ```

