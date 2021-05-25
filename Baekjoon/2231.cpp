#include <stdio.h>
 
int main() {
    int num1, count;
	int tmp, result = 0;
	int num2, sum = 0;
	
    scanf("%d", &num1);
    count = num1;
 
    while (count > 0) {
        count /= 10;
        tmp++;
    }
 
    count = num1;
    count = count - tmp * 9;
    if (count < 0) 
		count = 0;
 
    for (int i = count; i <= num1; i++) {
        num2 = i;
       
        sum += num2;
        
        while (num2 > 0) {
            sum += num2 % 10;
            num2 /= 10;
        }
 

        if (sum == num1) {
            result = i;
            break;
        }
        sum = 0;
    }

    printf("%d\n", result);
    
    return 0;
}

