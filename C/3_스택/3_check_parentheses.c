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

int testPair(char *exp){
    char symbol, open_pair;
    // char형 포인터 매개변수로 받은 수식 exp의 길이를 계산하여 length 변수에 저장
    int i, length = strlen(exp);
    top = NULL;

    for (i=0;i<length;i++){
        symbol = exp[i];
        switch (symbol){
        case '(':
        case '[':
        case '{':
            push(symbol); break;
        case ')':
        case ']':
        case '}':
            if (top == NULL) return 0;
            else{
                // 스택에서 마지막으로 읽은 괄호를 꺼냄
                open_pair = pop();
                // 괄호 쌍이 맞는지 검사
                if ((open_pair == '(' && symbol != ')') || (open_pair == '[' && symbol != ']') || (open_pair == '{' && symbol != '}')){
                    // 괄호 쌍이 틀리면 수식 오류
                    return 0;
                }
                else break; // 괄호 쌍이 맞으면 다음 symbol 검사를 계속함
            }
        }
    }
    if (top == NULL) return 1; // 수식 검사를 마친 후 스택이 공백이면 1을 반환
    else return 0;
}

void main()
{
    char* express = "{(A+B)-3}*5+[{cos(x+y)+7}-1]*4";
    printf("%s", express);

    if (testPair(express) == 1){
        printf("\n\nCorrect!\n");
    }
    else{
        printf("\n\nIncorrect!\n");
    }
}