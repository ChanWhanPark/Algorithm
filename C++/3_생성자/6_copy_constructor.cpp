#include <stdio.h>
#include <string.h>

class Human
{
private:
    char *pname;
    int age;
public:
    Human(const char *aname, int aage){
        pname = new char[strlen(aname) + 1];
        strcpy(pname, aname);
        age = aage;
    }
    Human(const Human &other){ // 복사 생성자
        pname = new char[strlen(other.pname) + 1];
        strcpy(pname, other.pname);
        age = other.age;
    }
    ~Human(){
        delete []pname;
    }
    void intro(){
        printf("Name : %s, Age : %d\n", pname, age);
    }
};

void printHuman(Human who){
    who.intro();
}

int main()
{
    Human kang("Kang", 1424);
    Human boy = kang;
    printHuman(boy);
}