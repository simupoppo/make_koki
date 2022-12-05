# make_koki
## Flexible container loading position set
This programs make you to load container flexibly.
This programs for making pak128.japan addon only! (Not for pak128!).
If you want to use in pak128, please change container figures and some parameters in the program such as freight and top/end length.

## contents

- src  
  - koki_a.png  
  - koki_b.png  
  - koki_c.png   
  - koki_d.png   
  - koki_e.png  
- input.txt (input parameters. If you want to skip writting in terminal, please use it.)  
- make_koki.exe (program file)
- make_koki_ja.exe (program file for japanese)
- make_koki.py (python program)  
- make_koki_ja.py (python program for japanese. UTF-8)  
- make_koki.bat (for windows. SHIFT-JIS.)

## How to use

### Before use
0-1. Put the container track vehicle empty image in the same directory as the programs. Vehicle Empty Image must be drawn in First line (kokiXXX.0.n)! 
0-2. If you put Makeobj in the same directory, you can make not only dat file but also pak file by using "make_koki.bat". 

### Use

1. Input "make_koki.bat" in terminal.
2. After choosing the language, input the car_name, copyright, imagefile-name, length, container-loading number(not available), top speed, cost of the car, running cost of the car,weight of the car, intro_year, retire_year,and container-loading length (top and end).

Vehicle Empty Image must be drawn in First line (kokiXXX.0.n)!

If you use only make_koki.exe, only the dat file is made. If you want to edit dat files, please do.

You can skip input phase by using "input.txt". Please write input.txt before usinig program and answer the car_name by "isfile" while running program. 


# make_koki_japanese

## コンテナ自由積載セット

本フォルダはコンテナを自由自在に編成内で積み替えられるpakの作成を支援します。
注意:ここで使用している画像はpak128.japan専用です。pak128等ほかのサイズで使用する場合は画像をご用意いただき、適宜差し替えてください。また、連結位置や貨物の種類についても変更する必要があります。

## 同梱物

- src  
  - koki_a.png  
  - koki_b.png  
  - koki_c.png   
  - koki_d.png   
  - koki_e.png  
- input.txt (プログラムのパラメータが記入されています。コマンドプロンプトでの入力を省略できます。コマンドプロンプトを使用しない場合は不要です。)  
- make_koki.exe (プログラム)
- make_koki_ja.exe (日本語版プログラム)
- make_koki.py (プログラムのソースコード。python環境で起動します。)   
- make_koki_ja.py (日本語版プログラムのソースコード。python環境で起動します。UTF-8で記述。ja_kokiXXX.tabも作成します(kokiXXXは車両名)。)  
- make_koki.bat (windows環境で起動します。SHIFT-JIS)

## 使用方法

本ファイルと同じディレクトリに空のコンテナ貨車の画像とmakeobjをご用意ください。貨車の画像は必ずpngファイルの1行目に配置してください!
起動にはpython環境が必要ですので、インストールしてください。python3.11で起動確認済みです。
また、pythonファイルは単独でご使用いただけますが、同封しているバッチファイルをご使用いただける場合pak化まで自動で行われます。Windows 11 Home Edditionで起動確認済みです。

### バッチファイルを使用する場合

1. コマンドプロンプトで本ディレクトリを指定
2. コマンドプロンプトでmake_koki.batと入力しエンター
3. 表示に従って貨車名、著者名、貨車のpngファイル名(.pngは不要)、貨車の長さ、貨車の積めるコンテナ数、貨車の最高速度、貨車の購入費用、貨車の運行費用、貨車の重量、貨車の登場年、貨車の引退年、コンテナを積むことができる位置(はじめ、終わり)、貨車の日本語名(日本語版のみ)を入力してください。
以上の入力完了後、自動でpak化されます。ただし、画像がない場合やmakeobjがない場合はdatファイルのみが作成されます。

### datのみを生成する場合

1. コマンドプロンプトまたはターミナルで make_koki_ja.exe と入力。または make_koki_ja.exe をダブルクリック等で起動
2. 表示に従って貨車名、著者名、貨車のpngファイル名(.pngは不要)、貨車の長さ、貨車の積めるコンテナ数、貨車の最高速度、貨車の購入費用、貨車の運行費用、貨車の重量、貨車の登場年、貨車の引退年、コンテナを積むことができる位置(はじめ、終わり)、貨車の日本語名(日本語版のみ)を入力してください。
以上の入力完了後、自動でdatファイルが生成されます。

### 改造等でpythonを使用する場合

1. コマンドプロンプトまたはターミナルで python make_koki.py または python make_koki_ja.py と入力
2. バッチファイルを使用する場合3.と同様に入力
以上の入力完了後、datファイルが出力されます。


なお、コマンドプロンプトでの入力が面倒な場合、同梱のinput.txtに上記の内容を上から順に各行に入力することでdat化(バッチファイルからの場合pak化)を自動化できます。貨車名を聞かれた際に"isfile"と入力してください。input.txtの内容に従って自動でdatが記述されます(日本語版の場合は日本語のみコマンドプロンプト,ターミナル上で入力する必要があります)。

## 謝辞/Special thanks

pak化に用いた画像は大ぼけ様のコキ100系のコンテナをもとに作成しております。
この場を借りてお礼申し上げます。


## 改造,再配布について

画像については改造が可能となっております。
プログラムにつきましてはご自由に改造/再配布してください。

## 免責事項

本プログラムおよび添付ファイルのダウンロード、インストール、起動等により発生した損失に関しましては、当方では責任を負いかねます。

使用は自己責任でお願いいたします。

# release note

2022.11.14 ver 0.0 作成:コンテナ数指定に未対応、input.txt入力での動作を確認済み  
2022.11.23 ver 0.1 コンテナの積む範囲の指定に対応、車掌室のついた貨車(コキフ)に対応可能、日本語化対応(自動ja.tab生成機能付き)  
2022.11.24 ver 0.1 公開
2022.11.25 ver 1.0 make_koki.exe, make_koki_ja.exe作成、python環境なしでも作成可能に
