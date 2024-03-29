# SQLクエリ(MySQL,MariaDB) サンプル
**SQL** (Structured Query Language) は<br>
データの挿入、更新、削除、取得等を行う**DML** (Data Manipulation Language) と<br>
データベースや表などを定義する**DDL** (Data Definition Language) に大別される。
## INDEX
* [DML(データの取得)](#DMLデータの取得)
  * [条件](#条件)
  * [並べ替え](#並べ替え)
  * [最大数の指定](#最大数の指定)
  * [集計関数](#集計関数)
  * [グループ化](#グループ化)
  * [グループ化から更なる絞り込み](#グループ化から更なる絞り込み)
  * [サブクエリ](#サブクエリ)
  * [結合](#結合)
* [DML(データの挿入、変更、削除)](#DMLデータの挿入更新削除)
  * [データの挿入](#データの挿入)
  * [データの更新](#データの更新)
  * [データの削除](#データの削除)
* [DDL](#DDL)  
  * [データベースの作成](#データベースの作成)
  * [テーブルの作成](#テーブルの作成)
  * [テーブル、データベースの削除](#テーブルデータベースの削除)
  * [列(カラム)の追加](#列カラムの追加)
  * [列名の変更](#列目の変更)
  * [列の削除](#列の削除)
* [その他](#その他)
  * [MySQLの起動、ログイン](#MySQLの起動ログイン)
  * [MySQLのログアウト、停止](#MySQLのログアウト停止)
# DML(データの取得)
データの取得では基本的に下のような形で記述をする。
```
SELECT 列名1,列名2, …
FROM 表名1,表名2, …
WHERE 条件;
```
#### 条件
**比較演算子**、**AND演算子**、**OR演算子**などが使える。<br>
特殊な条件としては<br>
"**ある文字を含むデータ**"  を取得したい時に用いる**LIKE演算子** `列名 LIKE "%文字列%" `<br>
"**NULLデータ**"  を取得したい時に用いる`列名 is NULL` などがある。<br>
LIKE演算子における `%` はワイルドカードである。
#### 並べ替え
WHERE の後ろに `ORDER BY 列名 並べ方` を置くことで並べ替えができる。<br>
**昇順**の時は`ASC` , **降順**の時は`DESC`を並べ方の場所に代入する。
#### 最大数の指定
WHERE , ORDER BY の後ろに `LIMIT 自然数` を置くことで**取得するデータの最大数**を指定することができる。<br>
また下のように ORDER BY と LIMIT を組み合わせることで "**上位3位のデータ**" を取得することができる。
```
SELECT *
FROM 表名
WHERE 条件
ORDER BY 列名 DESC
LIMIT 3;
```
#### 集計関数
特定の列に対して `SELECT 関数名(列名)` の形で集計をする関数が存在する。以下にまとめる。
|関数名|機能|
|:---:|:---:|
|DISTICT|重複を省く|
|SUM|合計を計算|
|AVG|平均を計算|
|COUNT|データの個数を計算|
|MAX/MIN|最大/最小を計算|
#### グループ化
`GROUP BY 列名` でデータをグループ化することができる。<br>
グループを行う際は下のように SELECT には **GROUP BY で指定している列名** と **集計関数** しか来ない。
```
SELECT SUM(列名1),列名2,列名3
FROM 表名
WHERE 条件
GROUP BY 列名2,列名3;
```
#### グループ化から更なる絞り込み
`HAVING 条件` でグループ化後に更なる絞り込みを行うことができる。<br>
グループ化後に絞り込みを行う特性から下のように **SELECT にある列名** しか条件に来ない。
```
SELECT SUM(列名1),列名2
FROM 表名
GROUP BY 列名2
HAVING SUM(列名1)>1000;
```
#### サブクエリ
例えば WHERE の後ろの条件の中で集計関数の結果等の **クエリで取得したデータ** を使いたいことがある。  
このとき2つ以上のクエリを1つに纏めることができる。
```
SELECT 列名1
FROM 表名
WHERE 列名2 > (
  SELECT AVG(列名2)
  FROM 表名
  WHERE 条件;
)
```
#### 結合
表1の **外部キー** と表2の **主キー** を紐づけることで2つの表を結合することができる。  
2つの表に同じ名前の列があるときは SELECT をするときに注意が必要である。
```
SELECT 表名1.列1, 表名2.列1
FROM 表名1
JOIN 表名2
ON 表名1.外部キー=表名2.主キー;
```
**外部キーに NULL があるとき、その行は取得されないので注意が必要である。**  
外部キーに NULL を持つ行も取得したい時は下のようにする。
```
SELECT 表名1.列1, 表名2.列1
FROM 表名1
LEFT JOIN 表名2
ON 表名1.外部キー=表名2.主キー;
```
3つ以上の表を結合したい時は、 JOIN と ON を下に付け足すようにする。
# DML(データの挿入、更新、削除)
#### データの挿入
```
INSERT INTO 表名(列1,列2, … )
VALUES(データ1,データ2 … );
```
多くの表の主キーでは AUTO INCREMENT (後述) が使われているため、値を入力しなくてよい(ときが殆どである)。
#### データの更新
```
UPDATE 表名
SET 列名1=データ1
WHERE 条件;
```
多くの場合、条件で主キーの値を指定して、更新を行う。
#### データの削除
```
DELETE FROM 表名
WHERE 条件;
```
データの更新時と同じく条件で主キーの値をしていする。
# DDL
#### データベースの作成
```
CREATE DATABASE データベース名;
SHOW databases;
```
#### テーブルの作成
```
USE データベース名;
CREATE TABLE 表名(列名 データ型 [オプション],
 …
PRIMARY KEY(列名1),
FOREIGN KEY(列名2) REFERENCES 他の表(他の表の列1))
DEFAULT CHARSET=utf8;

SHOW tables;
DESCRIBE 表名;    # 表のテーブル構造を表示
```
主なデータ型は以下の通り。
||データ型|
|:---:|:---:|
|INT|整数型(4バイト)|
|FLOAT|浮動小数点型(単精度)|
|DOUBLE|浮動小数点型(倍精度)|
|VARCHAR|可変長の文字列|
|TEXT|長い文字列|
|BOOLEAN|ブール|
|DATE|日付型|
|DATETIME|日付時刻型|

主なオプションは以下の通り。

|オプション|機能|
|:---:|:---:|
|AUTO INCREMENT|列を増やすと自動で<br>インクリメントされる|
|NOT NULL|NULLを許さない|
|UNIQUE|列の値の重複を許さない|
|DEFAULT 値|デフォルト値の設定|
|CHECK(列 条件)|条件に合わないデータを許さない|
#### テーブル、データベースの削除
```
DROP TABLE 表名;
DROP DATABASE データベース名;
```
#### 列(カラム)の追加
```
ALTER TABLE 表名 ADD COLUMN 列名 データ型;
```
#### 列名の変更
```
ALTER TABLE 表名 CHANGE COLUMN 旧列名 新列名 データ型; 
```
#### 列の削除
```
ALTER TABLE 表名 DROP COLUMN 列名;
```
# その他
#### MySQLの起動、ログイン
```
net start mysql57
mysql --user=root --password // mysql -uroot
```
#### MySQLのログアウト、停止
```
exit;
net stop mysql57
```
#### CSVファイルの書き出し
```
SELECT * FROM テーブル名 
INTO OUTFILE '/tmp/example.csv' // 書き出すディレクトリのパス
CHARACTER SET 'utf8'
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"';
```
参考</br>
https://urashita.com/archives/25205?utm_source=pocket_reader
#### CSVファイルをインポート
```
LOAD DATA LOCAL INFILE '/tmp/examle.csv' // CSVファイルを保管したディレクトリまでのパス
INTO TABLE テーブル名
FIELDS TERMINATED BY ','
ENCLOSED BY '"';
```
参考</br>
https://qiita.com/oden141/items/239a7ce3cfe3197a3ba7

※文字化けが起こるとき
1. CSVファイルをメモ帳で開く
2. 名前を付けて保存 → エンコード : UTF-8 (BOM付き)
3. MySQLにて下記のSQL文を打つ
```
set character_set_database=utf8;
```