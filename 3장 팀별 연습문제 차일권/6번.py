#202111467 차일권
#2024/04/17
#알고리즘 연습문제 6
def binary_search(A, key):
    low = 0                  # 리스트의 가장 작은 인덱스
    high = len(A) - 1        # 리스트의 가장 큰 인덱스
    while low <= high:
        mid = (low + high) // 2    # 중간 인덱스 계산
        if A[mid] == key:
            return mid            # 값을 찾은 경우 중간 인덱스 반환
        elif A[mid] < key:
            low = mid + 1         # 찾고자 하는 값이 중간 값보다 큰 경우, 오른쪽 절반 탐색
        else:
            high = mid - 1        # 찾고자 하는 값이 중간 값보다 작은 경우, 왼쪽 절반 탐색
    return -1                      # 값이 리스트에 없는 경우 -1 반환

# 주어진 리스트
A = [3, 4, 5, 6, 7, 7, 8, 9]
# 찾고자 하는 값
key = 7
# 이진 탐색 실행
result = binary_search(A, key)
# 결과 출력
if result != -1:
    print(f"값 {key}는 인덱스 {result}에 있습니다.")
else:
    print(f"값 {key}는 리스트에 없습니다.")
