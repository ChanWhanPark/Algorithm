/* 전치행렬 (Transposed Matrix) 연산 */
#include <stdio.h>

typedef struct {
    int row;
    int col;
    int value;
} term;

void smTranspose(term a[], term b[]){
    int m, n, v, i, j, p;
    m = a[0].row;
    n = a[0].col;
    v = a[0].value; // 행렬 a의 행, 열, 0이 아닌 원소 수
    b[0].row = n;
    b[0].col = m;
    b[0].value = v; // 행렬 b의 행, 열, 0이 아닌 원소 수
    if (v > 0){
        p = 1;
        for (i=0;i<n;i++){ // 희소 행렬 a의 열별로 전치 반복 수행
            for (j=0;j<=v;j++){ // 0이 아닌 원소 수에 대해서만 반복 수행
                if (a[j].col == i){ // 현재의 열에 속하는 원소가 있으면 b[]에 삽입
                    b[p].row = a[j].col; 
                    b[p].col = a[j].row; 
                    b[p].value = a[j].value;
                    p++;
                }
            }
        }
    }
}