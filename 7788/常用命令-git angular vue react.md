# 常用命令

1. git

    - init 
    - clone
    - add
    - status
    - diff
    - commit
    - reset
    - rm
    - branch
    - checkout
    - merge
    - log
    - tag
    - remote
    - fetch
    - pull
    - push


    git clone ...

    git add 

    git log --pretty=oneline

    git reset --merge   恢复到merge请求之前的

    git diff [文件名]   比较文件差异

    git branch -a   查看所有分支信息

    git branch -v   查看本地库中的所有分支

    git branch dev  创建dev分支

    git checkout dev    切换到dev分支

    git push origin --delete Chapater6   可以删除远程分支Chapater6

    git branch -d Chapater8 可以删除本地分支
    
    git checkout -b Chapater6 切换分支

    git add [文件名] 添加待提交的文件

    git commit -m '日志信息' 提交

    git config user.name    查看git用户名

    git config user.email   查看git邮箱

    git config --global user.name 'username'    修改用户名
    
    git config --global user.email 'email'  修改用户邮箱

    git pull origin develop 将develop分支上的内容拉取到本地分支 
    
    git push origin dev-gyd:dev 将本地dev-gyd分支的代码提交到远程dev分支

    #### git fetch 合并远程仓库到本地

    //方法一

    $ git fetch origin master //从远程的origin仓库的master分支下载代码到本地的origin master

    $ git log -p master.. origin/master//比较本地的仓库和远程参考的区别

    $ git merge origin/master//把远程下载下来的代码合并到本地仓库，远程的和本地的合并

    //方法二

    $ git fetch origin master:temp //从远程的origin仓库的master分支下载到本地并新建一个分支temp

    $ git diff temp//比较master分支和temp分支的不同

    $ git merge temp//合并temp分支到master分支

    $ git branch -d temp//删除temp

    #### fork远程到本地，并与远程保持同步

    git clone https://github.com/claire/month.git  clone forked

    git remote add jsfrontgroup https://github.com/jsfront/month.git  添加远程源作者的仓库到本地

        jsfrontgroup是关联的原仓库在本地的名称
    
    git remote -v   查看本地所有仓库

    git fetch --all   更新git remote中所有的repo所包含的最新commit-id

    git rebase jsfrontgroup/master   与源作者同步

    git push origin master  提交到自己的仓库

    git status 查看提交


    git fetch jsfrontgroup   将远程分支同步到本地

    git checkout master 检查本地master代码变更

    git merge jsfrontgroup/master  分支合并


    #### git .gitignore忽略文件.DS_Store

    .DS_Store

    */.DS_Store

    ### git 清除缓存（若已经在git记录中的文件添加到ignore，需使用）

    git rm -r --cached .
    
    git add .
    
    git commit -m 'update .gitignore'

    **如果是项目做到一半才开始加入.gitignore,则需要在commit所有已经修改文件后，执行以下命令保证.gitignore开始生效。**

    git rm -r --cached .

    git add .
    
    git commit -m 'update .gitignore'

    git stash 缓存本地未提交代码（切换分支前使用）    
    
    git stash pop 导出缓存的未提交代码（切换分支后使用）  

2. angular

    - @angular/cli
    
        ng new projectName

        ng serve --open
        
    - ionic

        sudo npm install -g cordova ionic

        ionic start myApp tabs
        
        ionic serve

        ionic cordova platform add android
        
        ionic cordova build android
        
        ionic cordova emulate android
  
        ionic4 新增了 prepare 命令，在使用 

            ionic cordova platofrm add android/ios 

        构建 android 或 ios 平台后，如果修改了代码，在 ionic3 中只要执行

            ionic build 
            
        就可以应用改变，

        但在 ionic4 中需要行执行 

            ionic cordova prepare android/ios 
            
        命令才能将改变应用到平台中，当然在打包之前还是一样要执行 ionic build --prod 命令。
  
    

3. vue

    - vue cli 2.x
        
        vue init webpack vue-demo00

        vue init webpack-simple vue-demo01 （中小项目创建，目录结构简单）

    - vue cli 3.x

        vue create hello-world

    - npm run serve

    - npm run build

    - Vue CLI 3.x和2.x之间桥接工具

        npm install -g @vue/cli-init


4. React

    - react native

        react-native init

        react-native run-ios(android)

        react-native link 