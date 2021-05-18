#include <stdio.h>
#include <string.h>

int main() {
	int tmp, cmd = 0;
	char arr[100005] = { 0 };
	
	gets(arr);
	
	int len = strlen(arr);
	
	for(int i = 0; i <= len; i++) {
		if (arr[i] == '\0')
			return 0;
				
		if(arr[i] == '<') {
			while(1) {
				printf("%c", arr[i]);
				
				i++;
				
				if(arr[i] == '>') {
					printf(">");
					
					tmp = i + 1;
					break;
				}
			}
		}
		
		else if(arr[i + 1] == ' ' || arr[i + 1] == '\0' || arr[i + 1] == '<') {
			cmd = i;
			
			for(int j = cmd; j >= tmp; j--) {
				printf("%c", arr[j]);
			}
			tmp = i + 1;
		}
		else if(arr[i] == ' ') {
			printf(" ");
			tmp++;
		}
	}
	
	printf ("\n");
	
	return 0;
}
