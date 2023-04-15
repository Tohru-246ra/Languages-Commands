# Dockerの基本的な使用例
### 参考 

書籍

 [Docker&仮想サーバー完全入門](https://onl.la/8ZaHXAR)</br>

web</br>
[VSCodeとDockerでシンプルなPythonの開発環境を作る](https://qiita.com/dai08srhg/items/dd4db729f965b2c6963d)</br>
[DockerでPython実行環境を作ってみる](https://qiita.com/jhorikawa_err/items/fb9c03c0982c29c5b6d5)

### コンテナの作り方

ローカルにディレクトリをつくり、その中にcompose.yml(必要であればDockerfile)を置く

```
docker-python/
  ├ Dockerfile
  └ compose.yml
```
compose.yml、Dockerfile の例は [ここから](./containerEX/)

コマンドラインで当該のディレクトリに行き、以下のコマンドを打つ
```
docker compose up -d --build 
```
### コマンド
```
docker compose stop  // コンテナ停止

docker compose restart // コンテナ再稼働

docker compose down // コンテナ削除

docker compose exec コンテナ名 /bin/bash // コンテナに入る

docker container ls // コンテナ一覧
```

