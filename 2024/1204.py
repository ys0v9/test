# avg=92.2456
# print(f'{avg:.2f}')
# print('%.2f'%(avg)) #잘 안씀
# print(round(avg,2))

# def add(x,y):
#     print(x+y)
# a=10
# b=20
# add(a,b)

# def add(x,y):
#     return x+y
# a=10
# b=20
# print(add(a,b))

# def add(x,y):
#     return x+y
# a=10
# b=20
# c=add(a,b)
# print(c)

# def grade(s,sc):
#     if sc>=90:
#         print(s+'A')
#     elif sc>=80:
#         print(s+'B')
#     elif sc>=70:
#         print(s+'C')
#     elif sc>=60:
#         print(s+'D')
#     else:
#         print(s+'E')
# print('중간고사 목표 점수를 입력하세요')
# kor=int(input("국어 점수를 입력하세요"))
# grade('국어',kor)

# def sachic(x,y):
#     plus=x+y
#     minus=x-y
#     print(plus)
#     return minus
# a=10
# b=20
# c=sachic(a,b)
# print(c)

# sub=['국어','영어','수학',0,1,True]
# print(sub[3])
# sub[3]='과학'
# sub[4]='역사'
# sub.remove(True) #특정한 것을 지움(여러 개 있을 시 맨 앞에 있는 것만 지움)
# del sub[0] #딱 그 숫자의 위치에 있는 것만 지움
# sub.append('총점')
# sub.insert(2,'정보')
# print(sub)

# a_list=[100,200,300,-10,70]
# print(a_list[2:4])
# print(a_list[-1])
# print(a_list[:-1])
# print(a_list[0:-2])
# print(a_list[-4:4])

# def average(total_score,mount):
#     ave=total_score/mount
#     return ave
# sub=['국어','영어','수학','과학','역사']
# score=[100,90,89,88,77]
# total=score[0]+score[1]+score[2]+score[3]+score[4]
# print('평균:'+str(average(total,len(score)))+'점')

# sub=['국어','영어','수학','과학','역사']
# for i in sub:
#     print(i+'수업에 집중합시다..')
# print(' ')
# for i in ['국어','영어','수학','과학','역사']:
#     print(i+'수업에 집중합시다..')

# for i in range(0,5,2):
#     print('노트북 충전')

# sub=['국어','영어','수학','과학','역사']
# for i in range(4,-1,-1):
#     print(sub[i]+'시간에 노트북 충전 하기')

# def average(total_score,mount):
#     ave=total_score/mount
#     return ave
# sub=['국어','영어','수학','과학','역사']
# score=[100,90,89,88,77]
# total=0
# for i in range(0,5):
#     total=total+score[i]
# print(average(total,len(score)))
# print('평균:'+str(average(total,len(score)))+'점')

# def menu_p(drink,price):
#     print(drink+str(price)+'원')
# drink=['커피','우유','물']
# price=[500,300,200]
# for i in range(0,3):
#     menu_p(drink[i],price[i])

# menu_dict={'커피':500, '우유':300, '물':200}
# print(menu_dict)
# menu_dict['주스']=400 #추가, append 처럼 맨 뒤에 추가 되는게 아님. 그냥 추가 되는거라 생각하기.
# print(menu_dict['우유'])
# del menu_dict['커피']
# print(menu_dict)