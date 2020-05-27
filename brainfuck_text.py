from sys import argv

if '.py' in argv[0]:
    del argv[0]
else:
    del argv[0:1]


ascii = {

' ':f"{'+'*32}.,",
'!':f"{'+'*33}.,",
'"':f"{'+'*34}.,",
'#':f"{'+'*35}.,",
'$':f"{'+'*36}.,",
'%':f"{'+'*37}.,",
'&':f"{'+'*38}.,",
"'":f"{'+'*39}.,",
'(':f"{'+'*40}.,",
')':f"{'+'*41}.,",
'*':f"{'+'*42}.,",
'+':f"{'+'*43}.,",
',':f"{'+'*44}.,",
'-':f"{'+'*45}.,",
'.':f"{'+'*46}.,",
'/':f"{'+'*47}.,",
'0':f"{'+'*48}.,",
'1':f"{'+'*49}.,",
'2':f"{'+'*50}.,",
'3':f"{'+'*51}.,",
'4':f"{'+'*52}.,",
'5':f"{'+'*53}.,",
'6':f"{'+'*54}.,",
'7':f"{'+'*55}.,",
'8':f"{'+'*56}.,",
'9':f"{'+'*57}.,",
':':f"{'+'*58}.,",
';':f"{'+'*59}.,",
'<':f"{'+'*60}.,",
'=':f"{'+'*61}.,",
'>':f"{'+'*62}.,",
'?':f"{'+'*63}.,",
'@':f"{'+'*64}.,",
'A':f"{'+'*65}.,",
'B':f"{'+'*66}.,",
'C':f"{'+'*67}.,",
'D':f"{'+'*68}.,",
'E':f"{'+'*69}.,",
'F':f"{'+'*70}.,",
'G':f"{'+'*71}.,",
'H':f"{'+'*72}.,",
'I':f"{'+'*73}.,",
'J':f"{'+'*74}.,",
'K':f"{'+'*75}.,",
'L':f"{'+'*76}.,",
'M':f"{'+'*77}.,",
'N':f"{'+'*78}.,",
'O':f"{'+'*79}.,",
'P':f"{'+'*80}.,",
'Q':f"{'+'*81}.,",
'R':f"{'+'*82}.,",
'S':f"{'+'*83}.,",
'T':f"{'+'*84}.,",
'U':f"{'+'*85}.,",
'V':f"{'+'*86}.,",
'W':f"{'+'*87}.,",
'X':f"{'+'*88}.,",
'Y':f"{'+'*89}.,",
'Z':f"{'+'*90}.,",
'[':f"{'+'*91}.,",
'\\':f"{'+'*92}.,",
']':f"{'+'*93}.,",
'^':f"{'+'*94}.,",
'_':f"{'+'*95}.,",
'`':f"{'+'*96}.,",
'a':f"{'+'*97}.,",
'b':f"{'+'*98}.,",
'c':f"{'+'*99}.,",
'd':f"{'+'*100}.,",
'e':f"{'+'*101}.,",
'f':f"{'+'*102}.,",
'g':f"{'+'*103}.,",
'h':f"{'+'*104}.,",
'i':f"{'+'*105}.,",
'j':f"{'+'*106}.,",
'k':f"{'+'*107}.,",
'l':f"{'+'*108}.,",
'm':f"{'+'*109}.,",
'n':f"{'+'*110}.,",
'o':f"{'+'*111}.,",
'p':f"{'+'*112}.,",
'q':f"{'+'*113}.,",
'r':f"{'+'*114}.,",
's':f"{'+'*115}.,",
't':f"{'+'*116}.,",
'u':f"{'+'*117}.,",
'v':f"{'+'*118}.,",
'w':f"{'+'*119}.,",
'x':f"{'+'*120}.,",
'y':f"{'+'*121}.,",
'z':f"{'+'*122}.,",
'{':f"{'+'*123}.,",
'|':f"{'+'*124}.,",
'}':f"{'+'*125}.,",
'~':f"{'+'*126}.,"

}

text = ''
brain = ''

for a in argv:
    text += a + ' '
text = text[:-1]

for c in text:
    from re import sub

    brain += sub(c, ascii[c], c)

print(brain)
