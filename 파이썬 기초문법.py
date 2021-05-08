# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 15:20:37 2021

@author: qwuni
"""

animal = "강아지"
name = "연탄이"
age= 4
hobby = "산책"
is_adult = age >=3
print("우리집 " + animal + "의 이름은 " +name + "에요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult)) 

## 연산자
print(4*2)
print(6/3)

print(2**4) #2^4 =16
print(5%3) # 나머지 2
print(5//3)  # 몫 1

## 간단한 수식
number = 2 + 3 * 4
print(number)
number = number +2
number += 2
print(number)

## 숫자처리함수
print(abs(-5)) 
print(pow(4,2))  # 4^2=16
print(max(5,12))
print(min(5,12))
print(round(3.14)) # 반올림

from math import *
print(floor(4.99)) #내림
print(ceil(1.22)) # 올림

## 랜덤함수 생성
from random import *
print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10 ) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0~10 이하
print(int(random( * 10) + 1)) #1~10 이하

print(int(raondom() * 45) + 1)  #1 ~45 이하

print(randrange(1,46))  #1~46 미만의 임의의 값 생성
print(randint(1,45))  #1~45 이하의 임의의 값을 생성

## 문자열
sentence = "나는 소년입니다"
sentence3 ="""
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

## 슬라이싱
jumin = "940120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])  # 0부터 2 직전까지 (0,1)
print("월 : " + jumin[2:4])

print("생년월일 : " + jumin[:6]) #처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print(" 뒤 7자리 (뒤에부터) :" + jumin[-7:])  #끝은 -1임

## 문자열 처리함수
python ="Python is Amazing"
print(python.lower())  #모든 문자가 다 소문자로 출력
print(python.upper())  # 대문자
print(python[0].isupper())  #python의 첫번째 글자가 대문자이냐
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")  # 해당 문자의 위치 찾기
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))

print(pyhton.find("Java"))  #내가 원하는 변수가 없을 경우 : -1 출력
print(python.index("Java"))  #내가 원하는 변수가 없을 경우  : 오류

print(python.count("n"))  # n이 총 몇번 나오는지

##문자열 포맷
#방법1
print("나는 %d살 입니다." %20)  # d : 정수
print("나는 %s을 좋아해요." % "파이썬") # s : 문자열
print("Apple은 %c로 시작해요." % "A")  # A : 문자
# %s 는 다 가능
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

#방법2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))

#방법3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age=27, color="빨간"))

#방법4
age=20
color= "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
#\n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

#저는 "나도코딩" 입니다.
# \" ,  \'  : 문장 내에서 따옴표
print("저는 \"나도코딩\"입니다.")

# \\ : 문장내에서 \
print("C:\\USER.")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b  : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

##QUIZ
url ="http://naver.com"
my_str = url.replace("http://", "")
my_str2= my_str.replace(".com", "")
print(my_str2)
a=print("비밀번호 : " + my_str2[0:3])
print(my_str2[0:3]+str(len(my_str2))+str(my_str2.count("e"))+ "!")

##SOLUTION
my_str = url.replace("http://", "")  #규칙1
my_str = my_str[:my_str.index(".")]  #규칙2
password= my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))

## 리스트 []  : 순서를 가진 객체의 집합
subway1 =10
subway2 =20
subway3 =30
subway = [10,20,30]
print(subway)

subway= ["유재석", "조세호", "박명수"]

#조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

#하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

###
num_list = [5,2,4,3,1]
num_list.sort()  # 정렬
num_list.reverse()  # 순서뒤집기
num_list.clear()   # 모두 지우기
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)

### 사전 자료형
dict = { "이름표" : [1,2,3]}  #key : 숫자형, 문자열, 튜플 / value : 리스트를 포함한 모든 자료형 
print(dict["이름표"])

dict1 = { 'one':1, 'two':2}
dict1['one']=11 # 값 수정
dict1['three']= 3 # 값 추가
del (dict1['one'])  # 값 삭제
dict1.pop('two')  # 값 삭제
dict2= {'one':100, 'three':3}
dict1.update(dict2)  # 딕셔너리 합치기
print(dict1)
#딕셔너리와 반복문(순서와 상관없이 for문 실행)
ages = {'Tod':35, 'Jane':23, 'Paul':62}
for key in ages:
    print('{}의 나이는 {}입니다.'.format(key, ages[key]))
for key,value in ages.items():
    print('{}의 나이는 {}입니다.'.format(key, value))
                   
    


cabinet = {3: "유재석" , 100: "김태호"}
print(cabinet[3])    # 해당 값이 없을 땐, 오류가 남
print(cabinet.get(3))  # 해당 값이 없을 땐, None 값이 됨
print(cabinet.get(5, "사용가능"))  #none 값 대신 사용 가능 출력

print(3 in cabinet) # True
print(5 in cabinet)  #False


cabinet = {"A-3" : "유재석" , "B-100": "김태호"}

# 새 손님
cabinet["A-3"] = "김종국"
cabinet["C-20"] =" 조세호"

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목용탕 폐점
cabinet.clear()
print(cabinet)

# 가위바위보
wintable = { '가위':'보', '바위':'가위', '보':'바위'}
def rsp(mine, yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'
    
result = rsp('가위', '보')
message = {
    'win': '이겼다', 'draw': '비겼네', 'lose' : '졌어'}  
print(message[result])  


## 튜플 : 내용 변경이나 추가 할 수 없지만, 속도가 매우 빠름
menu = ("돈가스", "치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age=20
hobby ="코딩"
print(name, age, hobby)

(name,age,hobby) =("김종국", 20, "코딩")
print(name,age,hobby)

## 집합(set)  : 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java={"유재석","김태호", "양세형"}
python= set(["유재석", "박명수"])

#교집합
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합
print(java- python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊어버린 사람
java.remove("김태호")
print(java)

## 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu= tuple(menu)
print(menu, type(menu))

menu= set(menu)
print(menu, type(menu))


##QUIZ
# 댓글 작성자들 중에 1명은 치킨, 3명은 커피쿠폰을 받는 추첨 프로그램을 작성하시오.
# 조건1 : 편의상 댓글은 20명이 작성, 아이디는 1~20 이라고 가정
# 조건2 : 무작위 추첨, 중복 불가
# 조건3 : random 모듈의 shuffle과 sample 활용

from random import *
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list)
shuffle(list)
print(list)
print(sample(list,1))
print(sample(list,1))
list.clear

sentence="""
-- 당첨자 발표 --
치킨 당첨자 : a[1]
커피 당첨자 : a[2:4]
-- 축하합니다 --
"""
print(sentence)

#solution
from random import *
users = range(1,21) #1부터 20까지 숫자를 생성
print(type(users))
users = list(users)
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:])
print("-- 축하합니다 --")

## if  조건문
weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
      print("마스크를 챙기세요")
else:
     print("준비물 필요 없어요")      

temp = int(input("기온은 어때요?"))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30 :
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요") 
    
    
## for 반복문   
for waiting_no in range(5): #0,1,2,3,4
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]

## while 반복문 (조건을 만족할 때까지 계속 반복)
customer = "토르"
index =5
while  index >= 1 :
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
      print("커피는 폐기처분되었습니다.")          
          
customer ="아이언맨"
person = "Unknown"

while person != customer :
      print("{0}, 커피가 준비 되었습니다.".format(customer))
      person= input("이름이 어떻게 되세요?")

## continue, break
absent = [2,5] # 결석
no_book =[7]  # 책을 깜빡했음
for student in range(1,11):  #1~10 까지 출석번호
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

## 한 줄 for
students = [1,2,3,4,5]
students = [i+100 for i in students]    
print(students)          

#학생 이름을 길이로 변환
students=["Iron man", "Thor", "I am groot"]          
students = [len(i) for i in students]          
print(students)          

#학생 이름을 대문자로 변환
students = [i.upper() for i in students]          
print(students)          

##QUIZ
from random import *
customer = range(1,21)
time= randrange(5,51)
okay = range(5,16)
over = range(15,51)
sign = 0
for time in randrange(5,51):
    if time in over:
        print("[] {}번째 손님 (소요시간 : {}분".format(customer,time))
    elif customer in okay:
       print("[{}] {}번째 손님(소요시간 : {}분".format(sign,customer,time))
 
##SOLUTION      
from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1,51)  #1 ~50 이라는 수 (승객)
    time = randrange(5,51)
    if 5<= time <=15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)". format(i, time))
        cnt +=1
    else:
        print("[] {0}번째 손님 (소요시간 : {1}분").format(i, time))
print("총 탑승 승객 : {0}분".format(cnt))   

## 함수
def open_account() :
    print("새로운 계좌가 생성되었습니다.")

open_account()    

def deposit(balance, money):  #입금
    print("입금이 완료되었습니다. 잔액은  {} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money : # 잔액이 출금보다 많으면
       print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
       return balance- money
    else:
       print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
       return balance

def withdraw_night(balance, money): #저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance-money-commission

balance = 0     
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
          .format(name,age,main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")        

def profile(name, age, *language) :
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++" "C#" , "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")

## 지역변수 , 전역변수
gun = 10

def checkpoint(soldiers) : # 경계근무
    global gun  # 전역 공간에 있는 gun 사용   
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계근무 나감
print("남은 총 : {0}".format(gun))   

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun= checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))   

##QUIZ
gender = ("남자", "여자")
height = 175    

def std_weight(height, gender) :
    if gender == "남자" :
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, round(((0.01*height) * (0.01*height) * 22),2)))  
    else :
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height, round(((0.01*height) * (0.01*height) * 21),2)))   
        
    
std_weight(175, "남자")    
    
##SOLUTION
def std_weight(height,gender):
    if gender == "남자":
        return (0.01*height) * (0.01 * height) *22
    else :
        return (0.01*height) * (0.01 * height) *21

height = 175
gender = "남자"
weight = round(std_weight(height, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


## 표준 입출력
print("Python", "Java")    
print("Python", "Java", sep=" vs ") 
   
print("Python", "Java", sep=" vs ", end="?")
print("무엇이 더 재미있을까요?")    

import sys
print("Python", "Java", file=sys.stdout)  # 표준출력
print("Python", "Java", file=sys.stderr)  # 표준에러

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":") 
# ljust(8) : 왼쪽으로 정렬, 해당칸은 총 8칸 / rjust(4) : 오른쪽으로 정렬, 총 4칸

#은행 대기순번표
# 001, 002, 003, ...
for num in range(1,12):
    print("대기번호 : " + str(num).zfill(3))  #zfill(3) : 3자리를 다 0으로 채워라

answer = input("아무 값이나 입력하세요 : ")    #사용자 입력을 통해 (input)을 통해 값을 갖게 되면 항상 문자열(str) 형태로 저장됨
print(type(answer))

## 다양한 출력포맷
print("{0:f}".format(5/3))     # 소수점 출력
print("{0: .2f}".format(5/3))   # 소수점 둘째자리까지 표시
print("{0: >10}".format(500))  #빈 자리는 빈공간으로 두고, 오른쪽 정렬, 총 10자리 공간 확보
print("{0: >+10}".format(500))  # 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >10}".format(-500))
print("{0:_<10}".format(500))  # 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:,}".format(10000000000))  # 3자리마다 콤마를 찍어주기
print("{0:^<+30,}".format(10000000000000))  # 빈자리마다 ^, 왼쪽정렬, +부호, 총 30자리, 3자리마다 콤마

## 파일 입출력
score_file = open("score.txt", "w", encoding= "utf8")  # w : 쓰기용도
print("수학 : 0", file= score_file)
print(" 영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding= "utf8")  # a : 덮어쓰기  append
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")  # r : 읽기
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
score_file.close() 

score_file = open("score.txt", "r", encoding="utf8") 
while True :
    line = score_file.readline()
    if not line:
        break
    print(line, end =" ")  # end=""  : 줄바꿈 x
score_file.close()    
    
score_file = open("score.txt",  "r", encoding="utf8")
lines= score_file.readlines()  #list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()   

## 모듈
import theater_module
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)

import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning
price(5)
price_morning(4)

from theater_module import price_soldier as price
price(5)

### 리스트와 문자열(유사, 서로 변환 가능)
characters = list("abcdef")
characters
words = "Hello world"
words_list = words.split()
time_str =  "10:35:27"
time_list = time_str.split(":")  # .split() : string을 리스트로 쪼개기
time_list
":".join(time_list)  # .join() : 리스트를 string으로 합치기

### 리스트
list1= list(range(20))
list1[5:15:2]  # step =2  씩 띄어서 값을 가져온다
list1[15:5:-1]
list1[::3]  # 전체 영역에 대하여 3씩 띄어서 가져오기
list1[0:2]=[77,88,99]  # slice로 list 수정
list1     
    
### 리스트 comprehansion
area = []
for i in range(1,11):
    if i % 2 ==0:
        area = area + [i*i]
print("area:", area)

area2 = [i*i for i in range(1,11) if i%2==0]
print("area2:", area2)    

[(x,y) for x in range(1,5) for y in range(1,5)]


    
    
    
    
    
    
    
    
    
    
    
    


















          
          
          
          
          
          
          
          
          
          
          
          
          
          
          























