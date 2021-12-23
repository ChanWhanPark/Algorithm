#include <stdio.h>

struct SHuman{
    char name[12];
    int age;

    void Intro();
};

void SHuman::Intro(){
    printf("Name : %s, Age : %d\n", name, age);
}

int main()
{
    SHuman kim = {"KIM", 29};
    kim.Intro();
}