# HalfKPからHalfKPE9に変換
# 一度空でもいいからHalfKPE9のファイルを作成し、そこにHalfKPの値を埋めていく方法をとる
#
# 使用法
#   python3 hkp2hkpe9.py [HalfKPファイルパス] [HalfKPE9ファイルパス]

import io, sys
import struct as st

ifn1  = "eval/halfkp/nn.bin"
ifn2  = "eval/halfkpe9/nn.bin"

args  = sys.argv
argc  = len(args)

if argc > 1:
    ifn1 = args[1]
if argc > 2:
    ifn1 = args[1]
    ifn2 = args[2]

# HalfKPの分解

nndata1  = open(ifn1, "rb").read()
nnlen1   = st.unpack_from("<I", nndata1, 8)[0]

# HalfKPの各層のポインタオフセット

offset1  = 4 + 4 + 4 + nnlen1 + 4           # isb
offset2  = offset1 + 256 * 2                # isw
offset3  = offset2 + 125388 * 256 * 2 + 4   # h1b
offset4  = offset3 + 32 * 4                 # h1w
offset5  = offset4 + 32 * 512               # h2b
offset6  = offset5 + 32 * 4                 # h2w
offset7  = offset6 + 32 * 32                # osb
offset8  = offset7 + 4                      # osw

# HalfKPの各層を構造配列に取り込む

isb1     = st.unpack_from("<" + str(256) + "h", nndata1, offset1)
isw1     = st.unpack_from("<" + str(125388 * 256) + "h", nndata1, offset2)
h1b1     = st.unpack_from("<" + str(32) + "i", nndata1, offset3)
h1w1     = st.unpack_from("<" + str(32 * 512) + "b", nndata1, offset4)
h2b1     = st.unpack_from("<" + str(32) + "i", nndata1, offset5)
h2w1     = st.unpack_from("<" + str(32 * 32) + "b", nndata1, offset6)
osb1     = st.unpack_from("<" + str(1) + "i", nndata1, offset7)
osw1     = st.unpack_from("<" + str(32 * 1) + "b", nndata1, offset8)

# HalfKPE9の分解

nndata2  = open(ifn2, "rb").read()
nnlen2   = st.unpack_from("<I", nndata2, 8)[0]

# HalfKPE9の各層のポインタオフセット

offset10 = 4 + 4 + 4 + nnlen2 + 4           # isb
offset20 = offset10 + 256 * 2               # isw
offset30 = offset20 + 125388 * 256 * 2      # h1b 0
offset31 = offset30 + 125388 * 256 * 2      # h1b 1
offset32 = offset31 + 125388 * 256 * 2      # h1b 2
offset33 = offset32 + 125388 * 256 * 2      # h1b 3
offset34 = offset33 + 125388 * 256 * 2      # h1b 4
offset35 = offset34 + 125388 * 256 * 2      # h1b 5
offset36 = offset35 + 125388 * 256 * 2      # h1b 6
offset37 = offset36 + 125388 * 256 * 2      # h1b 7
offset38 = offset37 + 125388 * 256 * 2 + 4  # h1b 8
offset40 = offset38 + 32 * 4                # h1w
offset50 = offset40 + 32 * 512              # h2b
offset60 = offset50 + 32 * 4                # h2w
offset70 = offset60 + 32 * 32               # osb
offset80 = offset70 + 4                     # osw

# HalfKPE9の各層を構造配列に取り込む

isb20    = st.unpack_from("<" + str(256) + "h", nndata2, offset10)
isw20    = st.unpack_from("<" + str(125388 * 256) + "h", nndata2, offset20)
isw21    = st.unpack_from("<" + str(125388 * 256) + "h", nndata2, offset30)
isw22    = st.unpack_from("<" + str(125388 * 256) + "h", nndata2, offset31)
isw23    = st.unpack_from("<" + str(125388 * 256) + "h", nndata2, offset32)
isw24    = st.unpack_from("<" + str(125388 * 256) + "h", nndata2, offset33)
isw25    = st.unpack_from("<" + str(125388 * 256) + "h", nndata2, offset34)
isw26    = st.unpack_from("<" + str(125388 * 256) + "h", nndata2, offset35)
isw27    = st.unpack_from("<" + str(125388 * 256) + "h", nndata2, offset36)
isw28    = st.unpack_from("<" + str(125388 * 256) + "h", nndata2, offset37)
h1b20    = st.unpack_from("<" + str(32) + "i", nndata2, offset38)
h1w20    = st.unpack_from("<" + str(32 * 512) + "b", nndata2, offset40)
h2b20    = st.unpack_from("<" + str(32) + "i", nndata2, offset50)
h2w20    = st.unpack_from("<" + str(32 * 32) + "b", nndata2, offset60)
osb20    = st.unpack_from("<" + str(1) + "i", nndata2, offset70)
osw20    = st.unpack_from("<" + str(32 * 1) + "b", nndata2, offset80)

# ヘッダ部以外、HalfKPの各層の値をHalfKPE9にコピーする
# 利き分9個はHalfKPのものと同じものをコピーしておく

isb20    = isb1
isw20    = isw1
isw21    = isw1
isw22    = isw1
isw23    = isw1
isw24    = isw1
isw25    = isw1
isw26    = isw1
isw27    = isw1
isw28    = isw1
h1b20    = h1b1
h1w20    = h1w1
h2b20    = h2b1
h2w20    = h2w1
osb20    = osb1
osw20    = osw1

# 出力ファイルへ書き出す

rwf      = io.BytesIO(nndata2)
buf      = rwf.getbuffer()
st.pack_into(str(256         ) + "h", buf, offset10, *isb20)
st.pack_into(str(125388 * 256) + "h", buf, offset20, *isw20)
st.pack_into(str(125388 * 256) + "h", buf, offset30, *isw21)
st.pack_into(str(125388 * 256) + "h", buf, offset31, *isw22)
st.pack_into(str(125388 * 256) + "h", buf, offset32, *isw23)
st.pack_into(str(125388 * 256) + "h", buf, offset33, *isw24)
st.pack_into(str(125388 * 256) + "h", buf, offset34, *isw25)
st.pack_into(str(125388 * 256) + "h", buf, offset35, *isw26)
st.pack_into(str(125388 * 256) + "h", buf, offset36, *isw27)
st.pack_into(str(125388 * 256) + "h", buf, offset37, *isw28)
st.pack_into(str(32          ) + "i", buf, offset38, *h1b20)
st.pack_into(str(32     * 512) + "b", buf, offset40, *h1w20)
st.pack_into(str(32          ) + "i", buf, offset50, *h2b20)
st.pack_into(str(32     * 32 ) + "b", buf, offset60, *h2w20)
st.pack_into(str(1           ) + "i", buf, offset70, *osb20)
st.pack_into(str(32     * 1  ) + "b", buf, offset80, *osw20)
new_nn = rwf.read()

ofp    = open(ifn2, "wb")
ofp.write(new_nn)
ofp.close()
