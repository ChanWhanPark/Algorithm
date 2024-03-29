# C언어의 확장

### 레퍼런스
레퍼런스는 변수에 대한 별명을 정의하여 이름을 하나 더 붙이는 것으로, 포인터와 유사한 파생형이며 사용하는 방식도 비슷하나 차이가 있다.    

    타입 &변수 = 대상체;

이 경우, 변수와 대상체는 주소가 같기 때문에 두 변수는 **이름만 다른 완전히 같은 변수**다. 주의사항은 다음과 같다.

> 벼령은 같은 타입에 대해 붙이는 것이므로 레퍼런스와 대상체는 타입이 완전히 일치해야 한다.

> 레퍼런스와 대상체는 실제 메모리를 저유하고 있는 좌변값이어야 한다. 

> 레퍼런스 생성 시, 대상체를 분명히 지정해야 한다. 레퍼런스는 처음 생성할 때 누구의 별명인지 명확히 지정해야 하며 NULL 레퍼런스는 인정되지 않는다.

> 레퍼런스는 선언할 때 초기화되어 같은 대상체를 계속 가리키며 실행 중에 참조 대상을 변경할 수 없다.

#### 레퍼런스의 대상체
기본형과 포인터에 대해서 레퍼런스를 선언할 수 있다.
> 레퍼런스에 대한 레퍼런스는 선언할 수 없다.

    int i;
    int &ri = i;
    int &rri = ri; // 불가

> 포인터에 대한 레퍼런스는 가능하지만 역으로 레퍼런스에 대한 포인터는 선언할 수 없다.

    int i;
    int &ri = i;
    int &*pri = &ri; // 불가

> 레퍼런스의 배열도 선언할 수 없다. i,j에 대한 레퍼런스가 필요하면 각각 따로 레퍼런스를 선언해야 한다.

    int i, j;
    int &ra[2] = {i, j}; // 불가

