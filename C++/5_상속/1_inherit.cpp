#include <stdio.h>
#include <string.h>

class Human
{
private:
    char name[12];
    int age;
public:
    Human(const char *aname, int aage){
        strcpy(name, aname);
        age = aage;
    }
    void intro(){
        printf("Name : %s, Age : %d\n", name, age);
    }
};

class Student : public Human{
private:
    int stunum;
public:
    Student (const char *aname, int aage, int astunum) : Human(aname, aage){
        stunum = astunum;
    }
    void study(){
        printf("ABCDEFG\n");
    }
};

int main()
{
    Human kim("Kim", 29);
    kim.intro();
    Student han("Han", 15, 123456);
    han.intro();
    han.study();
}