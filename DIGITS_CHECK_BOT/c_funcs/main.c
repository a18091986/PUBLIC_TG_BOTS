#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void print_answer_to_file(int * arr, int size) {
    FILE *file = NULL;
    file = fopen("answer.txt", "a");
    for (int i = 0; i < size; i++) {
        if (i == size - 1)
            fprintf(file, "%d", arr[i]);
        else
            fprintf(file, "%d ", arr[i]);
    }
    fprintf(file, "\n\n");
    fclose(file);
}


void is_simple_check (int number) {
    printf("%d\n", number);
    FILE *file = NULL;
    file = fopen("answer.txt", "a");
    fprintf(file, "- простое, т.е. делится только на 1 и на само себя\n\n");
    fclose(file);



    int * arr = NULL;
    arr = (int *) malloc(1 * sizeof(int));
    int arr_size = 1;
    printf("%d\n", arr_size);
    for (int i = 1; i <= number; i++) {
        if ((number % i) == 0) {
            arr = (int *) realloc(arr, (arr_size + 1)*sizeof(int));
            arr[arr_size-1] = i;
            arr_size++;
//            if (i != number) arr_size++;
        }

    arr[arr_size-1] = number;
    }
//    FILE *file = NULL;
//    file = fopen("answer.txt", "a");
//    if (arr_size != 2) {
//        fprintf(file, "- делится на: ");
//        fclose(file);
////        print_answer_to_file(arr, arr_size);
//    } else {
//        fprintf(file, "- простое, т.е. делится только на 1 и на само себя\n\n");
//        fclose(file);
//    }
    free(arr);
}

void is_fibo_check (int number) {
    FILE *file = NULL;
    file = fopen("answer.txt", "a");
    switch (number) {
    case 0:
        fprintf(file, "- 1 член ряда Фибоначчи\n\n");
        break;
    case 1:
        fprintf(file, "- 2 член ряда Фибоначчи\n\n");
        break;
    default: 
        int f_el = 0;
        int s_el = 1;
        for (int i = 3; i <= 70; i++) {
            int current = f_el + s_el;
            f_el = s_el;
            s_el = current;
            if (current == number) {
                fprintf(file, "- %d член ряда Фибоначчи\n\n", i);
                break;
            }
            else if (current > number) {
                fprintf(file, "- не принадлежит к ряду чисел Фибоначчи\n\n");
                break;
            }
        }  
    }
    fclose(file);  
}

int main(int argc, char * argv[]) {
    if (argc!=2) {
        printf("Not enough arguments count\n\n");
        exit(1);
    }
    int income_number = atoi(argv[1]);
    FILE *file = NULL;
    file = fopen("answer.txt", "w");
    fprintf(file, "--------------- %d ---------------\n\n", income_number);
    fclose(file);
    is_simple_check(income_number);
    is_fibo_check(income_number);
    return 0;
}
