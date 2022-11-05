#include <stdio.h>
#include <string.h>

void modificaStringa(char *array[]);

int main() {

    char array[20];

    printf("Inserisci una stringa: ");
    scanf("%s", array);
    modificaStringa(array);
    //risultato = modificaStringa(array);
    
    return 0;

}

void modificaStringa(char *array[]) {
    // ho la stringa Ciao123
    // deve diventare Ciao***
    int i;
    int length = (int)strlen(array);
    for(i=0;i<length;i++){
        printf("%c", array[i]);
    }
    //return array;
}
