f=open('1.txt','r',encoding='utf-8')

# for i in range(5):
#     score=input('점수 : ')
#     f.write(score+'\n')

s=0
cnt=0
for score in f:
    s=s+int(score)
    cnt=cnt+1

f.close()

print(s/cnt)
print(f'{s/cnt:.2f}')