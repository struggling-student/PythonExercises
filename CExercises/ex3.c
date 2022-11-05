#include<stdio.h>

int somma(int a, int b) {
    int risultato;
    risultato = a + b;
    return risultato;
}

int main() {
    int numero1, numero2, risultato;

    printf("Inserisci il primo numero: ");
    scanf("%d", &numero1);

    printf("Inserisci il secondo numero numero: ");
    scanf("%d", &numero2);

    risultato = somma(numero1, numero2);

    printf("La somma è: %d \n", risultato);
    return 0;
}
