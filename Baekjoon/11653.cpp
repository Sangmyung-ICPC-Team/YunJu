#include <stdio.h>
 
int main() {
    int n, m;
    int cnt = 0, min = 0, result = 0;
    
    scanf("%d", &n);
    scanf("%d", &m);
    
    for(int i = n; i <= m; i++) {
    	for(int j = 2; j <= i; j++) {
    		if(i % j == 0)
    			if(i == j) {
    				result += i;
    				cnt++;
    				
    				if(cnt == 1)
    					min = i;
    				break;
				}
				else 
					break;
		}
	}
	if(result == 0)
		printf("-1");
	else
		printf("%d\n%d", result, min);
	
	return 0;
}
