#include <stdio.h>
#include <string.h>

class Human{
protected:
    char name[12];
    int age;
public:
    Human(const char *aname, int aage){
        strcpy(name, aname);
        age = aage;
    }
    void eat(){
        puts("EAT");
    }
    virtual void intro(){ // 재정의되는 함수이기 때문에 가상함수로 선언
        printf("Name : %s, Age : %d\n", name, age);
    }
};

class Student : public Human
{
protected:
    int stunum;
public:
    Student(const char *aname, int aage, int astunum) : Human(aname, aage){
        stunum = astunum;
    }
    void intro(){
        printf("%d %s\n", stunum, name);
    }
};

int main()
{
    Human h("Kim", 10);
    Student s("Park", 15, 1234567);
    Human *pH;

    pH = &h;
    pH->intro();
    pH->eat();
    pH = &s;
    pH->intro();
    pH->eat();
}