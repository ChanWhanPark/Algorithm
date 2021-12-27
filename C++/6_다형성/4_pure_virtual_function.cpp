#include <stdio.h>

class Shape{
public:
    virtual void draw() = 0;
    // 순수 가상 함수로 부모 클래스가 동작을 아예 정의하지 않음
    // 파생 클래스에서 재정의 필요
};

class Line : public Shape{
public:
    virtual void draw(){puts("Draw Line.");}
};

class Circle : public Shape{
public:
    virtual void draw(){puts("Draw Circle");}
};

class Rect : public Shape{
public:
    virtual void draw(){puts("Draw Rectangle");}
};

int main()
{
    Shape *pS[3];

    pS[0] = new Line;
    pS[1] = new Circle;
    pS[2] = new Rect;

    for (int i=0;i<3;i++) pS[i]->draw();
    for (int i=0;i<3;i++) delete pS[i];
}