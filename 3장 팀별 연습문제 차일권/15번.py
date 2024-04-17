import random

def is_hamiltonian_cycle(graph, cycle):
    # 모든 정점을 한 번씩만 방문하는지 확인
    return set(cycle) == set(graph.keys()) and cycle[0] == cycle[-1]

def find_hamiltonian_cycle(graph):
    # 임의의 시작 정점 선택
    start_vertex = random.choice(list(graph.keys()))
    current_vertex = start_vertex
    cycle = [start_vertex]

    # 사이클 형성
    while True:
        # 현재 정점과 인접한 정점들 중 무작위로 선택
        neighbors = graph[current_vertex]
        next_vertex = random.choice(neighbors)
        
        # 다음 정점을 사이클에 추가
        cycle.append(next_vertex)

        # 모든 정점을 방문하고 마지막으로 선택한 정점이 시작 정점과 연결되어 있는지 확인
        if is_hamiltonian_cycle(graph, cycle):
            return cycle

        # 다음으로 이동
        current_vertex = next_vertex

# 간단한 그래프 정의
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# 해밀토니안 사이클 찾기
hamiltonian_cycle = find_hamiltonian_cycle(graph)
print("해밀토니안 사이클:", hamiltonian_cycle)
