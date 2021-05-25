#include<stdio.h>

int main() {
    int num, count = 0;
    int x[51];
    int y[51];
    
    scanf("%d", &num);
    
    for(int i = 0; i < num; i++) {
        scanf("%d %d", &x[i], &y[i]);
    }
    
    for(int i = 0; i < num; i++) {
       	count = 1;
       	
        for(int j = 0; j < num; j++) {
            if(x[i] < x[j] && y[i] < y[j])
             count++;       
        }
        printf("%d ", count);
    }
}
