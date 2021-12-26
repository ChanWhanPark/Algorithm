/* 자료 색인 순차 검색 */
#include <stdio.h>
#define INDEX_SIZE 3
typedef int element;

// 인덱스 테이블의 구조 정의
typedef struct {
    int index;
    element key;
} iTable;

iTable indexTable[INDEX_SIZE];

// 배열 a의 begin 원소와 end 원소 사이에서 key를 순차 검색하기
void sequentialSearch(element a[], int begin, int end, element key){
    int i = 0;
    printf("Search %d ->>", key);
    while (a[i] < key && i < end) i++;

    if (a[i] == key) printf("Step %d Success!\n", (i-begin)+1);
    else printf("Step %d Fail..\n", (i-begin)+1);
}

// 배열 a에 대한 인덱스 테이블 생성
void makeIndexTable(element a[], int size){
    int i, n;
    n = size / INDEX_SIZE;
    if (size % INDEX_SIZE > 0) n++;
    for (i=0;i<INDEX_SIZE;i++){
        indexTable[i].index = i*n;
        indexTable[i].key = a[i*n];
    }
}

// 색인 순차 검색
void indexSearch(element a[], int n, element key){
    int i, begin, end;
    if (key < a[0] || key > a[n-1]) printf("%d Not Exist!!\n");

    // 인덱스 테이블을 검색하여 검색 범위 결정
    for (i=0;i<INDEX_SIZE;i++){
        if ((indexTable[i].key <= key) && (indexTable[i+1].key > key)){
            begin = indexTable[i].index;
            end = indexTable[i+1].index;
            break;
        }
    }
    if (i == INDEX_SIZE){
        begin = indexTable[i-1].index;
        end = n;
    }

    sequentialSearch(a, begin, end, key);
}

void main()
{
    element a[] = {1, 2, 8, 9, 11, 19, 29};
    int n = 7;
    makeIndexTable(a, n);
    indexSearch(a, n, 9);
    indexSearch(a, n, 6);

    getchar();
}