import sys, pyperclip

infn = "mate3.sfen"
args = sys.argv
argc = len(args)
if argc > 1:
    infn = args[1]

with open(infn, "r") as inf:
    slist = inf.readlines()

print("Enterを押して！")

for sfen in slist:
    a = input()
    pyperclip.copy(sfen.strip())
    print("局面をコピーしたよ。ShogiGUIに貼ってね！")

print("お疲れ様でした！")
