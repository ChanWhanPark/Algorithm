/* 이진 검색하기 */
#include <stdio.h>
typedef int element;
int i; // 이진 검색의 연산 횟수

void binarySearch(element a[], int begin, int end, element key){
    int middle;
    i++;
    if (begin == end){
        if (key == a[begin]) printf("Step %d Success!\n", i);
        else printf("Step %d Fail..\n", i);
        return;
    }

    middle = (begin + end) / 2;
    if (key == a[middle]) printf("Step %d Success!\n", i);
    else if (key < a[middle] && (middle-1 >= begin))
        binarySearch(a, begin, middle-1, key);
    else if (key > a[middle] && (middle+1 <= end))
        binarySearch(a, middle+1, end, key);
    else printf("Step %d Fail..\n", i);
}

void main()
{
    element a[] = {1, 2, 8, 9, 11, 19, 29}, key;
    int n = 7;

    i = 0; printf("Search %d ->>", key = 11);
    binarySearch(a, 0, n-1, key);

    i = 0; printf("Search %d ->>", key = 6);
    binarySearch(a, 0, n-1, key);

    i = 0; printf("Search %d ->>", key = 2); i=0;
    binarySearch(a, 0, n-1, key);

}