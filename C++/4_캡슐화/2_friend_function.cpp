#include <stdio.h>

class Date;
class Time{
    friend void OutToday(Date &, Time &);
private:
    int hour, min, sec;
public:
    Time(int h, int m, int s){hour=h;min=m;sec=s;}
};

class Date{
    friend void OutToday(Date &, Time &);
private:
    int year, month, day;
public:
    Date(int y, int m, int d) {year=y; month=m; day=d;}
};

void OutToday(Date &d, Time &t){
    printf("Day : %d %d %d, Time : %d:%d:%d",
    d.year, d.month, d.day, t.hour, t.min, t.sec);
}

int main()
{
    Date d(2018, 06, 29);
    Time t(12, 34, 56);
    OutToday(d, t);
}