# Gitコマンド 
##### origin : リモートリポジトリの場所(URL)にデフォルトでつけられる名前
##### main : メインブランチ名
##### origin main : リモートリポジトリのメインブランチ
##### origin/main : origin main を追跡するリモート追跡ブランチ

</br>

#### ワーキングツリー : 今作業しているファイル
#### インデックス : コミットするためにファイルを登録する場所

</br>

参考</br>
[https://qiita.com/seri1234/items/e651b3e108a695a92809](https://qiita.com/seri1234/items/e651b3e108a695a92809)<br/>
[https://qiita.com/uasi/items/69368c17c79e99aaddbf](https://qiita.com/uasi/items/69368c17c79e99aaddbf)
## Index
* [リモートから変更を取得](#リモートから変更を取得)
* [リモートに変更を反映](#リモートに変更を反映)
* [](#)
* [](#)
* [](#)

### リモートから変更を取得
```
git pull origin main
```
または
```
git fetch origin main
git merge origin/main
```

</br>

参考</br>
[https://qiita.com/wann/items/688bc17460a457104d7d](https://qiita.com/wann/items/688bc17460a457104d7d)

### リモートに変更を反映
まずはファイルを登録
```
git add ファイル名
```
カレントディレクトリ下全てのファイルを登録するときは
```
git add .
```
ファイルの変更や追加をコミット
```
git commit -m "メッセージ"
```