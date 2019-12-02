/*
Exercicio resolvido: uva_10264 - The most potent corner
Autores: Leonardo Laia Arpini, Harrison Sanches, Mathues Garcias
*/

#include <stdio.h>
#include <stdlib.h>

#define is_power2(v1, v2) (((v1^v2)&(-(v1^v2)))==(v1^v2))

int main() {
    int N, V, i, j, maximum, *p, weight;
    while(scanf("%d", &N) != EOF) {
        V = 1 << N;
        p = calloc(V, sizeof(int));
        maximum = 0;
        for(i = 0; i < V; i++) {
            scanf("%d", &weight);
            for(j = 0; j < V; j++) 
                if(is_power2(i, j) && i != j) 
                    p[j] += weight;
        }
        for(i = 0; i < V; i++) {
            for(j = 0; j < V; j++) {
                if(!is_power2(i, j) || i == j)
                    continue;
                maximum = (((maximum)>(p[i]+p[j]))?(maximum):(p[i]+p[j]));
            }
	    }
        printf("%d\n", maximum);
        free(p);
    }
    return 0;
}
