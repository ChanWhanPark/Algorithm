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
        printf("ABCDEFG\n");
    }
};

class Graduate : public Student {
protected:
    char thesis[32];
public:
    Graduate(const char *aname, int aage, int astunum, const char *athesis) : Student(aname, aage, astunum){
        strcpy(thesis, athesis);
    }
    void research(){
        printf("Researching %s\n", thesis);
    }
};

int main()
{
    Graduate moon("Moon", 45, 970204, "C++");
    moon.research();
}