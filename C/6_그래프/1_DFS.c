/* 깊이 우선 탐색 (DFS) 구현하기 */
#include <stdio.h>
#include <memory.h>
#include <stdlib.h>
#define MAX_VERTEX 10
#define FALSE 0
#define TRUE 1

// 그래프에 대한 인접 리스트의 노드 구조 정의
typedef struct graphNode {
    int vertex;
    struct graphNode* link;
} graphNode;

typedef struct graphType {
    int n; // 정점 개수
    graphNode* adjList_H[MAX_VERTEX];
    int visited[MAX_VERTEX];
} graphType;

typedef int element;

// 스택 사용
typedef struct stackNode{
    int data;
    struct stackNode* link;
} stackNode;

stackNode* top;

int isEmpty(){
    if (top == NULL) return 1;
    else return 0;
}

void push(int item){
    stackNode* temp = (stackNode*)malloc(sizeof(stackNode));
    temp->data = item;
    temp->link = top;
    top = temp;
}

int pop(){
    int item;
    stackNode* temp = top;

    if (isEmpty()){
        printf("\n\n Stack is empty!\n");
        return 0;
    }
    else{
        item = temp->data;
        top = temp->link;
        free(temp);
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

// 그래프 g에서 정점 v에 대한 DFS 연산
void DFS(graphType *g, int v){
    graphNode* w;
    top = NULL; // 스택의 top
    push(v); // 깊이 우선 탐색을 시작하는 정점 v를 스택에 push
    g->visited[v] = TRUE; // 정점 v를 방문했으므로 해당 배열값을 TRUE로 설정
    printf(" %c", v+65);

    while (!isEmpty()){
        v = pop();
        w = g->adjList_H[v];
        // 인접 정점이 있는 동안 수행
        while (w){
            if (!g -> visited[w->vertex]){
                if (isEmpty()) push(v); // 정점 v로 돌아올 경우를 위해 다시 push하여 저장
                push(w->vertex);
                g->visited[w->vertex] = TRUE;
                printf(" %c", w->vertex + 65);
                v = w->vertex;
                w = g->adjList_H[v];
            }
            else w = w->link;
        }
    }
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

    printf("\n\n/////////\n\nDFS >> ");
    DFS(G9, 0);
    getchar();
}