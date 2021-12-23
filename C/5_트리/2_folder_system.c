/* 후위 순회 이용 폴더 용량 계산하기 */
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

typedef struct treeNode { // 트리의 노드 구조 정의
    int size; // 데이터 필드
    struct treeNode *left;
    struct treeNode *right;
} treeNode;

int FolderSize = 0;

// size를 루트 노드로 하여 왼쪽 서브 트리와 오른쪽 서브 트리를 연결하는 연산
treeNode* makeRootNode(int size, treeNode* leftNode, treeNode* rightNode){
    treeNode* root = (treeNode*)malloc(sizeof(treeNode));
    root->size = size;
    root->left = leftNode;
    root->right = rightNode;
    return root;
}

// 각 폴더 크기를 계산하기 위한 후위 순회 연산
int postorder_FolderSize(treeNode* root){
    if (root) {
        postorder_FolderSize(root->left);
        postorder_FolderSize(root->right);
        FolderSize += root->size;
    }
    return FolderSize;
}

void main()
{
    treeNode* F11 = makeRootNode(120, NULL, NULL);
    treeNode* F10 = makeRootNode(55, NULL, NULL);
    treeNode* F9 = makeRootNode(100, NULL, NULL);
    treeNode* F8 = makeRootNode(200, NULL, NULL);
    treeNode* F7 = makeRootNode(68, F10, F11);
    treeNode* F6 = makeRootNode(40, NULL, NULL);
    treeNode* F5 = makeRootNode(15, NULL, NULL);
    treeNode* F4 = makeRootNode(2, F8, F9);
    treeNode* F3 = makeRootNode(10, F6, F7);
    treeNode* F2 = makeRootNode(0, F4, F5);
    treeNode* F1 = makeRootNode(0, F2, F3);

    printf("\n\n C drive : %d M\n", postorder_FolderSize(F2));
    FolderSize = 0;
    printf("\n\n D drive : %d M\n", postorder_FolderSize(F3));
    FolderSize = 0;
    printf("\n\n Whole Size : %d M\n", postorder_FolderSize(F1));
    
}