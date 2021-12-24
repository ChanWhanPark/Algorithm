#include <stdio.h>
#include <string.h>

class Human
{
private:
    char name[12];
    int age;

public:
    Human(){ // 디폴트 생성자로서 무난한 값으로 초기화
        strcpy(name, "No Name");
        age = 0;
    }
    void intro(){
        printf("Name : %s, Age : %d\n", name, age);
    }
};

int main()
{
    Human momo;
    momo.intro();
}