str=input('Enter string : ')
isPalin=True
for i in range(0,int(len(str)/2)):
    if str[i]!=str[len(str)-i-1]:
        isPalin=False
if isPalin==True:
    print('Palindromic string')
else:
    print('Not Palindromic string')