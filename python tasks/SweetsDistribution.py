names=[]
name=input()
while name != '':
    names.append(name)
    name=input()
setNames=list(set(names))
for name in setNames:
    count=names.count(name)
    print(name,':',count)