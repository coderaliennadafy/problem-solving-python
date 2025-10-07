#include <stdio.h>

int		max(int* tab, unsigned int len){

    unsigned i;
    int value_max;

    if (len == 0){

        return 0;
    }

    value_max = tab[0];

    i = 1;

    while (i < len){

        if (tab[i] > value_max)

            value_max = tab[i];
            i++;
        }
    return value_max;
}

int main(){

    int array[] = {12,5,9,13,24,6};
    printf("%d\n",max(array,6));
}