#include <stdio.h>
#include <windows.h> // 윈도우 화면 크기를 조사하는 API 함수 호출

class Shape
{
private:
    int shapeType;
    RECT shapeArea;
    COLORREF color;
public:
    static int scrx, scry;
    static void GetScreenSize();
};

int Shape::scrx;
int Shape::scry;
void Shape::GetScreenSize(){
    scrx = GetSystemMetrics(SM_CXSCREEN);
    scry = GetSystemMetrics(SM_CYSCREEN);
}

int main()
{
    Shape::GetScreenSize();
    Shape C, E, R;
    printf("Shape Size : (%d, %d)\n", Shape::scrx, Shape::scry);
}