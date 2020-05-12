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
tools  
└ sel_hirate.zip  
　　 将棋俱楽部24の棋譜から、平手の棋譜を抽出するpythonスクリプトです。  
  
  
ボツ版については、https://github.com/Tama4649/Kristallweizen/ の実行バイナリを使用する場合は、そのままevalフォルダに  
解凍後得られたbeer.binファイルを入れてください。  
うちの実行バイナリでない場合は、ファイル名をbeer.binからnn.binに変更して入れてください。  
  
HKPE9型については、評価関数ファイル名をnn.binをbeer.binに変更してevalフォルダに入れてください。  

