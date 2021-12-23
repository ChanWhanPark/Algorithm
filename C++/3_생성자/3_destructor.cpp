#include <stdio.h>
#include <string.h>

class Human{
private:
    char *pname;
    int age;
public:
    Human(const char *aname, int aage){
        pname = new char[strlen(aname)+1];
        strcpy(pname, aname);
        age = aage;
        printf("%s constructor\n", pname);
    }

    ~Human(){
        printf("%s destructor\n", pname);
        delete[] pname;
    }

    void Intro();
};

void Human::Intro(){
    printf("Name : %s, Age : %d\n", pname, age);
}

int main()
{
    // Human kim = Human("KIM", 29); // 명시적 방법
    Human kim("KIM", 29); // 암시적 방법
    kim.Intro();
}