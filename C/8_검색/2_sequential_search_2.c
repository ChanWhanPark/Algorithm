/* 정렬된 자료를 순차 검색하기 */
#include <stdio.h>
typedef int element;

void sequential_search(element a[], int n, element key){
    int i = 0;
    printf("Search %d ->>", key);
    while (a[i] < key) i++;
    if (a[i] == key) printf("Step %d Success!\n", i+1);
    else printf("Step %d Fail..\n", i+1);
}

void main()
{
    element a[] = {1, 2, 8, 9, 11, 19, 29};
    int n = 7;

    sequential_search(a, n, 9);
    sequential_search(a, n, 6);

    getchar();
}