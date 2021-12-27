#include <stdio.h>
#include <string.h>

class Date{
protected:
    int year, month, day;
public:
    Date();
    Date(int y, int m, int d){year=y;month=m;day=d;}
    void OutDate(){printf("%d/%d/%d", year, month, day);}
};

class Product : private Date { // private 상속
private:
    char name[64];
    char company[32];;
    int price;
public:
    Product(const char *aname, const char *acompany, int y, int m, int d, int aprice) : Date(y, m, d){
        strcpy(name, aname);
        strcpy(company, acompany);
        price = aprice;
    }

     void OutProduct(){
        printf("Name : %s\n", name);
        printf("Product : %s\n", company);
        printf("Date : ");
        OutDate();
        puts("");
        printf("Price : %d\n", price);
    }
};

int main()
{
    Product shrimp("Shi", "Nong", 2020, 8, 15, 900);
    shrimp.OutProduct();
}