#include <stdio.h>

int main() {
	int result, tmp;
	int cmp = 0;
	char str;
	
	scanf("%d", &result);
	
	while(1) {
		
		scanf("%c", &str);
		
		if(str == '\n') {
			printf("%d", result);
			
			return 0;
		}
		
		scanf("%d", &tmp);
		
		if(cmp == 0) {
			if(str == '+') {
				result += tmp;
			}
			else {
				result -= tmp;
				cmp = 1;
			}
		}
		
		else {
			result -= tmp;
		}
	}

}
