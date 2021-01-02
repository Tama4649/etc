いろいろなものを置いておきます。  
  
Hefeweizen_botsu  
├ Hefeweizen-2020_botsu.zip  
│　WCSOC用に作ってボツになったNNUE標準型の評価関数。  
│　（そんなに弱くないと思うんだけどなぁ……^^;）  
│  
Hefeweizen-HKPE9  
├ Hefeweizen-HKPE9-avx2.exe  
│　NNUEのHalfKPE9型の評価関数用の実行バイナリ（AVX2以降用）  
│　yunyun0419さんのブランチmがマージされています。強いそうです……。  
│　（自分では検証が足りない）  
│  
├ Hefeweizen-HKPE9-sse42.exe  
│　NNUEのHalfKPE9型の評価関数用の実行バイナリ（SSE4.2以降用）  
│　yunyun0419さんのブランチmがマージされています。強いそうです……。  
│　（自分では検証が足りない）  
│  
├ Hefeweizen-HKPE9-learn-avx2.exe  
│　NNUEのHalfKPE9型の評価関数用の学習用実行バイナリ（AVX2以降用）  
│　yunyun0419さんのブランチmをマージし、その探索部を使用して教師局面を生成できる  
│　ようにしました。  
│  
├ Hefeweizen-HKPE9-learn-sse42.exe  
│　NNUEのHalfKPE9型の評価関数用の学習用実行バイナリ（SSE4.2以降用）  
│　yunyun0419さんのブランチmをマージし、その探索部を使用して教師局面を生成できる  
│　ようにしました。  
│  
├ Hefeweizen-HKPE9_m_src.zip  
│　上記のソースファイルです。  
│  
JKishi18gou_tttak_merge  
├ JKishi18gou_tttak_merge.zip  
│　人造棋士18号にtttakさんのNNUEのいろいろ評価関数のブランチをマージしたソース  
│　ファイルです。tournamentビルドはtttakさんの元ブランチと変わりませんが、evallearn  
│　ビルドは教師データを1万局面から学習可能とし、学習経過のログをCSV形式で出力する  
│　ようにしていて、集計しやすくしています。  
│  
├ JKishi18gou_HKPKSDG_avx2.exe  
│　NNUEのHalfKP-KingSfety-DestinguishGolds型の評価関数用の対局用Windowsバイナリの  
│　AVX2版です。  
│  
├ JKishi18gou_HKPKSDG_sse42.exe  
│　NNUEのHalfKP-KingSfety-DestinguishGolds型の評価関数用の対局用Windowsバイナリの  
│　SSE4.2版です。  
│  
├ JKishi18gou_HKPKSDG_learn_avx2.exe  
│　NNUEのHalfKP-KingSfety-DestinguishGolds型の評価関数用の学習用Windowsバイナリの  
│　AVX2版です。  
│  
├ JKishi18gou_HKPKSDG_learn_sse42.exe  
│　NNUEのHalfKP-KingSfety-DestinguishGolds型の評価関数用の学習用Windowsバイナリの  
│　SSE4.2版です。  
│  
├ JKishi18gou_HKPKSDG_sample.zip  
│　HalfKP-KingSfety-DestinguishGolds型の評価関数にKristallweizenから生成した教師局面  
│　約1億局面から学習させたサンプルです。  
│  
JKishi18gou_m  
├ JKishi18gou_m.zip  
│　mブランチビルドした標準NNUE用の実行バイナリと、水匠2とHefeweizen-2929を線形マージ  
│　して作り上げた評価関数、tttakさんのいろいろ評価関数のmブランチを人造棋士18号に  
│　マージしたソースファイルの一式です。  
│　実行バイナリはmsys2-clangでビルドしているので、実行は高速だと思います。水匠2にも  
│　これが使えます。  
│　評価関数もかなりイケてるはずです。  
│  
│　2020/06/11追記  
│  
│　やねうら王V4.91をマージしたWindowsバイナリを作成したので配布します。  
│　軽い動作検証は行いましたが、パフォーマンス検証までは行っていません。速くなったか  
│　どうかはわかりません。w  
│  
│　2020/06/13追記  
│  
│　ソース一式は人造棋士18号のソースリポジトリに「18gou_m」というブランチを作成して  
│　そちらにアップするようにしました。  
│  
├ eval200512.zip  
│　線形マージの際の主従関係を反対にし（水匠2が主）、6:4の割合でマージしたバージョンの  
│　評価関数です。  
│  
book  
├ floodgate.db  
│　Floodgateの2020年1月1日～12月12日の対局で、レーティングが3900以上同士の対局の勝局を  
│　そのままやねうら王の定跡ファイルにしたものを配布します。  
│　やねうら王エンジンの定跡フォルダにコピーし、定跡ファイルに「floodgate.db」を指定して  
│　ご利用ください。  
│  
│　2020/11/24  
│  
│　新たに生成したところ、ファイルサイズが50MBを超えてしまったため、そのままだとアップ  
│　できないため、FGbook.zipとしてZIP圧縮しました。解凍してご利用ください。  
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
├ nnuetool.py  
│  HalfKP 256x2-32-32の標準的なNNUEの評価関数の値を直接いじるPythonスクリプトです。  
│  NNUEのデータ構造や、値の変化が及ぼす影響度を理解していないと使えないです。ゴミを量産するだけです。w  
│  動作にはnumpyが必要です。入ってない人はpipでインストールしてください。  
│  自分のLinux環境(Python3.6以上)でしか実行してませんので、動作環境に対する質問等はお受けできません。  
│  48先生のブログ(https://bleu48.hatenablog.com/entry/2019/05/18/132808) を参考にして、自分なりにわかりやすく  
│  まとめたつもりです。  
│  
├ hkp2hkpe9.py  
│　HalfKP 256x2-32-32の評価関数をHalfKPE9の評価関数に変換するスクリプトです。Python3.6以降で動くと思います。  
│　python3 hkp2hkpe9.py [HalfKPファイルパス] [HalfKPE9ファイルパス] で動きます。  
│　(Windowsの場合は、python3 を py に置き換えて実行してください)  
│　利きの9個分に、HalfKPの層をそのままコピーしていますので、HalfKPと同じ手を指すと思います。  
│　せっかく作ってきた資産ですもの。有効に活用していきましょう！(o^-')b  
│  
├ JKishi18gou_set.zip  
│　あんまり詳しくない方でもお手軽に将棋AIが利用できるように、エンジン、評価関数、定跡ファイルを1セットにした  
│　お気楽セットを作りました。(^-^)  
│　詳しくは解凍後のフォルダにある、最初にお読みください.txtを参照願います。  
│  
├  copypaste.py  
│　やねうらおさん(@yaneuraou)のクリスマスプレゼントの詰め問題集を楽しむために、Enterキーを押すだけで局面を  
│　順次クリップボードにコピーするだけの簡単なスクリプトを作ってみました。  
│　Python3以降で動作します。ライブラリはpyperclipを使っています。  
│　やねさんの問題集を解凍したフォルダと同じところにこのスクリプトを配置して、以下のような手順で使います。  
│　(Windowsを想定)  
│  
│  ・コマンドプロンプトを開く  
│　・cd /d (このスクリプトが保存されているフォルダパス)  
│　・py -m pip install -U pip  
│　・py -m pip install pyperclip  
│　・py copypaste.py [SFENファイル名]  
│　・「Enterを押して！」と表示されるので、Enterキーを押す。  
│　・「局面をコピーしたよ。ShogiGUIに貼ってね！」と表示されるので、ShogiGUIの画面でCtrl+Vを押す。  
│　・ShogiGUIには問題局面が表示されるので、頑張って解く！  
│　・解けたらコマンドプロンプト画面に戻り、Enterキーを押す。  
│　・ShogiGUI画面でCtrl+Vを押す。  
│　・以下繰り返し  
│  
temp  
├ JKishi18gou_n.zip  
│　JKishi18gouにmブランチを取り込み方をちょっと変えたバージョンです。JKishi18gou_mよりは安定しています。  
│  
├ tsec_20201231.zip  
│　2020/12/30～31に行われた世界将棋AI電竜戦TSECの対局棋譜をごっそりダウンロードしたものを置いておきます。  
│　ほしい方はご自由にどうぞ。  
│  
eval  
├ JKishi18gou_20200815.zip  
│　第1回電竜戦の後の打ち上げの時の余興で、大会に参加しようとして作成した評価関数でテスト対局をしてみたところ、  
│　そこそこおもしろい対局をしてくれたので、ネタとして公開します。  
│　やねうら王の標準的なNNUE構成（HalfKP-256x2-32-32）で利用できる評価関数ファイルです。  
│　やねうら王のevalフォルダにコピーしてお使いください。  
│　これは、たややんさん（@tayayan_ts）の水匠2を拙作のnnuetool.pyで評価値を操作して評価値を均すことにより、  
│　多様な手を指すことを目的として作成しました。  
│　ですので、水匠2より強くなっていることはないのですが、意外な手を指すことにより一発パンチを食らわせることが  
│　できたりします。(^-^)  
│　興味がある奇特な方がいらっしゃいましたらどうぞ。^^  
│  
├ JKishi18gou_20201129.zip  
│　JKishi18gou_20200815.zipの評価関数に、拙作のnnuetool.pyでBURNUNG BRIDGESの評価関数をマージしたものです。  
│　いい具合にとんがりが丸まって、より汎用性のある評価関数になりました。(^-^)  
│　Floodgateで放流しているJKシリーズや将棋倶楽部24で稼働しているJKishi18gou、Hefeweizenは、皆この評価関数で  
│　動作しています。リソースをお持ちの方に検証していただけたら幸いです。  
│  
├ JKishi18gou_20210101.zip  
│　新年のお年玉として、2020/12/30～31に行われた、世界将棋AI電竜戦TSECファイナルで優勝したBURNING BRIDGES……  
│　の前に公開されたバージョンｗと、同大会のBリーグ優勝の水匠3がフュージョンしたらどうなるか？ということで、  
│　拙作のnnuetool.pyでキメラッタしてみた評価関数を公開します。    
│　現在、depth24 or 3000万ノードで水匠3と検証対局中ですが、6局やってまだ負けてないし、勝負所でしっかり逆転を  
│　キメたりしているので、悪くはなさそうです。^^    
│　お正月の暇つぶしに検証対局も悪くないですヨ♪   
│  
├ JKishi18gou_20210102.zip  
│　ホンマもんの電竜BURNING BRIDGESが公開されましたので、無条件にフュージョン素材を差し替えたものです。  
│　現在、depth24 or 3000万ノードで素材元のBURNING_BRIDGEと検証対局中ですが、ちとビミョ～です。ｗ  
│　使うならJKishi18gou_20210101.zipのほうがいいかも。^^;   
│  
└ YaneuraOu_Mate  
　　やねうら王詰将棋ルーチンが公開になったので、いち早く使ってみたい方もおられると思いますので、Windowsバイナリを  
　　配布します。  
  
  
ボツ版については、https://github.com/Tama4649/Kristallweizen/ の実行バイナリを使用する場合は、そのままevalフォルダに  
解凍後得られたbeer.binファイルを入れてください。  
うちの実行バイナリでない場合は、ファイル名をbeer.binからnn.binに変更して入れてください。  
  
HKPE9型については、評価関数ファイル名をnn.binをbeer.binに変更してevalフォルダに入れてください。  
