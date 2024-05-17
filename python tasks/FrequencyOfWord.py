str=input('enter string : ')
setStr=list(set(str))
for c in setStr:
    freq=str.count(c)
    print(c,'repeated',freq,'times.')