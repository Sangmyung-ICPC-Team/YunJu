#include <stdio.h>

int main() {
    int arr[3] = {0,};
    int tmp = 0;
    
    while(1) {
        for(int i = 0; i < 3; i++) {
        scanf("%d", &arr[i]);
        }
        
        if(arr[0] == 0 && arr[1] == 0 && arr[2] == 0) {
            break;
        }
        else {
            int max = 0;
            int tmp = 0;
            
            for(int i = 0; i < 3; i++) {
                if(arr[i] > max) {
                    max = arr[i];
                }
            }
            for(int i = 0; i < 3; i++) {
                if(arr[i] != max) {
                    tmp += arr[i] * arr[i];
                }
            }
            
            if(max * max == tmp) {
                printf("right\n");
            }
			else {
                printf("wrong\n");
                }       
            }
    }
    
    return 0;
}
