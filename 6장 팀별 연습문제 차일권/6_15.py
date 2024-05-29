#202111467 차일권
#2024/05/29
#6장 알고리즘 연습문제 15-1

def create_shift_table(pattern):
    # 시프트 테이블을 패턴의 길이로 초기화합니다.
    shift_table = {ch: len(pattern) for ch in "ACGT"}
    
    # 시프트 테이블에 적절한 시프트 값을 채웁니다.
    for i in range(len(pattern) - 1):
        shift_table[pattern[i]] = len(pattern) - 1 - i
        
    return shift_table

# 주어진 패턴
pattern = "TCCTATTCTT"

# 시프트 테이블 생성
shift_table = create_shift_table(pattern)
print(shift_table)  
