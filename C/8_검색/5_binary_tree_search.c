#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#define MAX_WORD_LENGTH 20
#define MAX_MEAN_LENGTH 200

// 영어 사전 항목의 구조 정의
typedef struct {
    char word[MAX_WORD_LENGTH];
    char mean[MAX_MEAN_LENGTH];
} element;

// 영어 사전 이진 트리의 노드 구조 정의
typedef struct treeNode {
    element key;
    struct treeNode* left;
    struct treeNode* right;
} treeNode;

// 포인터 p가 가리키는 노드와 비교하여 항목 key를 삽입하는 연산
treeNode* insertKey(treeNode *p, element key){
    treeNode* newNode;
    int compare;

    // 삽입할 자리에 새 노드를 구성하여 연결
    if (p == NULL){
        newNode = (treeNode*)malloc(sizeof(treeNode));
        newNode->key = key;
        newNode->left = NULL;
        newNode->right = NULL;
        return newNode;
    }

    else{
        compare = strcmp(key.word, p->key.word);
        if (compare < 0) p->left = insertKey(p->left, key);
        else if (compare > 0) p->right = insertKey(p->right, key);
        else printf("\n Same Word\n");

        return p;
    }
}

void insert(treeNode** root, element key){
    *root = insertKey(*root, key);
}

// root 노드부터 탐색하여 key와 같은 노드를 찾아 삭제하는 연산
void deleteNode(treeNode *root, element key){
    treeNode *parent, *p, *succ_parent, *succ;
    treeNode *child;

    parent = NULL;
    p = root;
    while ((p!=NULL) && (strcmp(p->key.word, key.word) != 0)){
        parent = p;
        if (strcmp(key.word, p->key.word) < 0) p = p->left;
        else p = p->right;
    }

    // 삭제할 노드가 없는 경우
    if (p == NULL){
        printf("\n No Word!\n");
        return;
    }

    // 삭제할 노드가 단말 노드인 경우
    if ((p->left == NULL) && (p->right == NULL)){
        if (parent != NULL){
            if (parent->left == p) parent->left = child;
            else parent->right = child;
        }
        else root = child;
    }

    // 삭제할 노드가 자식 노드를 두 개 가진 경우
    else {
        succ_parent = p;
        succ = p->right;
        while (succ->left != NULL){
            succ_parent = succ;
            succ = succ->left;
        }
        if (succ_parent->left == succ){
            succ_parent->left = succ->right;
        }
        else succ_parent->right = succ->right;
        p->key = succ->key;
        p = succ;
    }
    free(p);
}

treeNode* searchBST(treeNode* root, element key){
    treeNode* p;
    int compare;
    p = root;

    while (p != NULL){
        compare = strcmp(key.word, p->key.word);
        if (compare < 0) p = p->left;
        else if (compare > 0) p = p->right;
        else {
            printf("\nWord : %s", p->key.word);
            return p;
        }
    }
    return p;
}

// 이진 탐색 트리를 중위 순회
void inorder(treeNode* root){
    if (root){
        inorder(root->left);
        printf("\n%s : %s", root->key.word, root->key.mean);
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

void main()
{
    char choice;
    element e;
    treeNode *root = NULL, *temp = NULL;

    do{
        menu();
        choice = getchar(); getchar();

        switch (choice - '0'){
        case 1:
            printf("\t[Display Dictionary] ");
            inorder(root); printf("\n\t[End]");
            break;
        case 2: 
            printf("\tInput Word: ");
            gets(e.word);
            printf("\tInput Meaning: ");
            gets(e.mean);
            insert(&root, e);
            break;
        case 3:
            printf("\tDelete Word : ");
            gets(e.word);
            deleteNode(root, e);
            break;
        case 4:
            printf("\nSearch Word : ");
            gets(e.word);
            temp = searchBST(root, e);
            if (temp != NULL) printf("\nWord Meaning : %s", temp->key.mean);
            else printf("\nNo Word!");
            break;
        }
    } while ((choice - '0') != 5);

    getchar();
}