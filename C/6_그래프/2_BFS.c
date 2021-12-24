/* BFS */
#include <stdio.h>
#include <memory.h>
#include <stdlib.h>
#define MAX_VERTEX 10
#define TRUE 1
#define FALSE 0

// 그래프에 대한 인접 리스트의 노드 구조 정의
typedef struct graphNode {
    int vertex;
    struct graphNode *link;
} graphNode;

typedef struct graphType {
    int n;
    graphNode* adjList_H[MAX_VERTEX];
    int visited[MAX_VERTEX];
} graphType;

typedef int element;

// 큐 사용
typedef struct QNode {
    int data;
    struct QNode* link;
} QNode;

typedef struct {
    QNode *front, *rear;
} LQueueType;

LQueueType *createdLinkedQueue(){
    LQueueType *LQ;
    LQ = (LQueueType*)malloc(sizeof(LQueueType));
    LQ->front = NULL;
    LQ->rear = NULL;
    return LQ;
}

int isEmpty(LQueueType *LQ){
    if (LQ->front == NULL){
        printf("\n Linked Queue is Empty!\n");
        return 1;
    }
    else return 0;
}

void enQueue(LQueueType *LQ, int item){
    QNode *newNode = (QNode*)malloc(sizeof(QNode));
    newNode->data = item;
    newNode->link = NULL;
    if (LQ->front == NULL){
        LQ->front = newNode;
        LQ->rear = newNode;
    }
    else {
        LQ->rear->link = newNode;
        LQ->rear = newNode;
    }
}

int deQueue(LQueueType *LQ){
    QNode *old = LQ->front;
    int item;
    if (isEmpty(LQ)) return 0;
    else {
        item = old->data;
        LQ->front = LQ->front->link;
        if (LQ->front == NULL)
            LQ->rear = NULL;
        free(old);
        return item;
    }
}

// 깊이 우선 탐색을 위해 초기 공백 그래프 생성
void createGraph(graphType* g){
    int v;
    g->n = 0;
    for (v=0;v<MAX_VERTEX;v++){
        g->visited[v] = FALSE; // 그래프의 정점에 대한 배열 visited를 FALSE로 초기화
        g->adjList_H[v] = NULL; // 인접 리스트에 대한 헤드 노드 배열을 NULL로 초기화
    }
}

// 그래프 g에 정점 v를 삽입하는 연산
void insertVertex(graphType *g, int v){
    if (((g->n) + 1) > MAX_VERTEX){
        printf("\nOverload!");
        return;
    }
    g->n++;
}

// 그래프 g에 간선 (u, v)를 삽입하는 연산
void insertEdge(graphType *g, int u, int v){
    graphNode* node;
    if (u >= g->n || v >= g->n){
        printf("\nNot existed!");
        return;
    }
    node = (graphNode*)malloc(sizeof(graphNode));
    node->vertex = v;
    node->link = g->adjList_H[u];
    g->adjList_H[u] = node;
}

// 그래프 g의 각 정점에 대한 인접 리스트를 출력하는 연산
void print_adjList(graphType* g){
    int i;
    graphNode* p;
    for (i=0;i < g->n;i++){
        printf("\n\t\t %c's adj_list", i+65);
        p = g->adjList_H[i];
        while (p){
            printf(" -> %c", p->vertex + 65);
            p = p->link;
        }
    }
}

// 그래프 g에서 정점 v에 대한 BFS 연산
void BFS(graphType* g, int v){
    graphNode* w;
    LQueueType* Q; // 큐
    Q = createdLinkedQueue(); // 큐 생성
    g->visited[v] = TRUE;
    printf(" %c", v+65);
    enQueue(Q, v); // 현재 정점 v를 큐에 enQueue

    // 큐가 공백이 아닌 동안 BFS 수행
    while (!isEmpty(Q)){
        v = deQueue(Q);
        // 현재 정점 w를 방문하지 않은 경우
        for (w = g->adjList_H[v]; w; w=w->link) // 인접 정점이 있는 동안 수행
            if (!g->visited[w->vertex]){ // 정점 w가 방문하지 않은 정점인 경우
                g->visited[w->vertex] = TRUE;
                printf(" %c", w->vertex + 65); // 정점 0~6을 A~G로 바꿔 출력
                enQueue(Q, w->vertex);
            }
    } // 큐가 공백이면 너비 우선 탐색 종료
}

void main()
{
    int i;
    graphType *G9;
    G9 = (graphType*)malloc(sizeof(graphType));
    createGraph(G9);

    for (i=0;i<7;i++){
        insertVertex(G9, i);
    }
    insertEdge(G9, 0, 2);
    insertEdge(G9, 0, 1);
    insertEdge(G9, 1, 4);
    insertEdge(G9, 1, 3);
    insertEdge(G9, 1, 0);
    insertEdge(G9, 2, 4);
    insertEdge(G9, 2, 0);
    insertEdge(G9, 3, 6);
    insertEdge(G9, 3, 1);
    insertEdge(G9, 4, 6);
    insertEdge(G9, 4, 2);
    insertEdge(G9, 4, 1);
    insertEdge(G9, 5, 6);
    insertEdge(G9, 6, 5);
    insertEdge(G9, 6, 4);
    insertEdge(G9, 6, 3);
    printf("\n G9's adjust list  ");
    print_adjList(G9);

    printf("\n\n/////////\n\nBFS >> ");
    BFS(G9, 0);
    getchar();
}