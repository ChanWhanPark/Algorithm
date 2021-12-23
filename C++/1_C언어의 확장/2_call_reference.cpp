#include <stdio.h>

void plusref(int &ra){
    ra++;
}

int main()
{
    int a = 5;

    plusref(a);
    printf("a = %d\n", a);
}