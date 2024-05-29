#202111467 차일권
#2024/05/29
#6장 알고리즘 연습문제 20

def hash_function(key, size):
    return key % size

def insert(hash_table, key, value):
    index = hash_function(key, len(hash_table))
    hash_table[index] = value

def main():
    hash_table_size = 13
    hash_table = [None] * hash_table_size

    # 입력 자료
    data = [27, 130]

    for key in data:
        insert(hash_table, key, key)

    # 해시 테이블 출력
    for i, value in enumerate(hash_table):
        print(f"인덱스 {i}: {value}")

if __name__ == "__main__":
    main()
