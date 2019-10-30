#include <stdio.h>
#include <stdint.h>
#include <getopt.h>
#include <string.h>
#include <errno.h>
#include <time.h>
#include <stdlib.h>

#include "core/typedefs.h"
#include "algorithms/sortalgorithms.h"
#include "core/arraylist.h"
#include "core/pessoa.h"

enum {QUICK_SORT = 0, SELECTION_SORT};

int32_t cmp(void *a, void *b) {
    return strcmp(((pessoa_p)a)->uid, ((pessoa_p)b)->uid);
}

int32_t getAlg(const char *str) {
    if(!strcmp("quick", str)) 
        return QUICK_SORT;
    else if(!strcmp("selection", str))
        return SELECTION_SORT;

    return -1;
}

int main(int argc, char **argv) {
    int option_index;
    char *input, *output, c;
    clock_t time;
    arraylist_t array;
    sorting_algorithm_f sort;
    sorting_algorithm_f algorithms[10];
    static struct option long_options[] = {
        {"algorithm", required_argument, NULL, 'a'},
        {"input",     required_argument, NULL, 'i'},
        {"output",    required_argument, NULL, 'o'},
        {0, 0, 0, 0}
    };

    input = NULL;
    output = NULL;

    algorithms[QUICK_SORT] = quick_sort;
    algorithms[SELECTION_SORT] = selection_sort;

    /* Parse Options ... */
    while((c = getopt_long(argc, argv, "i:o:a:", long_options, &option_index)) != -1)
        switch(c) {
            case 'a':
            {
                /* For now, will always set it to selection_sort, as it's the only one algorthm implemented by now. */
                int32_t alg;
                if((alg = getAlg(optarg)) == -1) {
                    fprintf(stderr, "Algorítimo não implementado: %s\n", optarg);
                    return EXIT_FAILURE;
                }

                sort = algorithms[alg];
                break;
            }
            case 'i':
                /* Linux maximum file name is 256 chars. */
                if((input = calloc(256, sizeof(char))) == NULL) {
                    fprintf(stderr, "Error: %s\n", "Error trying to calloc() input.");
                    return EXIT_FAILURE;
                }
                /* I don't like to use strcpy, because it might cause undefined behavior in some circunstances, but it's easier to use, so I'm going to use it anyway... */
                strcpy(input, optarg);
                /* In case file is small than 256, shrink allocated space. */
                if((input = realloc(input, strlen(input))) == NULL) {
                    fprintf(stderr, "Error: %s\n", "Error trying to realloc() input.");
                    return EXIT_FAILURE;
                }
                break;
            case 'o':
                /* Linux maximum file name is 256 chars. */
                if((output = calloc(256, sizeof(char))) == NULL) {
                    fprintf(stderr, "Error: %s\n", "Error trying to calloc() output.");
                    return EXIT_FAILURE; 
                }
                strcpy(output, optarg);
                /* In case file is small than 256, shrink allocated space. */
                if((output = realloc(output, strlen(output))) == NULL) {
                    fprintf(stderr, "Error: %s\n", "Error trying to realloc() output.");
                    return EXIT_FAILURE;
                }
                break;
        }

    /* Read Data ... */
    {
        FILE *f;
        int r;
        char tmp[2048], *ptr;

        if((f = fopen(input, "rt")) == NULL) {
            free(input);
            free(output);
            fprintf(stderr, "Error:%s", strerror(errno));
            return EXIT_FAILURE;
        }

        arraylist_init(&array, sizeof(pessoa_t), 10, 2);

        //email,gender,uid,birthdate,height,weight
        fscanf(f, "%*s\n");
        
        while((r = fscanf(f, "%s\n", tmp)) != EOF) {
            pessoa_t pessoa;
            INIT_PESSOA(&pessoa);

            ptr = strtok(tmp, ",");
            strcpy(pessoa.email, ptr);

            ptr = strtok(NULL, ",");
            pessoa.gender = *ptr;

            ptr = strtok(NULL, ",");
            strcpy(pessoa.uid, ptr);

            ptr = strtok(NULL, ",");
            strcpy(pessoa.birthdate, ptr);

            ptr = strtok(NULL, ",");
            pessoa.height = atoi(ptr);

            ptr = strtok(NULL, ",");
            pessoa.weight = atoi(ptr);

            if(arraylist_pushback(&array, (void*)&pessoa) != 0) {
                fprintf(stderr, "Error trying to arraylist_pushback()\n");
                return EXIT_FAILURE;
            }
        }

        fclose(f);
    }

    time = clock();
    sort(array.array, array.size-1, array.item_size, cmp);
    time = clock() - time;

    printf("Tempo que levou para ordenar: %f segundos\n", ((double)time)/CLOCKS_PER_SEC);

    {
        for(int i = 0; i < array.size; i++) {
            //printf("%s\n", ((pessoa_p)array.array+i)->uid);
        }
    }

    for(int i = 0; i < array.size; i++) {
        free(((pessoa_p)array.array+i)->email);
        free(((pessoa_p)array.array+i)->uid);
        free(((pessoa_p)array.array+i)->birthdate);
    }

    free(input);
    free(output);

    arraylist_destroy(&array);

    return EXIT_SUCCESS;
}