#include <stdio.h>

class Fahrenheit;
class Celsius{
public:
    double tem;
    Celsius(){}
    Celsius(double aTem): tem(aTem) {}
    operator Fahrenheit();
    void OutTem(){
        printf("%f'C\n", tem);
    }
};

class Fahrenheit{
public:
    double tem;
    Fahrenheit(){}
    Fahrenheit(double aTem): tem(aTem) {}
    operator Celsius();
    void OutTem(){
        printf("%f'F\n", tem);
    }
};

Celsius::operator Fahrenheit()
{
    Fahrenheit F;
    F.tem = tem * 1.8 + 32;
    return F;
}

Fahrenheit::operator Celsius()
{
    Celsius C;
    C.tem = (tem - 32) / 1.8;
    return C;
}

int main()
{
    Celsius C(100);
    Fahrenheit F = C;
    C.OutTem();
    F.OutTem();

    printf("\n");
    Fahrenheit F2(120);
    Celsius C2 = F2;
    F2.OutTem();
    C2.OutTem();
}