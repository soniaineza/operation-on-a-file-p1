file = open('Codingal.txt','r')
print(file.readline())
file.close()

file = open('Codingal.txt','r')
print(file.readline())
print(file.readline())
print(file.readline())
file.close()


file = open('Codingal.txt','r')
for line in file:
    print(line)
file.close()