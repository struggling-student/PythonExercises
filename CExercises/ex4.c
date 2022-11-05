#include<stdio.h>

int minimo(int array[], int lunghezza);

int main() {
    int i,len,risultato;
    int array[5];
    for (i=0; i<5; i++) {
        printf("Inserire alla posizione %d il valore: ", i);
        scanf("%d", &array[i]);
    }
    len = sizeof(array)/sizeof(array[0]);
    risultato = minimo(array, len);
    printf("Il minimo è: %d \n", risultato);

    return 0;
}

int minimo(int array[], int lunghezza) {
    int i,val;
    int min = array[0];
    for (i=1; i<lunghezza; i++){
        val = array[i];
        if (val < min) {
            min = val;
        }
        else {
            // do nothing
        }
    }
    return min;
}



