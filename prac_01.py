# a=.7
# a1=1e9
#print(a1)
# b=.3
# b2=.6
# sumb=b+b2
# if round(sumb,1)==0.9:
#     print(round(sumb,1))
# else:
#     print(False)
#----자료형----#
# c=[1,2,3,4]
# print(c)
# list()
# []
# [0]*10
# a[-1]
# 인덱스 0부터 시작, 끝인덱스-1
#2차원 배열(행렬) 초기화 시 list comprehension 사용필수 - 값 대입 시 이상해짐
# n=3
# m=4
# arrmat = [[0]*m for _ in range(n)]
# print(arrmat)
#---배열 메소드---
# a=[5,1,2,3,4]
# a.sort()
# #print(a.sort()) //안됨

# b={2,4,6}
# remove = [i for i in a if i not in b]
# print(remove)

# 배열 리버스인덱싱
# a="string"
# b="hi"
# print(a[-3:])
# print(a[-3:-1])

#tuple. immutable. 다익스트라(우선순위큐), 공간효율적

#dict > array 빠름. 공간효율적
# d = dict()
# d[1] = 'bre'
# d[2] = 'lunch'
# d[3] = 'dinner'
# if 2 in d: #key로 조회해야함
#     print('go lunch')
# else:
#     print("can't lunch")

# dkeys = d.keys()
# dvals = d.values()
# print(type(dkeys))
# print(type(dkeys)) #dict_keys([1,2,3]) - type : <class 'dict_keys'>

# for k in dkeys:
#     print(k) #! keys()가 아닌 keys로만 하면 'builtin_function_or_method is not iterable' 나옴

s = set([1,2,3,4,5])
# print(s)

# s2 = set([1,10,20,30])
# print(s & s2) #|, &, -
s.update([999])
s.remove(2)
print(s)





