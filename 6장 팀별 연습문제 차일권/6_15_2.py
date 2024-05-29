#202111467 차일권
#2024/05/29
#6장 알고리즘 연습문제 15-2 

def create_shift_table(pattern):
    # 시프트 테이블을 패턴의 길이로 초기화합니다.
    shift_table = {ch: len(pattern) for ch in "ACGT"}
    
    # 시프트 테이블에 적절한 시프트 값을 채웁니다.
    for i in range(len(pattern) - 1):
        shift_table[pattern[i]] = len(pattern) - 1 - i
        
    return shift_table

def search(text, pattern):
    shift_table = create_shift_table(pattern)
    m = len(pattern)
    n = len(text)
    
    i = 0
    same = []
    
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            same.append(i)
            i += m
        else:
            i += shift_table.get(text[i + m - 1], m)
    
    return same

# 주어진 텍스트와 패턴
text = "TTATAGATCTCGTATTCTTTATAGATCTCCTATTCTT"
pattern = "TCCTATTCTT"

# 호스풀 알고리즘을 사용하여 패턴 검색
same = search(text, pattern)
print("패턴이 발견된 위치:", same)
