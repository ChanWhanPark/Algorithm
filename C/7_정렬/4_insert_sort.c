#include <stdio.h>
typedef int element;
int size;

// 삽입 정렬
void InsertionSort(int a[], int size){
    int i, j, t, temp;
    printf("\n Sorting Element : ");
    for (t = 0;t < size;t++) printf("%d ", a[t]);
    printf("\n\n<<<< Insertion Sort >>>>\n");
    for (i=1;i<size;i++){
        temp = a[i];
        j = i;
        while ((j > 0) && (a[j-1] > temp)){
            a[j] = a[j-1];
            j = j - 1;
        }
        a[j] = temp;
        printf("\n %d Step : ", i);
        for (t=0;t<size;t++) printf("%3d ", a[t]);
    }
}

void main()
{
    element list[8] = {69, 10, 30, 2, 16, 8, 31, 22};
    size = 8;
    InsertionSort(list, size);

    getchar();
}