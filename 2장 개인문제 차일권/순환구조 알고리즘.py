# 실습자 : 202111467 차일권
# 실습일 : 2024:03:30
# 실습내용 : 팩토리얼의 순환구조
def factorial(n):
    if n <= 1:
        return 1  
    else:
        return n * factorial(n - 1)  


print(factorial(0))  # 출력: 1 (0! = 1)
print(factorial(1))  # 출력: 1 (1! = 1)
print(factorial(2))  # 출력: 2 (2! = 2*1 = 2)
print(factorial(3))  # 출력: 6 (3! = 3*2*1 = 6)
