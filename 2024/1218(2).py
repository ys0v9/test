f=open('2.txt','r',encoding='utf-8')

# content=f.read()
# print(content)

# content=f.readline()
# print(content)

# content=f.readlines()
# print(content)
# for i in content:
#     print(i)

for i in f:
    print(i)

f.close()