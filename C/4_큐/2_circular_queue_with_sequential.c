/* 순차 자료구조를 이용한 원형 큐 구현 */
#include <stdio.h>
#include <stdlib.h>
#define cQ_SIZE 4

typedef char element; // 큐 원소의 자료형을 char로 정의
typedef struct {
    element queue[cQ_SIZE]; // 1차원 배열 큐 선언
    int front, rear;
} QueueType;

QueueType* createQueue(){
    QueueType *cQ;
    cQ = (QueueType*)malloc(sizeof(QueueType));
    cQ->front = 0; // front 초깃값 설정
    cQ->rear = 0; // rear 초깃값 설정
    return cQ;
}

// 원형 큐가 공백 상태인지 검색하는 연산
int isEmpty(QueueType *cQ){
    if (cQ->front == cQ->rear){
        printf("Circular Queue is Empty!");
        return 1;
    }
    else return 0;
}

// 원형 큐가 포화 상태인지 검사하는 연산
int isFull(QueueType *cQ){
    if ((cQ->rear+1) % cQ_SIZE == cQ->front){
        printf("Queue is Full!\n");
        return 1;
    }
    else return 0;
}

// 원형 큐의 rear에 원소를 삽입하는 연산
void enQueue(QueueType *cQ, element item){
    if (isFull(cQ)) return; // 포화상태이면 삽입 중단
    else{
        cQ->rear = (cQ->rear+1) % cQ_SIZE;
        cQ->queue[cQ->rear] = item;
    }
}

// 원형 큐의 front에서 원소를 삭제하는 연산
element deQueue(QueueType *cQ){
    if (isEmpty(cQ)) return; // 공백상태이면 삭제 중단
    else{
        cQ->front = (cQ->front+1) % cQ_SIZE;
        return cQ->queue[cQ->front];
    }
}

// 원형 큐의 가장 앞에 있는 원소를 검색하는 연산
element peek(QueueType *cQ){
    if (isEmpty(cQ)) exit(1);
    else return cQ->queue[(cQ->front+1)%cQ_SIZE];
}

// 원형 큐의 원소를 출력하는 연산
void printQ(QueueType *cQ){
    int i;
    int first = (cQ->front+1) % cQ_SIZE;
    int last = (cQ->rear+1) % cQ_SIZE;
    printf("Queue : [");
    i = first;
    while (i != last){
        printf("%3c ", cQ->queue[i]);
        i = (i+1) % cQ_SIZE;
    }
    printf("]\n");
}

void main()
{
    QueueType *Q1 = createQueue();
    element data;
    printf("\n *** Circular Queue ***\n");
    printf("\n Insert A>>"); enQueue(Q1, 'A'); printQ(Q1);
    printf("\n Insert B>>"); enQueue(Q1, 'B'); printQ(Q1);
    printf("\n Insert C>>"); enQueue(Q1, 'C'); printQ(Q1);
    data = peek(Q1); printf("peek item : %c \n", data);
    printf("\n Delete >>"); data = deQueue(Q1); printQ(Q1);
    printf("Deleted Data : %c", data);
    printf("\n Delete >>"); data = deQueue(Q1); printQ(Q1);
    printf("Deleted Data : %c", data);
    printf("\n Delete >>"); data = deQueue(Q1); printQ(Q1);
    printf("Deleted Data : %c", data);

    printf("\n Insert D>>"); enQueue(Q1, 'D'); printQ(Q1);
    printf("\n Insert E>>"); enQueue(Q1, 'E'); printQ(Q1);
}