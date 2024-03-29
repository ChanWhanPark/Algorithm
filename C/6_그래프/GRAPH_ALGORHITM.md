# 그래프 알고리즘
## 신장 트리
신장 트리 : 모든 정점이 n개인 무방향 그래프 G에서 정점이 n개이고 간선이 n-1개인 트리 형태의 부분 그래프
## 최소 비용 신장 트리를 만드는 알고리즘
### 1. 크루스칼 알고리즘 1
크루스칼 알고리즘(Kruskal Algorithm) 1은 가중치가 높은 간선을 제거하면서 최소 비용 신장 트리를 만든다.

> 1. 그래프 G의 모든 간선을 가중치에 따라 내림차순으로 정리한다.    
> 2. 그래프 G에서 가중치가 가장 높은 간선을 제거한다. 이때, 정점을 그래프에서 분리시키는 간선을 제거할 수 없으므로 이런 경우는 그 다음으로 가중치가 높은 간선을 제거한다.
> 3. 그래프 G에 간선이 n-1개만 남을 때까지 2를 반복한다.
> 4. 그래프에 간선이 n-1개만 남으면 최소 비용 신장 트리가 완성된다.

### 2. 크루스칼 알고리즘 2
크루스칼 알고리즘 2는 가중치가 낮은 간선을 삽입하면서 최소 비용 신장 트리를 만든다.
> 1. 그래프 G의 모든 간선을 가중치에 따라 오름차순으로 정리한다.   
> 2. 그래프 G에 가중치가 가장 낮은 간선을 삽입한다. 단, 이때 사이클을 형성하는 간선은 삽입할 수 없으므로 그 다음으로 가중치가 낮은 간선을 삽입한다.
> 3. 그래프 G에 간선이 n-1개 삽입될 때까지 2를 반복한다.
> 4. 그래프에 간선이 n-1개가 되면 최소 비용 신장 트리가 완성된다.

### 3. 프림 알고리즘
프림 알고리즘은 미리 간선을 정렬하지 않고, 하나의 정저에서 시작하여 트리를 확장해나가는 방법이다.
> 1. 그래프 G에서 시작 정점을 선택한다.
> 2. 선택한 정점에 부속된 가장 가중치가 낮은 간선을 연결하여 트리를 확장한다.
> 3. 이전에 선택한 정점과 새로 확장된 정점에 부속된 모든 간선 중, 가중치가 가장 낮은 간선을 삽입한다. 단, 사이클을 형성하는 간선은 삽입할 수 없으므로 이런 경우에는 그 다음으로 가중치가 낮은 간선을 선택한다.
> 4. 그래프 G에 간선이 n-1개 삽입될 때까지 3을 반복한다.
> 5. 그래프 G의 간선이 n-1개가 되면 최소 비용 신장 트리가 완성된다.

## 최단 경로 알고리즘
### 다익스트라 알고리즘
다익스트라 최단 경로 알고리즘은 정점 하나를 출발점으로 두고 다른 모든 정점을 도착점으로 하는 단일점에서 최단 경로 알고리즘 중 가장 많이 사용된다.
기본 원리는 시작 정점 v에서 가장 가까운 정점을 선택하여 추가하면서, 추가된 새로운 정점에 의해 단축되는 경로가 있으면, 경로 거리를 수정하는 과정을 반복하며 시작 정점에서 모든 정점에 대한 최단 경로를 구한다.
> 1. 경로 길이를 저장할 배열 준비
> 2. 시작 정점 초기화
> 3. 최단 거리 수정

### 플로이드 최단 경로 알고리즘
플로이드 최단 경로 알고리즘은 모든 정점 사이의 최단 경로를 구하고 이 알고리즘으로 만드는 최단 경로를 k-최단 경로라고도 한다.
>1. 정점 0부터 정점 k-1까지의 정점을 고려한 최단 거리 A^(k-1)을 구한 상태에서 다음 정점 k를 고려할 때, A^(k-1)[v][w]와 A^(k-1)[v][k] + A^(k-1)[k][w] 중에서 작은 값에 따라 최단 경로가 수정된다.
> 2. 경로에 정점을 늘려 가며 최단 경로를 구하다 최종적으로 A^(n-1)을 구하면 n개의 모든 정점 사이의 최단 경로를 구하게 된다.
> 3. 즉, A^(-1)은 초기 상태로서 가중치 인접 행렬인 배열 weight 값이 되고, A^(n-1)[v][w]는 정점 0부터 정점 n-1까지의 모든 정점을 이용한 최단 경로가 된다.