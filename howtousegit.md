# how to use git

* git提交/删除文件
    ```
    git add <path> 提交到暂存区
    git rm <path>
    git commit -m <description text>
    ```

* git查看日志

    ```
    git log
    git log --pretty=oneline
    git reflog 记录每一条命令
    ```

* git 回溯

    ```
    git reset --hard HEAD^ | HEAD^^
    git reset --hard <commit id> 
    git reset HEAD <filename> 将暂存区回退到工作区
    ```

* 查看状态

    ```
    git status
    ```

    *查看暂存区*

* 查看工作区版本库区别

    ```
    git diff [<option>] [<commit>[<commit>]] [--] [<path>...]
    git diff HEAD -- <path>
    ```

* 丢弃工作区修改(将版本库中的替换工作区中的)

    ```
    git checkout -- <filename>
    ```

* 推送远程库

    ```
    git remote add origin <地址>
    git push -u orgin master   第一次
    git push orgin master 
    git clone <地址> 下载
    ```

