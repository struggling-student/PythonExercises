// Scrivere un programma che legge una
// linea di testo e stampa la somma dei numeri
// contenuti nella linea. Ad esempio se la linea è
// "L'appuntamento è alle 18:40 del 2/11/2010", allora
// il programma stampa 2081 (2081 =
// 18+40+2+11+2010).

#include<stdio.h>
#include <string.h>
int main() {
    
    char string[100];
    int count, sum = 0;

    printf("Inserisci la stringa \n");
    scanf("%s", string);
    for (count = 0; count != strlen(string); count++){
        printf("Carratter: %c\n", string[count]);
    }
    printf("Somma numeri nella stringa = %d\n", sum);
}
