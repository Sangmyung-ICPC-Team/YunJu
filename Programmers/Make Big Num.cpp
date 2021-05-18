#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* number, int k) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
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
