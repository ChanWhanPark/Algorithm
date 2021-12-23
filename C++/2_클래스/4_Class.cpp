#include <stdio.h>

class SHuman
{
public: // 외부에서 접근 불가
    char name[12];
    int age;
    void intro();
};

void SHuman::intro(){
    printf("Name : %s, Age : %d\n", name, age);
}

int main()
{
    SHuman kim = {"KIM", 29};
    kim.intro();
}