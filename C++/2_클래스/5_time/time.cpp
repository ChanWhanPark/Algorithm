#include <stdio.h>
#include "time.h"

void Time::SetTime(int h, int m, int s)
{
    hour = h;
    min = m;
    sec = s;
}

void Time::OutTime()
{
    printf("Time : %d:%d:%d\n", hour, min, sec);
}