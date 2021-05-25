#include <stdio.h>

int movie(int n) {
	int count = 0;
	
	while(n) {
		if(n % 10 == 6) {
			count++;
			if(count == 3) {
				return 1;
			}
		}
		else {
			count = 0;
		}
		n /= 10;
	}
	return 0;
}

int main() {
	int num, tmp = 0;
	
	scanf("%d", &num);
	
	for(int i = 0; i < 10000000; i++ ) {
		if(movie(i)) {
			tmp++;
			if(num == tmp) 
				printf("%d", i);
				
		}
	}
	
	return 0;
}
