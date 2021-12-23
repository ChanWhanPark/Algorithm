#include <stdio.h>
#include <string.h>

class Human{
private:
    char name[12];
    int age;

public:
    // 생성자
    Human(const char *aname, int aage){
        strcpy(name, aname);
        age = aage;
    }
    void Intro();
};

void Human::Intro(){
    printf("Name : %s, Age : %d\n", name, age);
}

int main()
{
    // Human kim = Human("KIM", 29); // 명시적 방법
    Human kim("KIM", 29); // 암시적 방법
    kim.Intro();
}