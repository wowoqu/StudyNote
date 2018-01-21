#Git Note
##安装Git
在Windows上使用Git，可以从Git官网直接下载安装程序，然后按默认选项安装即可。
安装完成后，需要进行设置，在命令行输入：
```
$ git config -- global user.name 'Your name'
$ git config -- global user.email 'Your email'
```
>注意git config命令的--global参数，用了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置，当然也可以对某个仓库指定不同的用户名和Email地址。

##创建版本库
```
$ git init
```

把一个文件放到Git仓库只需要两个步骤：

    1. $ git add 需要添加的文件

    2. $ git commit -m '这个版本的描述信息'

>简单解释一下git commit命令，-m后面输入的是本次提交的说明，可以输入任意内容，当然最好是有意义的，这样你就能从历史记录里方便地找到改动记录

**要随时掌握工作区的状态，使用git status命令。
如果git status告诉你有文件被修改过，用git diff可以查看修改内容。**

##版本回退

`git log`命令显示从最近到最远的提交日志，如果嫌输出信息太多，看得眼花缭乱的，可以试试加上`--pretty=oneline`参数。

`HEAD`指向的版本就是当前版本，前一个版本就是`HEAD^`因此，Git允许我们在版本的历
史之间穿梭，使用命令`$ git reset --hard commit_id`。

穿梭前，用`git log`可以查看提交历史，以便确定要回退到哪个版本。

要重返未来，用`git reflog`查看命令历史，以便确定要回到未来的哪个版本。

###示例代码：

    $ git reset --hard 3628164
    $ git reset --hard HEAD^  

>第一次修改 -> git add -> 第二次修改 -> git commit
>Git管理的是修改，当你用git add命令后，在工作区的第一次修改被放入暂存区，准备提交，但是，在工作区的第二次修改并没有放入暂存区，所以，git commit只负责把暂存区的修改提交了，也就是第一次的修改被提交了，第二次的修改不会被提交

##撤销修改

`git checkout -- file`可以丢弃工作区的修改：
就是让这个文件回到最近一次`git commit`或`git add`时的状态。

`git reset HEAD file`可以把暂存区的修改撤销掉:
`git reset`命令既可以回退版本，也可以把暂存区的修改回退到工作区。当我们用`HEAD`时，表示最新的版本。

- 场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- file。

- 场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令git reset HEAD file，就回到了场景1，第二步按场景1操作。

- 场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库

##删除文件

>$ git rm 文件名

删除完之后还需要提交上去。

>$ git commit -m 'remove something'

如果是误删除的话只需要敲如下命令即可还原：
>$ git checkout -- 文件名

`git checkout`其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”。

##远程仓库
需要先注册GitHub账号。由于你的本地Git仓库和GitHub仓库之间的传输是通过SSH加密的，所以，需要一点设置：

- 第1步：创建`SSH Key`。在用户主目录下，看看有没有`.ssh`目录，如果有，再看看这个目录下有没有`id_rsa`和`id_rsa.pub`这两个文件，
如果已经有了，可直接跳到下一步。如果没有，打开Shell（Windows下打开Git Bash），创建SSH Key：

    >$ ssh-keygen -t rsa -C 'youremail'

    你需要把邮件地址换成你自己的邮件地址，然后一路回车，使用默认值即可，由于这个Key也不是用于军事目的，所以也无需设置密码。

    如果一切顺利的话，可以在用户主目录里找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件，这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以放心地告诉任何人。

- 第2步：登陆GitHub，打开“Account settings”，“SSH Keys”页面：
然后，点“Add SSH Key”，填上任意Title，在Key文本框里粘贴id_rsa.pub文件的内容：

##添加远程库
- 第一步，在Github上创建一个空仓库

- 第二步，根据GitHub的提示，在本地的learngit仓库下运行命令：
   > $ git remote add origin git@github.com:Yourusername/warehousename.git <br>
   >这里需要替换为你自己的账户名跟仓库名。
- 第三步，由于远程库是空的，我们第一次推送`master`分支时，加上了`-u`参数，Git不但会把本地的`master`分支内容推送的远程新的`master`分支，还会把本地的`master`分支和远程的`master`分支关联起来。 
>$ git push -u origin master
- 第四布，从现在起，只要本地作了提交，就可以通过命令：
> $ git push origin master

##克隆Github上的仓库

要克隆一个仓库，首先必须知道仓库的地址，然后使用git clone命令克隆。

Git支持多种协议，包括https，但通过ssh支持的原生git协议速度最快。

##Git分支

查看分支：git branch

创建分支：git branch `<name>`

切换分支：git checkout `<name>`

创建+切换分支：git checkout -b `<name>`

合并某分支到当前分支：git merge `<name>`

删除分支：git branch -d `<name>`

用git log --graph命令可以看到分支合并图。

合并分支时，加上--no-ff参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而fast forward合并就看不出来曾经做过合并。

当手头工作没有完成时，先把工作现场git stash一下，然后去修复bug，修复后，再git stash pop，回到工作现场。

如果要丢弃一个没有被合并过的分支，可以通过git branch -D <name>强行删除。

##相关链接 [廖雪峰Git](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
