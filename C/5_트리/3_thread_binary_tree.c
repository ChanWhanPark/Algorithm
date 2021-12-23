/* 스레드 이진 트리 구현 */
// 자식 노드가 없는 경우 링크 필드를 NULL 포인터 대신 순회 순서상의 다른 노드를 가리킴

#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

typedef struct treeNode {
    char data;
    struct treeNode *left;
    struct treeNode *right;
    int isThreadRight;
} treeNode;

// data를 루트 노드로 하여 왼쪽 서브 트리와 오른쪽 서브 트리를 연결하는 연산
treeNode* makeRootNode(char data, treeNode* leftNode, treeNode* rightNode, int isThreadRight){
    treeNode* root = (treeNode*)malloc(sizeof(treeNode));
    root->data = data;
    root->left = leftNode;
    root->right = rightNode;
    root->isThreadRight = isThreadRight;
    return root;
}

// 후속자 노드를 반환하는 연산
treeNode* findThreadSuccessor(treeNode *p){
    treeNode *q = p->right;
    if (q == NULL) return q;
    if (p->isThreadRight == 1) return q;
    while (q->left != NULL) q=q->left;
    return q;
}

// 스레드 이진 트리의 중위 순회
void threadInorder(treeNode* root){
    treeNode* q;
    q = root;
    while (q->left) q = q->left;
    do {
        printf("%3c", q->data);
        q = findThreadSuccessor(q);
    }while (q);
}

void main()
{
    treeNode* n7 = makeRootNode('D', NULL, NULL, 0);
    treeNode* n6 = makeRootNode('C', NULL, NULL, 1);
    treeNode* n5 = makeRootNode('B', NULL, NULL, 1);
    treeNode* n4 = makeRootNode('A', NULL, NULL, 1);
    treeNode* n3 = makeRootNode('/', n6, n7, 0);
    treeNode* n2 = makeRootNode('*', n4, n5, 0);
    treeNode* n1 = makeRootNode('-', n2, n3, 0);
    // A*B-C/D 수식 구현

    n4->right = n2;
    n5->right = n1;
    n6->right = n3;

    printf("\n thread binary tree inorder : ");
    threadInorder(n1);
}