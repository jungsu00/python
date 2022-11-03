# x = 10
# y = 3
# print(x+y)    # x 의 y 덧셈
# print(x-y)    # x 의 y 뺄셈
# print(x*y)    # x 의 y 곱하기
# print(x/y)    # x 의 y 나누기
# print(x**y)   # x 의 y 제곱
# print(x//y)   # x 의 y 나눈 몫을 반환? 일단 3.33333나와야하는데 3나옴 아마 나머지는 버리는듯?
# print(x%y)    # x 의 y 나눈 나머지 값만 출력 
# round() 반올림 함수   # print(round(1.23456, 2))   # 1.23456의 소숫점 2까지 출력
# print("한 줄 쓰고\n그 다음 줄을 쓴다.")   # \n 띄워쓰기
# round() 반올림 함수
# print(round(1.23456, 2))   # 1.23456의 소숫점 2까지 출력
# def'함수이름'(매개변수1,매개변수2):
# find()로 처음(왼쪽)부터 문자열을 찾을 수 있음 rfind()는 뒤(오른쪽)에서 부터 검색
#   -> a = apply  
# count() 문자열에 문자나 단어의 개수를 알 수 있음
# replace() 문자열을 다른 문자열로 바꿔줌   예시 replace(" ","") 공백 사라짐# split()
#   -> 문자열.split('구분자', 분할횟수) / 문자열.split(sep='구분자', maxsplit=분할횟수)
# family = ['mother', 'father', 'gentleman', 'sexy lady']
#   -> 리스트   예시 함수 = [개체변수, 개체변수, 개체변수, 개체변수 ···]
# class 내장함수
# global(글로벌) 변수 = 전역변수
# 플로어 차트   알고 있어야 함
# ----------------------------------------------------------------
# for문 사용하기
# family = ['mother', 'father', 'gentleman', 'sexy lady']
# for x in family:
#     print(x, len(x))   # len은 각 단어의 문자크기를 구함
# ----------------------------------------------------------------
# type기초
# t = (1, "korea", 3.5, 1)
# print(t)
# print(type(t))
# ----------------------------------------------------------------
# find기초
# a = "puzzle"
# c = a.find("p")
# print(c)
# ----------------------------------------------------------------
# split()의 활용
# a, b, c = input("입력하시오 : "). split()
# print(f"안녕, {a}")
# print(f"안녕, {b}")
# print(f"안녕, {c}")

# a, b, c = input("입력하시오 : "). split()
#   -> 디버깅하면 "입력하시오 : "라고 출력됨 그러면 "글자 글자 글자" 엔터 말고 스페이스바 해야함
# ----------------------------------------------------------------
# list의 기본
# array = [273, 32, 103, "문자열", True, False]
# print(array)

# list.remove() 는 ()안에 리스트 안에 값을 적어서 삭제
# list.pop()은 ()안에 인덱스를 입력하여 값을 삭제
#                     -> 위에 문제 array[0] = 273 할 때 0이 인덱스
# ----------------------------------------------------------------
# 함수 return값 활용하기   python은 리턴값 여러개 가능
# def fir(a,b):
#     return a+b, a-b, a*b
# c = fir(10,5)
# print(c)
# ----------------------------------------------------------------
# 파일 만드는 코드
# file = open("basic.txt","w")
# file.write("hello python Programming...!")
# file.close()
# 파일 내용을 터미널에 나오게 하는 코드
# with open("basic.txt","r")as file:
#     contents = file.read()
# print(contents)
