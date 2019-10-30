//
// Created by hsanches on 16/10/2019.
//


#include <sys/types.h>
#include <stdint.h>
#include <stdio.h>


int vet[] heapsort(int vector[], int size_vector){
    for (i = tam; i <= -1; i--){
        Maxheapify(int vector[]), size_vector,i);
    }

    for (i = size_vector-1,0,-1){
        troca = vector[i];
        vector[i] = vector[0];
        vetcor[0] = troca;
        Maxheapify(int vector[],i,0)

    }
}

void Maxheapify(int [],size_vector,indice){
    maior = indice;
    direita = 2 * indice +1;
    esquerda = 2 * esquerda + 2;
    
    if (direita < size_vector && vector[direita] > vector[indice]){
        maior = direita;
    }

    if (esquerda < size_vector  && vector[esquerda] > vector[maior]){
        maior esquerda;
    }

    if (maior != indice) {
        troca = vector[indice];
        vector[indice = vector[maior]
        vector[maior] = troca;
        Maxheapify(int vector[],size_vector,indice);
    }
            
}