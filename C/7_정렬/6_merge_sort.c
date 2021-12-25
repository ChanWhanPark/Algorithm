#include <stdio.h>
#define MAX 30
typedef int element;
int size;
element sorted[MAX]; // 원소를 병합하면서 정렬한 상태로 저장할 배열 선언

void merge(element a[], int m, int middle, int n){
    int i, j, k, t;
    i = m; // 첫번째 부분집합의 시작 위치 설정
    j = middle + 1; // 두번째 부분집합의 시작 위치 설정
    k = m; // 배열 sorted에 정렬된 원소를 저장할 위치 설정

    while (i <= middle && j <= n){
        if (a[i] <= a[j]){
            sorted[k] = a[i];
            i++;
        }
        else {
            sorted[k] = a[j];
            j++;
        }
        k++;
    }
    if (i > middle) for (t=j;t<=n;t++, k++) sorted[k] = a[t];
    else for (t=i;t<=middle;t++, k++) sorted[k] = a[t];

    for (t=m;t<=n;t++) a[t] = sorted[t];
    printf("\n Merge Sort >> ");
    for (t=0;t<size;t++) printf("%4d ", a[t]);
}

void MergeSort(element a[], int m, int n){
    int middle;
    if (m < n){
        middle = (m + n) / 2;
        MergeSort(a, m, middle); // 앞부분에 대한 분할 작업 수행
        MergeSort(a, middle+1, n); // 뒷부분에 대한 분할 작업 수행
        merge(a, m, middle, n); // 부분집합에 대하여 정렬과 병합 작업 수행
    }
}

void main()
{
    int t;
    element list[8] = {69, 10, 30, 2, 16, 8, 31, 22};
    size = 8;
    printf("\n Sorting Element : ");
    for (t = 0;t < size;t++) printf("%4d ", list[t]);

    printf("\n\n<<<< Merge Sort>>>>\n");
    MergeSort(list, 0, size-1);

    getchar();
}