# 离线安装vscode插件

## 一、下载插件

- 进入 vs code官网
    
    [vs code插件官网](https://marketplace.visualstudio.com/)

- 找到需要下载的插件

    [Debugger for Chrome](https://marketplace.visualstudio.com/items?itemName=msjsdiag.debugger-for-chrome)

- 修改地址

    插件下载的拼接方式：https://${publisher}.gallery.vsassets.io/_apis/public/gallery/publisher/${publisher}/extension/${extension name}/${version}/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage

- 替换地址

    整理后的地址：https://msjsdiag.gallery.vsassets.io/_apis/public/gallery/publisher/msjsdiag/extension/debugger-for-chrome/4.11.3/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage

## 二、引入插件文件

