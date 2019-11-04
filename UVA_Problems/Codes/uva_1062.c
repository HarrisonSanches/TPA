#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int find(char *stacks, char value, int qt) {
    int i;
    for(i = 0; i <= qt; i++)
        if(stacks[i] >= value)
            return i;
    return -1;
}

int main() {
    char str[1000];
    int kase;

    kase = 0;

    scanf("%s\n", str);
    while(str[0] != 'e') {
        int i, i_stack, len;
        char stacks[1000];

        i_stack = 0;
        len = strlen(str);
        stacks[i_stack] = str[0];

        for(i = 0; i < len; i++) {
            int index;
            if((index = find(stacks, str[i], i_stack)) == -1)
                stacks[++i_stack] = str[i];
            else 
                stacks[index] = str[i];    
        }
        
        printf("Case %d: %d\n", ++kase, i_stack+1);
        scanf("%s\n", str);
    }
    return 0;
}
