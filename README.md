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
└ Hefeweizen-HKPE9_m_src.zip  
　　 上記のソースファイルです。  
  
  
ボツ版については、https://github.com/Tama4649/Kristallweizen/ の実行バイナリを使用する場合は、そのままevalフォルダに  
解凍後得られたbeer.binファイルを入れてください。  
うちの実行バイナリでない場合は、ファイル名をbeer.binからnn.binに変更して入れてください。  
  
HKPE9型については、評価関数ファイル名をnn.binをbeer.binに変更してevalフォルダに入れてください。  

