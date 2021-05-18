#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// �Ķ���ͷ� �־����� ���ڿ��� const�� �־����ϴ�. �����Ϸ��� ���ڿ��� �����ؼ� ����ϼ���.
char* solution(const char* number, int k) {
    // return ���� malloc �� ���� �Ҵ��� ������ּ���. �Ҵ� ���̴� ��Ȳ�� �°� �������ּ���.
    int len = 0;
    
    for(int i = 0; number[i] != NULL; i++) {
        len++;
    }
    
    char* answer = (char*)malloc(len - k + 1);
    
    int j, ans = 0;
    answer[len - k] = NULL;
    int num = k;
    
    for(int i = 0; i < len - k; i++) {
        for(j = ans + 1; j < num + 1; j++) {
            if(number[ans] < number[j])
                ans = j;
        }
        num++;
        answer[i] = number[ans];
        ans++;
    } 
    
    return answer;
}
