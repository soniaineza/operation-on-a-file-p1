file = open('Codingal.txt','r')
print(file.read())
file.close()

file = open('Codingal.txt','r')
print(file.read(8))
file.close()

file = open('Codingal.txt','a')
file.write("my name is sonia")
file.close()