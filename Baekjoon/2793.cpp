#include <stdio.h>

int main() {
	int num, sum;
	int ans, max, count = 0;
	int arr[100];
	
	scanf("%d %d", &num, &sum);
	ans = sum;
	
	for (int i = 0; i < num; i++)
		scanf("%d", &arr[i]);
		
	for (int i = 0; i < num - 2; i++) {
		for (int j = i + 1; j < num - 1; j++) {
			for (int k = j + 1; k < num; k++) {
				ans = arr[i] + arr[j] + arr[k];
				if (ans <= sum && max < ans)
					max = ans;
			}
		}
	}
	
	printf("%d", max);
	
	return 0;
}


