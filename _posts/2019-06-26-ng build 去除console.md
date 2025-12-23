---
title: "20190626 ng build 去除console"
date: 2019-06-26
category: Daily
tags: [daily]
---


- 使用environment
  - environment.ts中，production= false
  - environment.prod.ts中，production= true

- main.ts中
    ```

    if (environment.production) {
    enableProdMode();
    // console
    window.console.log=function(){}
    window.console.dir=function(){}
    }

    ```