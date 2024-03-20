"""
202111467 차일권
heapq 우선순위 큐를 사용하여 리스트 정렬하기
"""
import heapq

def number_list(nums):
   
    heapq.heapify(nums)

    sorted_nums = []

    while nums:
        sorted_nums.append(heapq.heappop(nums))

    return sorted_nums

numbers = [1213, 12, 323, 211, 35, 429, 552, 916]

sorted_numbers = number_list(numbers)
print("정렬된 리스트:", sorted_numbers)
