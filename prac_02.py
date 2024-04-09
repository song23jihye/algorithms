# x=55
# y=100
# # x, y = list(input())
# # map(list(int(input())))
# print(x,y)

# if x>=90 and y==100:
#     print("A")
# elif x>=80 and y==100:
#     pass
# elif x>=70 and y==100:
#     print("C")
# else:
#     print("F")

# print(x>=90 & y==100)
# print((x>=90) & (y==100)) #조건 두개 만족은 and 쓰세요 굳이 이러지 말고
# print(x>=90 and y==100)

# print(x) if x>=90 else print("you're not A") #한줄로 조건식 표현

# a = [1,2,3,4,5,5,5]
# remove_set = {1,3,5}

# result = [i for i in a if i not in remove_set]
# print(result)

# while문
# i=1
# res=0
# while(i<=10):
#     if i%2==1:
#         res +=i
#     i+=1
# sum=0
# for i in range(11):
#     sum+=i
# print(sum)

#continue
# score = [50,100,70,100,95,97]
# n = 0
# for i in range(len(score)):
#     if i in [1,3]:
#         print(score[i]," (cheating)")
#         continue
#     if score[i]>90:
#         n+=1
#         print(score[i])
#     else:
#         pass
# print("exam pass count : ",n)

#---함수---#
# def add(a,b):
#     return a+b
# print(add(5, .7))
# print(add(b=9, a=8))

#---global---#
# number = 100
# def func1():
#     global number
#     number+=1
#     print(number)
# func1()
# func1()
# func1()
# func1()
# print(number)

#---람다---#
# print((lambda a,b: a+b)(3,7))

#---입출력---#
# a = list(map(int, input().split()))
# n = len(a)
# print(a)
# a.sort(reverse = True)
# print(a)
#---input함수가 느릴 때 사용하는 readline().rstrip()---#
# import sys
# data = sys.stdin.readline().rstrip()
# print(data)

# n=3
# print("문자열끼리만 덧셈연산으로 출력 가능"*3)
# print("문자열끼리만 덧셈연산으로 출력 가능"+3) //파이썬만 그럼. 자바는 해줌
# print("문자열끼리만 덧셈가능  "+str(n))
# print("문자열끼리만 덧셈가능",n) //컴마로 해야됨

# print(f"숫자는 {n}이다.") //f-string 문법

