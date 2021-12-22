/* 연결 자료구조를 이용한 연결 큐 구현 */
#include <stdio.h>
#include <malloc.h>

typedef char element; // 연결 큐 원소의 자료형을 char로 정의
typedef struct QNode {
    element data;
    struct QNode *link;
} QNode;

typedef struct {
    QNode *front, *rear;
} LQueueType;

// 공백 연결 큐를 생성하는 연산
LQueueType *createLinkedQueue(){
    LQueueType *LQ;
    LQ = (LQueueType*)malloc(sizeof(LQueueType));
    LQ->front = NULL;
    LQ->rear = NULL;
    return LQ;
}

// 연결 큐가 공백 상태인지 확인하는 연산
int isEmpty(LQueueType *LQ){
    if (LQ->front == NULL){
        printf("Linked Queue is Empty!");
        return 1;
    }
    else return 0;
}

// 연결 큐의 rear에 원소를 삽입하는 연산
void enQueue(LQueueType *LQ, element item){
    QNode *newNode = (QNode*)malloc(sizeof(QNode));
    newNode->data = item;
    newNode->link = NULL;
    if (LQ->front == NULL){ // 연결 큐가 공백 상태인 경우
        LQ->front = newNode;
        LQ->rear = newNode;
    }
    else{
        LQ->rear->link = newNode;
        LQ->rear = newNode;
    }
}

// 연결 큐에서 원소를 삭제하고 반환하는 연산
element deQueue(LQueueType *LQ){
    QNode *old = LQ->front;
    element item;
    if (isEmpty(LQ)) return 0;
    else{
        item = old->data;
        LQ->front = LQ->front->link;
        if (LQ->front == NULL) LQ->rear = NULL;
        free(old);
        return item;
    }
}

// 연결 큐에서 원소를 검색하는 연산
element peek(LQueueType *LQ){
    element item;
    if (isEmpty(LQ)) return 0;
    else{
        item = LQ->front->data;
        return item;
    }
}

// 연결 큐의 원소를 출력하는 연산
void printLQ(LQueueType *LQ){
    QNode *temp = LQ->front;
    printf("Linked Queue : [");
    while (temp){
        printf("%3c ", temp->data);
        temp = temp->link;
    }
    printf("]");
}

void main()
{
    LQueueType *Q1 = createLinkedQueue();
    element data;
    printf("\n *** Linked Queue ***\n");
    printf("\n Insert A>>"); enQueue(Q1, 'A'); printLQ(Q1);
    printf("\n Insert B>>"); enQueue(Q1, 'B'); printLQ(Q1);
    printf("\n Insert C>>"); enQueue(Q1, 'C'); printLQ(Q1);
    data = peek(Q1); printf("peek item : %c \n", data);
    printf("\n Delete >>"); data = deQueue(Q1); printLQ(Q1);
    printf("\tDeleted Data : %c", data);
    printf("\n Delete >>"); data = deQueue(Q1); printLQ(Q1);
    printf("\tDeleted Data : %c", data);
    printf("\n Delete >>"); data = deQueue(Q1); printLQ(Q1);
    printf("\tDeleted Data : %c", data);

    printf("\n Insert D>>"); enQueue(Q1, 'D'); printLQ(Q1);
    printf("\n Insert E>>"); enQueue(Q1, 'E'); printLQ(Q1);
}