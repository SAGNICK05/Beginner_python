# f=open('myfile.txt','w')
# f.write('Hello World\n')
# f.close()

# f=open('myfile.txt','r')
# text=f.read()
# print(text)
# f.close()

# f=open('myfile.txt','a')
# f.write('hey there this is sagnick')
# f.close()

# f=open('myfile.txt','r')
# print(f.read())

# with open('myfile2.txt','a') as f:
#     f.write('HEllo World\n')

with open('myfile2.txt','w') as f:
     f.write('hi this is sagnick\nwell we all are trapped in this World\n well thanks for youe message')    
    
# with open('myfile2.txt','r') as f:
#     g=f.read()
#     print(g)

# f=open('myfile2.txt','r')
# while True:
#     line=f.readline()
#     print(line)
#     if not line:
#         print("this is the end of file")
#         break
    
# f=open('myfile.txt','w')
# lines=['line1','line2','line3']
# for line in lines:
#     f.write(line+'\n')
# f.close()

f=open('myfile2.txt','r')
while True:
    line=f.readline()
    print(line)
    if not line:
        print("this is the end of file")
        break

f.seek(7)
g=f.read(8)
print(g)

f.close()

