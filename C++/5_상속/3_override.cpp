#include <stdio.h>
#include <string.h>

class Human
{
protected:
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
protected:
    int stunum;
public:
    Student(const char *aname, int aage, int astunum) : Human(aname, aage){
        stunum = astunum;
    }
    void study(){
        printf("ABCDEF\n");
    }
    void intro(){
        printf("%d %s\n", stunum, name);
    }
};

int main()
{
    Human kim("kim", 29);
    kim.intro();
    Student han("han", 15, 123456);
    han.intro();
}