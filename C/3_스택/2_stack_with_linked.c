#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef int element;

typedef struct stackNode {
    element data;
    struct stackNode *link;
} stackNode;

stackNode* top;

int isEmpty(){
    if (top == NULL) return 1;
    else return 0;
}

// 스택의 top에 원소를 삽입하는 연산
void push(element item){
    stackNode* temp = (stackNode*)malloc(sizeof(stackNode));
    temp->data = item;
    temp->link = top;
    top = temp;
}

// 스택의 top에서 원소를 삭제하는 연산
element pop(){
    element item;
    stackNode* temp = top;

    if (top == NULL){
        printf("\n\n Stack is Empty!\n");
        return 0;
    }
    else{
        item = temp->data;
        top = temp->link;
        free(temp);
        return item;
    }
}

// 스택의 top 원소를 검색하는 연산
element peek(){
    if (top == NULL){
        printf("\n\n Stack is Empty!\n");
        return 0;
    }
    else return top->data;
}

// 스택의 연산을 top에서 bottom 순서로 출력하는 연산
void printStack(){
    stackNode* p = top;
    printf("\n STACK [ ");
    while (p){
        printf("%d ", p->data);
        p = p->link;
    }
    printf("] ");
}

void main()
{
    element item;
    printf("\n** 순차 스택 연산 **\n");
    printStack();
    push(1); printStack();
    push(2); printStack();
    push(3); printStack();

    item = peek(); printStack();
    printf("peed ==> %d", item);

    item = pop(); printStack();
    printf("\t pop ==> %d", item);

    item = pop(); printStack();
    printf("\t pop ==> %d", item);

    item = pop(); printStack();
    printf("\t pop ==> %d", item);

    getchar();
}