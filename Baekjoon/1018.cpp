#include <stdio.h>

int main() {

	char arr[50][50];
	int row, col;
	int answer, cnt1, cnt2 = 0;
	int result = 64;
	
	scanf("%d %d", &row, &col);

	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			scanf(" %c", &arr[i][j]);
			
			if (i >= 7 && j >= 7) {
				answer = 0;
				cnt1 = 0;
				cnt2 = 0;
				
				for (int k = i - 7; k <= i; k++) {
					for (int l = j - 7; l <= j; l++) {
						
							if ((i + j) % 2 == (k + l) % 2) {
								if (arr[k][l] != 'B')
									cnt1++;
								else if (arr[k][l] != 'W')
									cnt2++;
							}
							else {
								if (arr[k][l] == 'B') 
									cnt1++;
								else if (arr[k][l] == 'W')
									cnt2++;
							}
					}	
				}
				if (cnt1 < cnt2) 
					answer = cnt1;
				
				else 
					answer = cnt2;
					
				if (result >= answer) 
					result = answer;
				
			}
		}
	}
	
	printf("%d\n", result);
}

