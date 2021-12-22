/* 이중 연결 리스트를 이용한 데크 구현 */
#include <stdio.h>
#include <malloc.h>

typedef char element;
typedef struct DQNode{
    element data;
    struct DQNode *llink;
    struct DQNode *rlink;
} DQNode;

typedef struct {
    DQNode *front, *rear; // 데크에서 사용하는 포인터 front, rear를 구조체로 정의
} DQueType;

// 공백 데크를 생성하는 연산
DQueType *createDQue(){
    DQueType *DQ;
    DQ = (DQueType*)malloc(sizeof(DQueType));
    DQ->front = NULL;
    DQ->rear = NULL;
    return DQ;
}

// 데크가 공백 상태인지 검사하는 연산
int isEmpty(DQueType *DQ){
    if (DQ->front == NULL){
        printf("\n Linked Queue is empty!\n");
        return 1;
    }
    else return 0;
}

// 데크의 front 앞으로 원소를 삽입하는 연산
void insertFront(DQueType *DQ, element item){
    DQNode *newNode = (DQNode*)malloc(sizeof(DQNode));
    newNode->data = item;
    if (DQ->front == NULL){
        DQ->front = newNode;
        DQ->rear = newNode;
        newNode->rlink = NULL;
        newNode->llink = NULL;
    }
    else{
        DQ->front->llink = newNode;
        newNode->rlink = DQ->front;
        newNode->llink = NULL;
        DQ->front = newNode;
    }
}

// 데크의 rear 뒤로 원소를 삽입하는 연산
void insertRear(DQueType *DQ, element item){
    DQNode *newNode = (DQNode*)malloc(sizeof(DQNode));
    newNode->data = item;
    if (DQ->rear == NULL){
        DQ->front = newNode;
        DQ->rear = newNode;
        newNode->rlink = NULL;
        newNode->llink = NULL;
    }
    else{
        DQ->rear->rlink = newNode;
        newNode->rlink = NULL;
        newNode->llink = DQ->rear;
        DQ->rear = newNode;
    }
}

// 데크의 front 노드를 삭제하고 반환하는 연산
element deleteFront(DQueType *DQ){
    DQNode *old = DQ->front;
    element item;
    if (isEmpty(DQ)) return 0;
    else{
        item = old->data;
        if (DQ->front->rlink == NULL){
            DQ->front = NULL;
            DQ->rear = NULL;
        }
        else{
            DQ->front = DQ->front->rlink;
            DQ->front->llink = NULL;
        }
        free(old);
        return item;
    }
}

// 데크의 rear 노드를 삭제하고 반환하는 연산
element deleteRear(DQueType *DQ){
    DQNode *old = DQ->rear;
    element item;
    if (isEmpty(DQ)) return 0;
    else{
        item = old->data;
        if (DQ->rear->llink == NULL){
            DQ->front = NULL;
            DQ->rear = NULL;
        }
        else{
            DQ->rear = DQ->rear->llink;
            DQ->rear->rlink = NULL;
        }
        free(old);
        return item;
    } 
}

// 데크의 front 노드의 데이터 필드를 반환하는 연산
element peekFront(DQueType *DQ){
    element item;
    if (isEmpty(DQ)) return 0;
    else{
        item = DQ->front->data;
        return item;
    }
}

// 데크의 rear 노드의 데이터 필드를 반환하는 연산
element peekRear(DQueType *DQ){
    element item;
    if (isEmpty(DQ)) return 0;
    else{
        item = DQ->rear->data;
        return item;
    }
}

// 데크의 front 노드로부터 rear 노드까지 출력하는 연산
void printDQ(DQueType *DQ){
    DQNode *temp = DQ->front;
    printf("Deque : [");
    while (temp){
        printf("%3c ", temp->data);
        temp = temp->rlink;
    }
    printf("]");
}

void main()
{
    DQNode *Q1 = createDQue();
    element data;
    printf("\n *** Deque ***\n");
    printf("\n Insert Front A>>"); insertFront(Q1, 'A'); printDQ(Q1);
    printf("\n Insert Front B>>"); insertFront(Q1, 'B'); printDQ(Q1);
    printf("\n Insert Rear C>>"); insertRear(Q1, 'C'); printDQ(Q1);

    printf("\n Delete >>"); data = deleteFront(Q1); printDQ(Q1);
    printf("\tDeleted Data : %c", data);
    printf("\n Delete >>"); data = deleteRear(Q1); printDQ(Q1);
    printf("\tDeleted Data : %c", data);

    printf("\n Insert Rear D>>"); insertRear(Q1, 'D'); printDQ(Q1);
    printf("\n Insert Front E>>"); insertFront(Q1, 'E'); printDQ(Q1);
    printf("\n Insert Front F>>"); insertFront(Q1, 'F'); printDQ(Q1);

    data = peekFront(Q1); printf("peek Front item : %c \n", data);
    data = peekRear(Q1); printf("peek Rear item : %c \n", data);
}