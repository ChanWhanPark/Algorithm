#include <stdio.h>
int main()
{
	int money;
	int coin[4] = { 500, 100, 50, 10 };
	int count = 0;

	printf("�ݾ� �Է�: ");
	scanf("%d", &money);
	for (int i = 0; i < 4; i++) {
		count += money / coin[i];
		money %= coin[i];
	}
	printf("%d��\n", count);
	return 0;
}