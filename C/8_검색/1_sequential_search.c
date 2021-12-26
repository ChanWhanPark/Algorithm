/* 정렬되지 않은 자료를 순차 검색 */
#include <stdio.h>
typedef int element;

void sequential_search(element a[], int n, int key){
    int i = 0;
    printf("Search %d ->>", key);
    while (i < n && a[i] != key) i++;
    if (i < n) printf("Step %d Success!\n", i+1);
    else printf("Step %d Fail..\n", i+1);
}

void main()
{
    element a[] = {8, 30, 1, 9, 11, 19, 2};
    int n = 7;

    sequential_search(a, n, 9);
    sequential_search(a, n, 6);

    getchar();
}