/* 이진 탐색 트리의 연산 프로그램 */
#include <stdio.h>
#include <stdlib.h>

typedef char element;
typedef struct treeNode {
    char key; // 데이터 필드
    struct treeNode* left; // 왼쪽 서브 트리 링크 필드
    struct treeNode* right; // 오른쪽 서브 트리 링크 필드
} treeNode;

// 이진 탐색 트리에서 키값이 x인 노드의 위치를 탐색하는 연산
treeNode* searchBST(treeNode* root, char x){
    treeNode* p;
    p = root;
    while (p != NULL){
        if (x < p->key) p = p->left;
        else if (x == p->key) return p;
        else p = p->right;
    }
    printf("\nNot Found!");
    return p;
}

// 포인터 p가 가리키는 노드와 비교하여 노드 x를 삽입하는 연산
treeNode* insertNode(treeNode *p, char x){
    treeNode *newNode;
    if (p == NULL){
        newNode = (treeNode*)malloc(sizeof(treeNode));
        newNode->key = x;
        newNode->left = NULL;
        newNode->right = NULL;
        return newNode;
    }
    else if (x < p->key) p->left = insertNode(p->left, x);
    else if (x > p->key) p->right = insertNode(p->right, x);
    else printf("\nKey Exist!!\n");

    return p;
}

// 루트 노드부터 타색하여 키값과 같은 노드를 찾아 삭제하는 연산
void deleteNode(treeNode *root, element key){
    treeNode *parent, *p, *succ_parent, *succ;
    treeNode *child;
    parent = NULL;
    p = root;
    while ((p != NULL) && (p->key != key)) { // 삭제할 노드의 위치 탐색
        parent = p;
        if (key < p->key) p = p->left;
        else p = p->right;
    }

    // 삭제할 노드가 없는 경우
    if (p == NULL){
        printf("No key!\n");
        return;
    }

    // 삭제할 노드가 단말 노드인 경우
    if ((p->left == NULL) && (p->right == NULL)){
        if (parent != NULL){
            if (parent->left == p) parent->left = NULL;
            else parent->right = NULL;
        }
        else root = NULL;
    }

    // 삭제할 노드가 자식 노드를 한 개 가진 경우
    else if ((p->left == NULL) || (p->right == NULL)){
        if (p->left != NULL) child = p->left;
        else child = p->right;

        if (parent != NULL){
            if (parent->left == p) parent->left = child;
            else parent->right = child;
        }
        else root = child;
    }

    // 삭제할 노드가 자식 노드를 두 개 가진 경우
    else{
        succ_parent = p;
        succ = p->left;
        while (succ->right != NULL){
            succ_parent = succ;
            succ = succ->right;
        }
        if (succ_parent->left == succ) succ_parent->left = succ->left;
        else succ_parent->right = succ->left;
        p->key = succ->key;
        p = succ;
    }
    free(p);
}

// 이진 탐색 트리에 대한 중위 순회 연산
void inorder(treeNode* root){
    if (root){
        inorder(root->left);
        printf("%c_", root->key);
        inorder(root->right);
    }
}

void menu()
{
    printf("\n*==================*");
    printf("\n\t1 : Display Tree");
    printf("\n\t2. Insert Data");
    printf("\n\t3 : Delete Data");
    printf("\n\t4 : Search Data");
    printf("\n\t5 : ShutDown");
    printf("\n*==================*");
    printf("\nSelect Menu >> ");
}

int main()
{
    treeNode* root = NULL;
    treeNode* foundedNode = NULL;
    char choice, key;

    root = insertNode(root, 'G');
    insertNode(root, 'I');
    insertNode(root, 'H');
    insertNode(root, 'D');
    insertNode(root, 'B');
    insertNode(root, 'M');
    insertNode(root, 'N');
    insertNode(root, 'A');
    insertNode(root, 'J');
    insertNode(root, 'E');
    insertNode(root, 'Q');

    while(1){
        menu();
        scanf(" %c", &choice);

        switch (choice - '0'){
        case 1: printf("\t[Binary Tree] ");
            inorder(root); printf("\n");
            break;

        case 2: printf("\tInput Key: ");
            scanf(" %c", &key);
            insertNode(root, key);
            break;
        case 3: printf("\tDelete Key: ");
            scanf(" %c", &key);
            deleteNode(root, key);
            break;
        case 4: printf("\tSearch Key: ");
            scanf(" %c", &key);
            foundedNode = searchBST(root, key);
            if (foundedNode != NULL){
                printf("\n Found %c\n", foundedNode->key);
            }
            else printf("\n Not Found\n");
            break;
        case 5: return 0;
        default: printf("Choice Again!\n"); break;
        }
    }
}