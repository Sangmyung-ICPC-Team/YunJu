#include <stdio.h>
#define SIZE 100001
 
int stack[SIZE];

int top = -1;
 
void push(int value) {
    if (top >= SIZE - 1) 
		return;
		
    stack[++top] = value;
}
 
void pop() {
    if (top < 0) 
		return;
		
    stack[top--] = 0;
}
 
int main() {
    int N, value;
    int result = 0;
    
    scanf("%d", &N);
 
    while (N--) {
        scanf("%d", &value);
        
        if (value == 0) 
			pop();
        else push(value);
    }
 
    for (int i = 0; i <= top; i++)
        result += stack[i];
        
    printf("%d\n", result);
    
    return 0;
}
