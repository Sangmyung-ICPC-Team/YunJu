#include <stdio.h>
#define PI 3.14159265358979

int main() {
	int num;
	
	scanf("%d", &num);
	
	printf("%.6f\n", PI*num*num);
	printf("%.6f\n", 2.0*num*num);
	
	return 0;
}
