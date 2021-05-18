#include <stdio.h>
#include <string.h>

int main() {
	int num;
	int count = 0;
	char arr[101];
	
	scanf("%d", &num);
	
	for(int i = 0; i < num; i++) {
		scanf("%s", arr);
		
		int N = 0;
		
		for(int i = 0; i < strlen(arr); i++) {
			for(int j = i + 1; j < strlen(arr); j++) {
				if((arr[i] != arr[i + 1]) && (arr[i] == arr[j]))
					N = 2;
			}
		}
		
		if(N == 0)
			count++;
	}
	
	printf("%d", count);
	
}
