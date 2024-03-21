"""
202111467 차일권
gcd를 이용하여 최대 공약수 구하기
"""
def gcd (X, Y) :
# A와 B의 약수를 저장할 리스트 초기화
    A_list = []
    B_list = []

# A의 약수 구하기
    for i in range(1, X + 1):       
        if X % i == 0:
            A_list.append(i)

# B의 약수 구하기
    for i in range(1, Y + 1):       
        if Y % i == 0:
         B_list.append(i)

    print(f"{X}의 약수 =", A_list)
    print(f"{Y}의 약수 =", B_list)

# A와 B의 공통된 약수를 찾고 그 중에서 최대 값을 구한다
    common_factors = set(A_list) & set(B_list)
    return max(common_factors)


print("최대 공약수 =", gcd(60, 28))
