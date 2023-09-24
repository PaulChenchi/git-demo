# GIT-DEMO

- 版本檢視
	- git --version

-設定使用者資訊
	- git config --global user.name "paul"
	- git config --global user.email "861124cc@gmail.com"

- git設定資訊	
	- git config --list

- 切換目錄 cd
	- cd\ #根目錄
	- cd d:\ #D槽
	- cd C:\Users\User\Desktop\python-django\GIT\demo #指定路徑

- 初始本地倉庫
	- git init(初始化)

- 檢視目前狀態
	-git status
		- Untrack (未控管)
- 加入控管
	- git  add <檔名>
		-Untrack -> Added (加入)
		-Added -> Modified (修改)
	- 四種狀態
		-U -> A -> M
		- D
	- 以文字檔為主
	- git add . # <all file>
		-將所有未加入跟變動的一次確認

- 修改後的確認
	-Modified -> Added (git add <檔名>)

- 新增忽略檔案
	- .gitignore
		-*.jpg
		-*.vscode/

- 恢復上一個動作
	- git checkout .

- 恢復刪除後的檔案
	- git restore <filename>
	- git restore . (恢復所有未確認刪除的檔案)

- 查找控管檔案
	-git ls-files -s

- 檢視object內容物
	- git cat-file (-t) sha-1
		-t(型態(blob))
		-p(內容)

- 正式儲存到倉庫
	- git commit -m "message"
	- git commit -am "message" 
		- add+message
	- git commit --amend
		- 合併上一次commit
		- vim
			- i(insert)鍵盤模式


- 檢視目前幾個commit
	- git log
	- q(強勢離開)
	- git log --oneline


- git cat-file -p commit-sha1
	- git cat-file -p tree-sha1

- git rm -f
	- 暫存區(完整刪除)
	- 倉庫區(曾經git commit)
		- 刪除
			- git add (確認刪除)
		- 恢復
			- gti restore --staged(暫存區)
				- git add (確認刪除)
				- git restore(恢復)

- git rm --cached <filename>
	- 暫存/倉庫區
		- 移回工作目錄(不控管)

- 分支
	- master(預設)
	- git branch
		- 分支列表
	- git branch <branch name>
		- 產生分支
- git checkout 
	- git checkout <branch name>(切換分支)
	- git checkout -b (新增+切換)
	- git checkout -commit (sha1)

- git merge(合併)
	- 切換 git checkout master
		- git merge test
	- 合併發生衝突
		- 選擇以哪個分支(current/incoming/both)
		- git merge abort 
			- 取消合併
- git branch -D<branch name>
	-刪除分支(-D，直接刪除)

- git reset
	- 重置指令
	- git reset --mixed(預設) commit(sha1)
	- git reset --soft commit(sha1)
	- git reset --hard commit(sha1)
	- 反悔 resrt 
		- git reset ORIG_HEAD
- git reflog
	- 查找過往的commit紀錄
		- git reset commit (sha1)

- git checkout HEAD
	- HEAD~1(前幾個分支的意思)
	
- 
	






--------------------------------------------

-git hub 

-加入雲端倉庫
	-git remote add origin https://github.com/PaulChenchi/git-demo.git

-git remote -v
	-顯示目前連結的遠端倉庫
-git push -u origin master



- echo "# git-demo" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/PaulChenchi/git-demo.git
- git push -u origin main
