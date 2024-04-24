#202111467 차일권
#2024/04/24
#4장 알고리즘 연습문제 7 -1 

def DFS_Tool(graph):
    visited = set()  # 이미 방문한 정점을 기록하기 위한 집합
    stack = []       # 위상 정렬 결과를 담기 위한 스택

    def dfs(vertex):
        visited.add(vertex)  # 현재 정점을 방문했음을 표시
        for neighbor in graph[vertex]:
            if neighbor not in visited:  # 이웃 정점 중 방문하지 않은 정점에 대해 DFS 호출
                dfs(neighbor)
        stack.append(vertex)  # 현재 정점을 스택에 추가하여 역순으로 저장

    # 모든 정점에 대해 DFS를 수행하여 위상 정렬 수행
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    # 위상 정렬된 순서를 역순으로 반환하여 반환
    return stack[::-1]

# 주어진 방향 그래프
graph = {
    "A": {"B", "C"},
    "B": {"D"},
    "C": {"D", "E"},
    "D": {"F"},
    "E": {"G", "H"},
    "F": {},
    "G": {"H"},
    "H": {"C"}
}


# DFS를 사용한 위상 정렬 수행
line = DFS_Tool(graph)

print("위상 정렬 순서:", line)
