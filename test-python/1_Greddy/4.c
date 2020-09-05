#include <stdio.h>
int main()
{
	int n, k;
	int result = 0;
	scanf_s("%d %d", &n, &k);

	while (n >= k) {
		if (n % k == 0) {
			n /= k;
			result++;
		}
		else {
			n--;
			result++;
		}
	}

	while (n > 1) {
		n--;
		result++;
	}

	printf("%d", result);
}