/* 원형 연결 리스트 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 원형 연결 리스트의 노드 구조를 구조체로 정의
typedef struct ListNode {
    char data[4];
    struct ListNode* link;
} listNode;

// 리스트 시작을 나타내는 head 노드를 구조체로 정의
typedef struct {
    listNode* head;
} linkedList_h;

// 공백 원형 연결 리스트를 생성하는 연산
linkedList_h* createLinkedList_h(void){
    linkedList_h *CL;
    CL = (linkedList_h*)malloc(sizeof(linkedList_h));
    CL->head = NULL;
    return CL;
}

// 원형 연결 리스트를 순서대로 출력하는 연산
void printList(linkedList_h* CL){
    listNode* p;
    printf(" CL = (");
    p = CL -> head;
    do {
        printf("%s", p->data);
        p = p->link;
        if (p != CL->head) printf(", ");
    } while (p != CL->head);
    printf(")\n");
}

// 첫 번째 노드 삽입 연산
void insertFirstNode(linkedList_h *CL, char *x){
    listNode* newNode, *temp;
    newNode = (listNode*)malloc(sizeof(listNode));
    strcpy(newNode->data, x);
    if (CL->head == NULL){ // 원형 리스트가 공백일 경우
        CL->head = newNode; // 새 노드를 리스트의 시작 노드로 연결
        newNode->link = newNode;
    }
    else{
        temp = CL->head;
        while (temp->link != CL->head) temp = temp->link;
        newNode->link = temp->link;
        temp->link = newNode; // 마지막 노드를 첫 번째 노드인 newNode에 원형 연결
        CL->head = newNode;
    }
}

// pre 뒤에 노드를 삽입하는 연산
void insertMiddleNode(linkedList_h *CL, listNode *pre, char *x){
    listNode* newNode;
    newNode = (listNode*)malloc(sizeof(listNode));
    strcpy(newNode->data, x);
    if (CL == NULL){
        CL->head = newNode;
        newNode->link = newNode;
    }
    else{
        newNode->link = pre->link;
        pre->link = newNode;
    }
}

// 원형 연결 리스트의 pre 뒤에 있는 노드 old를 삭제하는 연산
void deleteNode(linkedList_h* CL, listNode* old){
    listNode* pre; // 삭제할 노드의 선행 노드 포인터
    if (CL->head == NULL) return; // 공백 리스트인 경우 삭제 연산 중단
    if (CL->head->link == CL->head){ // 리스트에 노드가 한 개만 있는 경우
        free(CL->head); // 첫번째 노드의 메모리를 해제
        CL->head = NULL; // 리스트 시작 포인터를 NULL로 설정
        return;
    }
    else if (old == NULL) return; // 삭제할 노드가 없는 경우 삭제 연산 중ㅊ단
    else{
        pre = CL->head; // 포인터 pre를 리스트의 시작 노드에 연결
        while (pre->link != old) {
            pre = pre->link; // 선행자 노드를 포인터 pre를 이용해 찾음
        }
        pre->link = old->link;
        if (old == CL->head) 
            CL->head = old->link;
        free(old);
    }
}

// 원형 연결 리스트에서 x 노드를 탐색하는 연산
listNode* searchNode(linkedList_h* CL, char* x){
    listNode *temp;
    temp = CL->head;
    if (temp == NULL) return NULL;
    do {
        if (strcmp(temp->data, x) == 0) return temp;
        else temp = temp->link;
    }while (temp != CL->head);
    return NULL;
}

int main()
{
    linkedList_h* CL;
    listNode* p;
    CL = createLinkedList_h();
    printf("(1) Create Circular Linked List!\n");
    getchar();

    printf("(2) Insert Node!\n");
    insertFirstNode(CL, "a");
    printList(CL); getchar();

    printf("(3) Insert Node!\n");
    p = searchNode(CL, "a"); insertMiddleNode(CL, p, "b");
    printList(CL); getchar();

    printf("(4) Insert Node!\n");
    p = searchNode(CL, "b"); insertMiddleNode(CL, p, "c");
    printList(CL); getchar();

    printf("(5) Delete Node!\n");
    p = searchNode(CL, "b"); deleteNode(CL, p);
    printList(CL); getchar();

    return 0;
}