#include <stdio.h>

struct SHuman{
    char name[12];
    int age;
};

void IntroHuman(SHuman who){
    printf("Name : %s, Age : %d\n", who.name, who.age);
}

int main()
{
    SHuman kim = {"KIM", 29};
    IntroHuman(kim);
}