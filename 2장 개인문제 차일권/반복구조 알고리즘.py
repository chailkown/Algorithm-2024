# 실습자 : 202111467 차일권
# 실습일 : 2024:03:30
# 실습내용 : 팩토리얼의 반복구조
def factorial(n):
    result = 1  
    for k in range(n, 0, -1):  
        result = result * k  
    return result  

print(factorial(0))  # 출력: 1 (0! = 1)
print(factorial(1))  # 출력: 1 (1! = 1)
print(factorial(5))  # 출력: 120 (5! = 5*4*3*2*1 = 120)
print(factorial(10)) # 출력: 3628800 (10! = 10*9*8*7*6*5*4*3*2*1 = 3628800)
