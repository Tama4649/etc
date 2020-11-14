#!/home/tama/.pyenv/shims/python

# NNUEをいろいろいじる

import io, sys
import numpy  as np
import struct as st
import random as rn

# 値をゼロにする
def cmd_rn(a1):
    for i, r in enumerate(a1):
        a1[i] = 0

# 値をランダムに設定する
def cmd_rn(a1):
    rm = rn.randint(0, 32) - 16                                             # -16 ～ 16でランダム
    for i, r in enumerate(a1):
        if r != 0: a1[i] = rm                                               # 元の値が0じゃなかったらランダム値を設定する

# 評価値にノイズを乗せる
def cmd_an(a1):
    for i, r in enumerate(a1):
        rp = rn.randint(1, 100)
        if rp < 51:                                                         # 50%の確率で
            rm    = rn.randint(0, parc)                                     # 指定%までランダム
            par1  = rm / 100
            pm    = rn.randint(0, 1)
            # 指定％増減する
            v     = float(r * (1 - par1)) if pm == 0 else float(r * (1 + par1))
            a1[i] = int(v)

# 評価値の一律増加、低減
def cmd_eq(a1):
    par1 = parc / 100.0
    for i, r in enumerate(a1):
        v = float(int(r) * par1)                                            # 一律の増減率を掛ける
        a1[i] = int(v)

# 評価値のマージ
def cmd_mg(a1, a2):
    par1 = parc / 100.0
    par2 = (100.0 - parc) / 100.0
    for i, r in enumerate(a1):
        if   r     == 0: v = a2[i]                                          # 元が0なら右側の値を採用
        elif a2[i] == 0: v = r                                              # 右側が0なら元の値を採用
        else:            v = float(int(r) * par1 + int(a2[i]) * par2)       # 割合で按分
        a1[i] = int(v)
 
# 評価値のマージ（絶対値が大きいほうを左側とする）
def cmd_mgb(a1, a2):
    par1 = parc / 100.0
    par2 = (100.0 - parc) / 100.0
    for i, r in enumerate(a1):
        if   r     == 0: v = a2[i]                                          # 元が0なら右側の値を採用
        elif a2[i] == 0: v = r                                              # 右側が0なら元の値を採用
        else:
            v = float(int(r) * par1 + int(a2[i]) * par2) if r > a2[i] else float(int(a2[i]) * par1 + int(r) * par2)
        a1[i] = int(v)

# 評価値の取り込み
def cmd_fl(a1, a2):
    for i, r in enumerate(a1):
        v = a2[i] if r == 0 else r                                          # 元が0なら右側の値を採用
        a1[i] = v

# 評価値の転移学習
def cmd_tr(a1, a2):
    for i, r in enumerate(a1):
        if r == 0: v = a2[i]                                                # 元が0なら無条件で右を採用（未学習部分の取り込み）
        elif abs(r) == abs(a2[i]):                                          # 絶対値が同じなら
            v = r if r > a2[i] else a2[i]                                   # 正のほうを採用（居飛車の評価を潰さないため）
        else: 
            v = r if abs(r) > abs(a2[i]) else a2[i]                         # 絶対値が大きいほうを採用（学習が進んでいるほうを採るため）
        a1[i] = v

# パラメータ初期値
cmd  = "mg"
parc = 50.0
ifn1 = "eval/nn.bin"
ifn2 = "eval/suisho2/nn.bin"
ofn  = "eval/nn.bin"

# メイン処理
args  = sys.argv
argc  = len(args)
cmds  = [ "eq", "eq2", "is", "h1", "h2", "os", "mg", "mg2", "mgb", "fl", "tr", "an", "an2", "an3", "rn", "w0" ]
cmds2 = [ "mg", "mg2", "mgb", "fl", "tr" ]

# コマンドパーサ
if argc < 2:
    print("nnuetool.py コマンド [割合%] [入力ファイル名1] [入力ファイル名2|出力ファイル名] [出力ファイル名]")
    exit()

cmd  = args[1]

if cmd not in cmds:
    print("コマンドエラー。eq,eq2,is,h1,h2,os,mg,mg2,mgb,fl,tr,an,an2,an3,rn,w0のいずれかです。")
    exit()

if argc > 2:
    parc = float(args[2])
if argc > 3:
    ifn1 = args[3]
if argc > 4:
    if cmd in cmds2:
        ifn2 = args[4]
    else:
        ofn  = args[4]
if argc > 5:
    if cmd in cmds2:                            # 出力ファイル名を壊されないように
        ofn = args[5]

# 評価関数ファイルの分解
nndata1  = open(ifn1, "rb").read()
nnlen1   = st.unpack_from("<I", nndata1, 8)[0]

# 各層のポインタオフセット
offset11 = 4 + 4 + 4 + nnlen1 + 4               # isb
offset21 = offset11 + 256 * 2                   # isw
offset31 = offset21 + 125388 * 256 * 2 + 4      # h1b
offset41 = offset31 + 32 * 4                    # h1w
offset51 = offset41 + 32 * 512                  # h2b
offset61 = offset51 + 32 * 4                    # h2w
offset71 = offset61 + 32 * 32                   # osb
offset81 = offset71 + 4                         # osw

# 各層の構造配列に取り込む
wk   = st.unpack_from("<" + str(256) + "h", nndata1, offset11)
isb1 = np.array(wk, dtype='i2').reshape(256)
wk   = st.unpack_from("<" + str(125388 * 256) + "h", nndata1, offset21)
isw1 = np.array(wk, dtype='i2').reshape(125388 * 256)
wk   = st.unpack_from("<" + str(32) + "i", nndata1, offset31)
h1b1 = np.array(wk, dtype='i4').reshape(32)
wk   = st.unpack_from("<" + str(32 * 512) + "b", nndata1, offset41)
h1w1 = np.array(wk, dtype='i1').reshape(32 * 512)
wk   = st.unpack_from("<" + str(32) + "i", nndata1, offset51)
h2b1 = np.array(wk, dtype='i4').reshape(32)
wk   = st.unpack_from("<" + str(32 * 32) + "b", nndata1, offset61)
h2w1 = np.array(wk, dtype='i1').reshape(32 * 32)
wk   = st.unpack_from("<" + str(1) + "i", nndata1, offset71)
osb1 = np.array(wk, dtype='i4').reshape(1)
wk   = st.unpack_from("<" + str(32 * 1) + "b", nndata1, offset81)
osw1 = np.array(wk, dtype='i1').reshape(32 * 1)

if cmd in cmds2:
    # 評価関数ファイルの分解
    nndata2  = open(ifn2, "rb").read()
    nnlen2   = st.unpack_from("<I", nndata2, 8)[0]
    # 各層のポインタオフセット
    offset12 = 4 + 4 + 4 + nnlen2 + 4           # isb
    offset22 = offset12 + 256 * 2               # isw
    offset32 = offset22 + 125388 * 256 * 2 + 4  # h1b
    offset42 = offset32 + 32 * 4                # h1w
    offset52 = offset42 + 32 * 512              # h2b
    offset62 = offset52 + 32 * 4                # h2w
    offset72 = offset62 + 32 * 32               # osb
    offset82 = offset72 + 4                     # osw
    # 各層の構造配列に取り込む
    wk   = st.unpack_from("<" + str(256) + "h", nndata2, offset12)
    isb2 = np.array(wk, dtype='i2').reshape(256)
    wk   = st.unpack_from("<" + str(125388 * 256) + "h", nndata2, offset22)
    isw2 = np.array(wk, dtype='i2').reshape(125388 * 256)
    wk   = st.unpack_from("<" + str(32) + "i", nndata2, offset32)
    h1b2 = np.array(wk, dtype='i4').reshape(32)
    wk   = st.unpack_from("<" + str(32 * 512) + "b", nndata2, offset42)
    h1w2 = np.array(wk, dtype='i1').reshape(32 * 512)
    wk   = st.unpack_from("<" + str(32) + "i", nndata2, offset52)
    h2b2 = np.array(wk, dtype='i4').reshape(32)
    wk   = st.unpack_from("<" + str(32 * 32) + "b", nndata2, offset62)
    h2w2 = np.array(wk, dtype='i1').reshape(32 * 32)
    wk   = st.unpack_from("<" + str(1) + "i", nndata2, offset72)
    osb2 = np.array(wk, dtype='i4').reshape(1)
    wk   = st.unpack_from("<" + str(32 * 1) + "b", nndata2, offset82)
    osw2 = np.array(wk, dtype='i1').reshape(32 * 1)

# コマンドの実行
if cmd == "eq":         # 一律の増減（バイアス、ウェイト両方）
    cmd_eq(isb1)
    cmd_eq(isw1)
    cmd_eq(h1b1)
    cmd_eq(h1w1)
    cmd_eq(h2b1)
    cmd_eq(h2w1)
    cmd_eq(osb1)
    cmd_eq(osw1)
elif cmd == "eq2":      # 一律の増減（ウェイトのみ）
    cmd_eq(isw1)
    cmd_eq(h1w1)
    cmd_eq(h2w1)
    cmd_eq(osw1)
elif cmd == "is":       # 一律の増減（入力層のウェイトのみ）
    cmd_eq(isw1)
elif cmd == "h1":       # 一律の増減（隠れ１層のウェイトのみ）
    cmd_eq(h1w1)
elif cmd == "h2":       # 一律の増減（隠れ２層のウェイトのみ）
    cmd_eq(h2w1)
elif cmd == "os":       # 一律の増減（出力層のウェイトのみ）
    cmd_eq(osw1)
elif cmd == "mg":       # マージ（バイアス、ウェイト全部）
    cmd_mg(isb1, isb2)
    cmd_mg(isw1, isw2)
    cmd_mg(h1b1, h1b2)
    cmd_mg(h1w1, h1w2)
    cmd_mg(h2b1, h2b2)
    cmd_mg(h2w1, h2w2)
    cmd_mg(osb1, osb2)
    cmd_mg(osw1, osw2)
elif cmd == "mg2":      # マージ（ウェイトのみ）
    cmd_mg(isw1, isw2)
    cmd_mg(h1w1, h1w2)
    cmd_mg(h2w1, h2w2)
    cmd_mg(osw1, osw2)
elif cmd == "mgb":      # マージ（バイアス、ウェイト全部）
    cmd_mgb(isb1, isb2)
    cmd_mgb(isw1, isw2)
    cmd_mgb(h1b1, h1b2)
    cmd_mgb(h1w1, h1w2)
    cmd_mgb(h2b1, h2b2)
    cmd_mgb(h2w1, h2w2)
    cmd_mgb(osb1, osb2)
    cmd_mgb(osw1, osw2)
elif cmd == "fl":       # 不足分取り込み（バイアス、ウェイト全部）
    cmd_fl(isb1, isb2)
    cmd_fl(isw1, isw2)
    cmd_fl(h1b1, h1b2)
    cmd_fl(h1w1, h1w2)
    cmd_fl(h2b1, h2b2)
    cmd_fl(h2w1, h2w2)
    cmd_fl(osb1, osb2)
    cmd_fl(osw1, osw2)
elif cmd == "tr":       # 大きい値のみ取り込み（バイアス、ウェイト全部）
    cmd_tr(isb1, isb2)
    cmd_tr(isw1, isw2)
    cmd_tr(h1b1, h1b2)
    cmd_tr(h1w1, h1w2)
    cmd_tr(h2b1, h2b2)
    cmd_tr(h2w1, h2w2)
    cmd_tr(osb1, osb2)
    cmd_tr(osw1, osw2)
elif cmd == "an":       # バイアス、ウェイトにノイズを乗せる
    cmd_an(isb1)
    cmd_an(h1b1)
    cmd_an(h2b1)
    cmd_an(osb1)
    cmd_an(isw1)
    cmd_an(h1w1)
    cmd_an(h2w1)
    cmd_an(osw1)
elif cmd == "an2":      # ウェイトにノイズを乗せる
    cmd_an(isw1)
    cmd_an(h1w1)
    cmd_an(h2w1)
    cmd_an(osw1)
elif cmd == "an3":      # 入力層以外のウェイトにノイズを乗せる
    cmd_an(h1w1)
    cmd_an(h2w1)
    cmd_an(osw1)
elif cmd == "rn":       # 入力層以外のウェイトをランダム値で埋める
    cmd_rn(h1w1)
    cmd_rn(h2w1)
    cmd_rn(osw1)
elif cmd == "w0":       # ウェイトを全てゼロにする
    cmd_rn(isw1)
    cmd_rn(h1w1)
    cmd_rn(h2w1)
    cmd_rn(osw1)

# 出力ファイルへ書き出す
rwf     = io.BytesIO(nndata1)
buf     = rwf.getbuffer()
st.pack_into(str(256         ) + "h", buf, offset11, *isb1)
st.pack_into(str(125388 * 256) + "h", buf, offset21, *isw1)
st.pack_into(str(32          ) + "i", buf, offset31, *h1b1)
st.pack_into(str(32     * 512) + "b", buf, offset41, *h1w1)
st.pack_into(str(32          ) + "i", buf, offset51, *h2b1)
st.pack_into(str(32     * 32 ) + "b", buf, offset61, *h2w1)
st.pack_into(str(1           ) + "i", buf, offset71, *osb1)
st.pack_into(str(32     * 1  ) + "b", buf, offset81, *osw1)
new_nn = rwf.read()

ofp    = open(ofn, "wb")
ofp.write(new_nn)
ofp.close()
