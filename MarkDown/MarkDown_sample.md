# Markdown記法 サンプル
### INDEX
* [見出し](#見出し)  
* [箇条書きリスト](#箇条書きリスト)  
* [番号付きリスト](#番号付きリスト)  
* [引用](#引用)  
* [コードの挿入(1行)](#コードの挿入(1行))
* [コードの挿入(ブロック)](#コードの挿入(ブロック))
* [強調](#強調)
* [取り消し線](#取り消し線)
* [水平線](#水平線)
* [リンク](#リンク)
* [ページ内リンク](#ページ内リンク)
# 見出し
### 記述 
```
# 見出し1
## 見出し2
### 見出し3
#### 見出し4
##### 見出し5
```
### 表示
# 見出し1
## 見出し2
### 見出し3
#### 見出し4
##### 見出し5
# 箇条書きリスト
ハイフン、プラス、アスタリスクのいずれかを用いて記述することができる。
### 記述
```
* リスト1
  * リスト1-1
  - リスト1-2
    * リスト1-2-1
+ リスト2
```
### 表示
* リスト1
  * リスト1-1
  - リスト1-2
    * リスト1-2-1
+ リスト2
# 番号付きリスト
### 記述
```
1. リスト1
    1. リスト1-1  
    1. リスト1-2     
1. リスト2  
```
### 表示    
1. リスト1
    1. リスト1-1  
    1. リスト1-2     
1. リスト2  
# 引用
### 記述
```
> こんにちは。
>> こんにちは。<br>
>> また会いましたね。
>
> 本当ね。
```
\<br>で改行を行うことができる。
### 表示
> こんにちは。
>> こんにちは。<br>
>> また会いましたね。
>
> 本当ね。
# コードの挿入(1行)
### 記述
```
Pythonでは`print("Hello,world!")`のようにして出力を行います。
```
### 表示
Pythonでは`print("Hello,world!")`のようにして出力を行います。
# コードの挿入(ブロック)
### 記述
~~~
```
for i in range(10):
    print(i)
```
```python
for i in range(10):
    print(i)
```
~~~
**バッククォート (`)** の代わりに**チルダ (~)** を用いることもできる。
### 表示
```
for i in range(10):
    print(i)
```
**バッククォート3つの後ろに言語名を記述する**ことで視覚的に見やすくすることができる。
```python
for i in range(10):
    print(i)
```
# 強調
アスタリスクの代わりにアンダースコアを用いても良い。
### 記述
```
nomal **bold** nomal  
nomal *italic* nomal  
nomal ***bold*** nomal  
```
### 表示
nomal **bold** nomal  
nomal *italic* nomal  
nomal ***bold*** nomal  
# 取り消し線
### 記述
```
~~取り消し線~~
```
### 表記
~~取り消し線~~
# 水平線
アスタリスクの代わりにアンダースコア、ハイフンを用いても良い。
### 記述
```
***
```
### 表示
***
# リンク
### 記述
```
[Gooleのページに飛ぶ](https://www.google.co.jp)
```
### 表示
[Gooleのページに飛ぶ](https://www.google.co.jp)
# ページ内リンク
### 記述
```
[引用](#引用)
```
[引用](#引用)