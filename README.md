いろいろなものを置いておきます。  
  
Hefeweizen_botsu  
├ Hefeweizen-2020_botsu.zip  
│　 WCSOC用に作ってボツになったNNUE標準型の評価関数。（そんなに弱くないと思うんだけどなぁ……^^;）  
│  
Hefeweizen-HKPE9  
├ Hefeweizen-HKPE9-avx2.exe  
│　 NNUEのHalfKPE9型の評価関数用の実行バイナリ（AVX2以降用）  
│　 yunyun0419さんのブランチmがマージされています。強いそうです……。（自分では検証が足りない）  
│  
├ Hefeweizen-HKPE9-sse42.exe  
│　 NNUEのHalfKPE9型の評価関数用の実行バイナリ（SSE4.2以降用）  
│　 yunyun0419さんのブランチmがマージされています。強いそうです……。（自分では検証が足りない）  
│  
├ Hefeweizen-HKPE9-learn-avx2.exe  
│　 NNUEのHalfKPE9型の評価関数用の学習用実行バイナリ（AVX2以降用）  
│　 yunyun0419さんのブランチmをマージし、その探索部を使用して教師局面を生成できるようにしました。  
│  
├ Hefeweizen-HKPE9-learn-sse42.exe  
│　 NNUEのHalfKPE9型の評価関数用の学習用実行バイナリ（SSE4.2以降用）  
│　 yunyun0419さんのブランチmをマージし、その探索部を使用して教師局面を生成できるようにしました。  
│  
├ Hefeweizen-HKPE9_m_src.zip  
│　 上記のソースファイルです。  
│  
JKishi18gou_tttak_merge  
├ JKishi18gou_tttak_merge.zip  
│　 人造棋士18号にtttakさんのNNUEのいろいろ評価関数のブランチをマージしたソースファイルです。  
│　 tournamentビルドはtttakさんの元ブランチと変わりませんが、evallearnビルドは教師データを1万局面から学習可能とし、  
│　 学習経過のログをCSV形式で出力するようにしていて、集計しやすくしています。  
│  
├ JKishi18gou_HKPKSDG_avx2.exe  
│　 NNUEのHalfKP-KingSfety-DestinguishGolds型の評価関数用の対局用WindowsバイナリのAVX2版です。  
│  
├ JKishi18gou_HKPKSDG_sse42.exe  
│　 NNUEのHalfKP-KingSfety-DestinguishGolds型の評価関数用の対局用WindowsバイナリのSSE4.2版です。  
│  
├ JKishi18gou_HKPKSDG_learn_avx2.exe  
│　 NNUEのHalfKP-KingSfety-DestinguishGolds型の評価関数用の学習用WindowsバイナリのAVX2版です。  
│  
├ JKishi18gou_HKPKSDG_learn_sse42.exe  
│　 NNUEのHalfKP-KingSfety-DestinguishGolds型の評価関数用の学習用WindowsバイナリのSSE4.2版です。  
│  
├ JKishi18gou_HKPKSDG_sample.zip  
│　 HalfKP-KingSfety-DestinguishGolds型の評価関数にKristallweizenから生成した教師局面約1億局面から学習させた  
│　 サンプルです。  
│  
JKishi18gou_m  
├ JKishi18gou_m.zip  
│　 mブランチビルドした標準NNUE用の実行バイナリと、水匠2とHefeweizen-2929を線形マージして作り上げた評価関数、  
│　 tttakさんのいろいろ評価関数のmブランチを人造棋士18号にマージしたソースファイルの一式です。  
│　 実行バイナリはmsys2-clangでビルドしているので、実行は高速だと思います。水匠2にもこれが使えます。  
│　 評価関数もかなりイケてるはずです。  
│  
│　 2020/06/11追記  
│  
│　 やねうら王V4.91をマージしたWindowsバイナリを作成したので配布します。  
│　 軽い動作検証は行いましたが、パフォーマンス検証までは行っていません。速くなったかどうかはわかりません。w  
│  
│　 2020/06/13追記  
│  
│　 ソース一式は人造棋士18号のソースリポジトリに「18gou_m」というブランチを作成してそちらにアップするように  
│　 しました。  
│  
├ eval200512.zip  
│　 線形マージの際の主従関係を反対にし（水匠2が主）、6:4の割合でマージしたバージョンの評価関数です。  
│  
book  
├ floodgate.db  
│　 Floodgateの2020年1月1日～9月5日の対局で、レーティングが3900以上同士の対局の勝局をそのままやねうら王の  
│　 定跡ファイルにしたものを配布します。  
│　 やねうら王エンジンの定跡フォルダにコピーし、定跡ファイルに「floodgate.db」を指定してご利用ください。  
│  
tools  
├ sel_hirate.zip  
│　 将棋俱楽部24の棋譜から、平手の棋譜を抽出するPythonスクリプトです。  
│  
├ senkei.zip  
│　 CSA形式の棋譜から戦型と囲いを判別するPythonスクリプトです。  
│　 まだまだ改良の余地があると思うので、みんなで作っていけたらなぁと思っています。  
│  
├ senkei_api.zip  
│　戦型判別スクリプトをPHPからコールするためのサンプルをつけたセットです。  
│　実行にはpython-shogiが必要ですので、事前にインストールしておいてください。  
│  
temp  
└ JKishi18gou_n.zip  
　　JKishi18gouにmブランチを取り込み方をちょっと変えたバージョンです。JKishi18gou_mよりは安定しています。  
  
  
ボツ版については、https://github.com/Tama4649/Kristallweizen/ の実行バイナリを使用する場合は、そのままevalフォルダに  
解凍後得られたbeer.binファイルを入れてください。  
うちの実行バイナリでない場合は、ファイル名をbeer.binからnn.binに変更して入れてください。  
  
HKPE9型については、評価関数ファイル名をnn.binをbeer.binに変更してevalフォルダに入れてください。  
