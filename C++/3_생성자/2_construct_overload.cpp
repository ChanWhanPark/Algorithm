#include <stdio.h>

class Time{
private:
    int hour, min, sec;
public:
    // 생성자 1
    Time(int h, int m, int s){
        hour = h;
        min = m;
        sec = s;
    }
    // 생성자 2
    Time(int abssec){
        hour = abssec / 3600;
        min = (abssec / 60) % 60;
        sec = abssec % 60;
    }

    void OutTime();
};

void Time::OutTime(){
    printf("Time : %d:%d:%d\n", hour, min, sec);
}

int main()
{
    Time now(12, 30, 40);
    now.OutTime();
    Time noon(44000);
    noon.OutTime();
}