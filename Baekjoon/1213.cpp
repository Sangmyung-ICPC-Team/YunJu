#include <stdio.h>

int main(void) {
	char alp[50] = { 0, };
	char i, j, tmp = 0;
	int arr[26] = { 0, };

	scanf("%s", alp);
	
	for (i = 0; i < 50; i++) {
		arr[alp[i] - 65] += 1;
	}

	for (i = 0; i < 26; i++) {
		if (arr[i] % 2 != 0)
			tmp++;
	}
	
	if (tmp <= 1) {
		for (i = 0; i < 26; i++) {
			for (j = 0; j < arr[i] / 2; j++)
				printf("%c", i + 65);
		}
		
		for (i = 0; i < 26; i++) {
			if(arr[i] % 2 != 0)
				printf("%c", i + 65);
		}
		
		for (i = 25; i >= 0; i--) {
			for (j = 0; j < arr[i] / 2; j++)
				printf("%c", i + 65);
		}
		
		printf("\n");
	}
	
	else
		printf("I'm Sorry Hansoo");
}
