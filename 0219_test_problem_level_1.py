# 딕셔너리 정렬하기
print("# 딕셔너리 정렬하기")

dic = {'조이정': 98, '김철수': 87, '조윤하': 20, '박진환': 76}

def sort_dic (a):
    mylist = list(dic.items())
    mylist.sort()
    return mylist

result = sort_dic(dic)
print(result)

print("")
# 파이선 버전 확인
print("# 파이선 버전 확인")

import sys

print(sys.version)

print("")
# 최대공약수 최소공배수
print("# 최대공약수와 최소공배수")

print("첫번째 수는 : ", end='')
first = int(input())
print("두번째 수는 : ", end='')
second = int(input())


def gcdlcm(a,b) :
    gcd = 1
    for i in range(1, first+1) :
        if first % i == 0 and second % i == 0 :
            gcd *= i
        else :
            pass
    lcm = int((first * second) / gcd)
    return gcd,lcm

print(gcdlcm(first,second))


print("")
# 스트링을 숫자로 바꾸기
print("# 스트링을 숫자로 바꾸기")

def strToInt (str) :
    result = int(str)
    return result

print(strToInt("-1234")+34)


print("")
# 가운데 글자 반환하기
print("# 가운데 글자 반환하기")


def string_middle(str)  :
    if len(str) % 2 == 0 :
        even = int((len(str)/2))
        return str[even-1:even+1]

    else :
        odd = int(len(str)/2-0.5)
        return str[odd:odd+1]

print(string_middle("middle"))
print(string_middle("test"))
print(string_middle("power"))



print("")
# 제일 작은 수 제거하기
print("# 제일 작은 수 제거하기")

def rm_small(mylist) :
    if len(mylist) <= 1 :
        return []
    else :
        new_mylist = sorted(mylist)             # .sort() 로 정렬할 수 있지만 되돌릴 수 없는 단점이 있다.
        rm=new_mylist[0]                        # 메모이를 극히 아껴야 하는 경우가 아니라면 sorted 함수를 써서 사본을 저장할 수 있다.
        mylist.remove(rm)
        return mylist


print(rm_small([4,6,327,74,3,1]))
print(rm_small([5]))
print(rm_small([4,3,2,1]))


## BEST Practice
def best(mylist):
    return  [i for i in mylist if i > min(mylist)]

print(best([6,2,8,5,1]))



print("")
# 정수 제곱근 판별하기
print("# 정수 제곱근 판별하기")

def nextSqure(n):
    for i in range(1,n):
        if i ** 2 == n :
            return (i+1)**2
        else :
            pass
    else : return "no"

print(nextSqure(131))
print(nextSqure(144))

## Best Practice :
from math import sqrt

def calc(m):
    if sqrt(m) % 1 == 0  :
        result = int((sqrt(m)+1)**2)
        return result
    else : return "no"

print(calc(144))
print(calc(145))


print("")
# x만큼 간격이 있는 n개의 숫자 Level 1
print("# x만큼 간격이 있는 n개의 숫자 Level 1")

def number_generator(a,b):
    mylist = []
    for i in range(1,b+1) :
        mylist.append(i*a)
    return mylist

print(number_generator(4,5))

## Best Practice :
def best(a,b):
    return list(range(a,a*(b+1),a))

print(best(6,7))


print("")
# 서울에서 김서방 찾기
print("# 서울에서 김서방 찾기")


def findKim(seoul) :
    kimIdx = 0
    for i in range(len(seoul)) :
        if "Kim" == seoul[i] :
            kimIdx=i
            return "김서방은 {}에 있습니다.".format(kimIdx)
        else : pass

print(findKim(["Queen", "Tod", "Kim"]))

## BEST Practice
def find(seoul) :
    return "김서방은 {}에 있습니다.".format(seoul.index('Kim'))

print(find(["Queen", "Tod", "Kim"]))



print("")
# 문자열 내 마음대로 정렬하기
print("# 문자열 내 마음대로 정렬하기")

def strange_sort(strings, n):
    from operator import itemgetter
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=itemgetter(n))

print(strange_sort(["sun", "bed", "car"], 1))



from operator import *

test=["sun", "bed", "car"]
print(sorted(test, key=itemgetter(2)))


print("")
# 핸드폰 번호 가리기
print("# 핸드폰 번호 가리기")

def hide_numbers(s):
    leng = len(s)-4
    four = s[-4:]
    return "*"*leng + four

print(hide_numbers("44551234"))

## Best Practice :
def hide_numbers1(s):
    return '*' * len(a[:-4]) + a[-4:]

print(hide_numbers("44551234"))


print("")
# 같은 숫자는 싫어
print("# 같은 숫자는 싫어")

def no_continuous(s):
    my = [s[0]]
    for i in range(1,len(s)):
        if s[i] != s[i-1]:
            my.append(s[i])
        else :
            pass
    return my

print( no_continuous( "133303" ))


print("")
# 자릿수더하기
print("# 자릿수더하기")

def sum_digit(number):
    string = str(number)
    num = 0
    for i in range(len(string)) :
        num += int(string[i])
    return num

print("결과 : {}".format(sum_digit(123)));


# Best Practice :
def sum_digit1(number):
    if number < 10 :
        return number
    else :
        return (number % 10) + sum_digit1(number // 10)

print("결과 : {}".format(sum_digit1(13452534623)));



print("")
# 평균구하기
print("# 평균구하기")

def average(array) :
    sum=0
    for i in range(len(array)) :
        sum += array[i]
    return sum / len(array)

list = [5,3,4]
print("평균값 : {}".format(average(list)));

# BEST Practice :
def average1(array) :
    return sum(array) / len(array)

list1=[2,6,3,8,5,3,2]
print("평균값 : {}".format(average1(list1)));


print("")
# 짝수와 홀수
print("# 짝수와 홀수")

def evenOrOdd(num):
    if num % 2 == 1 :
        return "Odd"
    else :
        return "Even"


print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))


print("")
# 피보나치 수
print("# 피보나치 수")

def fibonacci(num):
    my = [0,1]
    for i in range(num):
        my.append(my[i]+my[i+1])
    return my[-2]

print(fibonacci(5))

# Best Practice :
def fibonacci1(num) :
    a ,b =0,1
    for i in range(num):
        a = b
        b = a + b
    return a

print(fibonacci1(9))


print("")
# 약수의 합
print("# 약수의 합")

def sumDivisor(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0 :
            sum += i
        else : pass
    return sum+num

print(sumDivisor(12))


print("")
# 문자열 다루기 기본
print("# 문자열 다루기 기본")

def alpha_string46(s):
    try:
        if (len(s) == 4 or len(s) == 6) and int(s) :
            return True
        else : return False
    except ValueError :
        return False

print(alpha_string46("a234"))
print(alpha_string46("1234"))

# Best Practice :
def alpha_string461(s):
    return s.isdigit() and len(s) in [4,6]

print(alpha_string461("a234"))
print(alpha_string461("1234"))


print("")
# 문자열 내 p와 y의 개수
print("# 문자열 내 p와 y의 개수")

def numPY(s):
    p = 0
    y = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            p += 1
        elif s[i] == 'y' or s[i] == 'Y':
            y += 1
        else : continue
    if p == y : return True
    else : return False

print( numPY("pPoooyY") )
print( numPY("Pyy") )

# Best Practice  :
def numPY1(s):
    return s.lower().count('p') == s.lower().count('y')

print( numPY1("pPoooyY") )
print( numPY1("Pyy") )


print("")
# 수박수박수박수박수박수?
print("# 수박수박수박수박수박수?")

def water_melon(n):
    s=""
    for i in range(n) :
        if i % 2 == 0 : s += "수"
        else : s += "박"
    return s

print("n이 3인 경우: " + water_melon(3))
print("n이 45인 경우: " + water_melon(4))