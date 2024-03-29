#include <stdio.h>
typedef int element;
int size, i=0;

// 주어진 부분집합 안에서 피봇 위치를 확정하여 분할 위치를 정하는 연산
int partition(element a[], int begin, int end){
    int pivot, L, R, t;
    element temp;
    L = begin;
    R = end;
    pivot = (int)((begin + end) / 2.0); // 중간 위치를 피봇 원소로 선택

    printf("\n [%d Step : pivot = %d] \n", ++i, a[pivot]);
    while (L < R){
        while ((a[L] < a[pivot]) && (L < R)) L++;
        while ((a[R] >= a[pivot]) && (L < R)) R--;
        if (L < R){
            temp = a[L];
            a[L] = a[R];
            a[R] = temp;

            if (L == pivot) pivot = R;
        }
    }
    // L = R인 경우, 더이상 진행이 불가하므로 R 원소와 피봇 원소 자리 교환
    temp = a[pivot];
    a[pivot] = a[R];
    a[R] = temp;
    for (t=0;t<size;t++) printf(" %d", a[t]); // 현재의 정렬 상태 출력
    printf("\n");
    return R;
}

void QuickSort(element a[], int begin, int end){
    int p;
    if (begin < end){
        p = partition(a, begin, end); // 피봇 위치에 의해 분할 위치 결정
        QuickSort(a, begin, p - 1); // 피봇 왼쪽 부분집합에 대해 퀵 정렬 재귀호출
        QuickSort(a, p + 1, end); // 피봇 오른쪽 부분집합에 대해 퀵 정렬 재귀호출
    }
}

void main()
{
    element list[8] = {69, 10, 30, 2, 16, 8, 31, 22};
    size = 8;
    printf("\n [Init State] \n");
    for (int i=0;i<size-1;i++) printf(" %d", list[i]);
    printf("\n");

    QuickSort(list, 0, size-1);

    getchar();
}