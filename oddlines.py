file1=open('Codingal.txt','r')
file2=open('Codingalupdated.txt','w')

content=file1.readlines()
type(content)

for i in range(1,len(content)+1):
    if i%2!=0:
        file2.write(content[i-1])
    else:
        pass
file2.close()
file2=open('Codingalupdated.txt','r')
content2=file2.read()
print(content2)
file1.close()
file2.close()