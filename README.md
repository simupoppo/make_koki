# make_koki
〇 Flexible loading position set.
This programs make you to load container flexibly.
This programs for making pak128.japan addon only! (Not for pak128!).

・contents
src
 koki_a.png
 koki_b.png
 koki_c.png
 koki_d.png
 koki_e.png
make_koki.py (python program)
make_koki_ja.py (python program for japanese. UTF-8)
make_koki.bat (for windows. SHIFT-JIS.)

・How to use
Before use
0-1. Put the container track vehicle empty image in the same directory as the programs.
0-2. Installing python.
0-3. If you put Makeobj in the same directory, you can make not only dat file but also pak file by using "make_koki.bat". 

Use
1. Input "make_koki.bat" in terminal.
2. After choosing the language, input the car_name, copyright, length, container-loading number(not available), top speed, cost of the car, running cost of the car,weight of the car, intro_year, retire_year,and container-loading length (top and end).

If you use only python file, only the dat file is made. Please make pak by using makeobj.




# make_koki_japanese

〇コンテナ自由積載セット
本フォルダはコンテナを自由自在に編成内で積み替えられるpakの作成を支援します。
注意:ここで使用している画像はpak128.japan専用です。pak128等ほかのサイズで使用する場合は画像をご用意いただき、適宜差し替えてください。

・同梱物
src
 koki_a.png
 koki_b.png
 koki_c.png
 koki_d.png
 koki_e.png
make_koki.py (プログラム。python環境で起動します。) 
make_koki_ja.py (日本語版プログラム。python環境で起動します。UTF-8で記述。ja_kokiXXX.tabも作成します(kokiXXXは車両名)。)
make_koki.bat (windows環境で起動します。SHIFT-JIS)

・使用方法
本ファイルと同じディレクトリに空のコンテナ貨車の画像とmakeobjをご用意ください。
起動にはpython環境が必要ですので、インストールしてください。python3.11で起動確認済みです。
また、pythonファイルは単独でご使用いただけますが、同封しているバッチファイルをご使用いただける場合pak化まで自動で行われます。Windows 11 Home Edditionで起動確認済みです。

バッチファイルを使用する場合
1.コマンドプロンプトで本ディレクトリを指定
2.コマンドプロンプトでmake_koki.batと入力しエンター
3.表示に従って貨車名、著者名、貨車のpngファイル名(.pngは不要)、貨車の長さ、貨車の積めるコンテナ数、貨車の最高速度、貨車の購入費用、貨車の運行費用、貨車の重量、貨車の登場年、貨車の引退年、コンテナを積むことができる位置(はじめ、終わり)、貨車の日本語名(日本語版のみ)を入力してください。
以上の入力完了後、自動でpak化されます。ただし、画像がない場合やmakeobjがない場合はdatファイルのみが作成されます。

pythonのみを使用する場合
1.コマンドプロンプトまたはターミナルでpython make_koki.pyと入力
2.バッチファイルを使用する場合3.と同様に入力
以上の入力完了後、datファイルが出力されます。


なお、コマンドプロンプトでの入力が面倒な場合、同梱のinput.txtに上記の内容を上から順に各行に入力することでdat化(バッチファイルからの場合pak化)を自動化できます。
・謝辞
pak化に用いた画像は大ぼけ様のコキ100系のコンテナをもとに作成しております。
この場を借りてお礼申し上げます。


・改造/再配布について
画像については改造が可能となっております。
プログラムにつきましてはご自由に改造/再配布してください。

#release note
2022.11.14 ver 0.0 作成:コンテナ数指定に未対応、input.txt入力での動作を確認済み
2022.11.23 ver 0.1 コンテナの積む範囲の指定に対応、車掌室のついた貨車(コキフ)に対応可能、日本語化対応(自動ja.tab生成機能付き)
