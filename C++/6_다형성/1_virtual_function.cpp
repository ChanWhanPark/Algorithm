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
    virtual void intro(){ // 가상으로 선언하여 포인터의 동적 타입을 따른다.
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
    void intro(){
        printf("%d %s", stunum, name);
    }
    virtual void study(){
        printf("ABCDEFG\n");
    }
};

void IntroSomeBody(Human *pH){ // 넘기는 객체 포인터에 따라 다른 intro() 함수 호출
    pH->intro();
}

int main()
{
    Human h("Kim", 10);
    Student s("Lee", 15, 1234567);

    IntroSomeBody(&h);
    IntroSomeBody(&s);
}