'''
aa = []
aa.append(0)
aa.append(0)
aa.append(0)
aa.append(0)
print(aa)
'''




'''
aa = []

for i in range(0,100):
    aa.append(0)
print(len(aa))
'''



###다시다시!
'''
num = []
sum = 0

#리스트 초기화해줘야함!!!
for i in range(0,4):
    num.append(0)

for i in range(0,4):
    num[i] = int(input(str(i+1)+"번째 숫자 : "))
#str써야 하는 이유: input은 문자열이고 int는 입력값에만 해당되는 데이터 타입이기 때문에
    sum += num[i]
print("합계 ==> %d" % sum)
'''






'''
aa=[10,20,30]
aa=[] #리스트 껍데기는 남아있음
print(aa)
print(type(aa))

aa=[1,2,3]
aa=None #aa는 더이상 리스트가 아님
print(aa)
print(type(aa))

aa=[1,2,3]
del(aa)
print(aa)
print(type(aa))
'''





######### 교수님코드 따라적고 공부하기 - 사진 ##################
'''
scores=[]
bestind, worstind, sum= 0, 0, 0


for i in range(0,5):
    scores.append(0)

    
print("5명의 평가 점수를 입력하세요! (100점 만점)")
    
for i in range(0,5):
    scores[i] = int(input("점수 입력 : "))

#점수를 입력한 다음에 0번째 index의 값을 best와 worst로 지정할 수가 있는거! 순서중요! 
best = scores[0]
worst = scores[0]

print("\n##총 입력 점수##")
for i in range(0,5):
    print("%d 점"% scores[i])

for i in range(0,5):
    if best <= scores[i]:
        best = scores[i]
        bestind = i

for k in range(0,5):
    if worst >= scores[k]:
        worst = scores[k]
        worstind = k
                    
print("\n##제거 대상 점수##")
print("-최고 점수 : %d" % best)
print("-최소 점수 : %d" % worst)

scores.remove(scores[bestind])
scores.remove(scores[worstind])

print("\n##최종 입력 점수##")
for i in range(0,3): #원소의 개수가 줄어든걸 반영해줘야지~!
    print("%d 점"% scores[i])
    sum += scores[i]

print("\n총점 %d"% sum)
'''
# 왜 안되는지 모름! 다시다시!print("평균 %d"% sum/3)






'''
tt = (10,20,30)
t1 = (10)
t = 10;

print(t)
print(t1)
'''




'''
singer = {} #기초

singer = {'이름':'트와이스','구성원 수':9,'데뷔':'서바이벌 식스틴','대표곡':'SIGNAL'}

for k in singer.keys():
    print('%s --> %s' % (k, singer[k])) ###singer[k] 키에 해당하는 값을 반환
'''


#오만년 걸림..복습...공부하기

foods = {'떡볶이': '오뎅', '짜장면':'단무지','라면':'김치','피자':'피클','치킨':'콜라'}

like = list(foods.keys())

while True:
    pair = input(str(like)+"중 좋아하는 음식은?:")
    if pair in foods :
        print("<%s>엔 <%s>이지요." % (pair, foods.get(pair)))
    elif pair == '끝':
        break
    else:
        print("그런 음식은 없습니다.")



























        













