# Gitコマンド 
##### origin : リモートリポジトリの場所(URL)にデフォルトでつけられる名前
##### main : (GitHubにおけるデフォルトの) メインブランチ名
##### origin main : リモートリポジトリのメインブランチ
##### origin/main : origin main を追跡するリモート追跡ブランチ

</br>

##### ワーキングツリー : 今作業しているファイル
##### インデックス : コミットするためにファイルを登録する場所

</br>

参考</br>
https://qiita.com/seri1234/items/e651b3e108a695a92809<br/>
https://qiita.com/uasi/items/69368c17c79e99aaddbf
## Index
* [GItを始める](#GItを始める)
* [リモートから変更を取得](#リモートから変更を取得)
* [リモートに変更を反映](#リモートに変更を反映)
* [](#)
* [](#)

</br>

### Gitを始める
ローカルリポジトリを作成
```
git init
```
または既存のリポジトリをローカルに複製
```
git clone
```
ブランチの一覧
```
git branch -a
```
ブランチ作成 & 切り替え
```
git checkout -b main
```
ブランチの削除
```
git branch -D master
```
リモートリポジトリを追加
```
git remote add origin URL
```
参考</br>
https://qiita.com/kohga/items/dccf135b0af395f69144

</br>

### リモートから変更を取得
```
git pull origin main
```
または
```
git fetch origin main
git merge origin/main
```
参考</br>
https://qiita.com/wann/items/688bc17460a457104d7d

</br>

### リモートに変更を反映
① ファイルを登録
```
git add ファイル名
```
カレントディレクトリ下全てのファイルを登録するとき
```
git add .
```
② ファイルの変更や追加をコミット
```
git commit -m "メッセージ"
```
③ リモートリポジトリに変更を反映
```
git push origin main
```