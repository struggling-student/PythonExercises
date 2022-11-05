#include<stdio.h>
#include<string.h>
typedef struct Libro {
	char titolo[50];
	float prezzo;
}Libro;

int controlloLibri(Libro L1, Libro L2);

int main() {
	Libro libro1, libro2;
	printf("Libro 1 Titolo: \n");
	scanf("%s",libro1.titolo);
	printf("Libro 1 Prezzo: \n");
	scanf("%f",&libro1.prezzo);
	printf("Libro 2 Titolo: \n");
	scanf("%s",libro2.titolo);
	printf("Libro 2 Prezzo: \n");
	scanf("%f",&libro2.prezzo);

	if(controlloLibri(libro1,libro2)==0) printf("I libri sono uguali!");
	else printf("I libri sono diversi!\n");
	return 0;
}

int controlloLibri(Libro L1, Libro L2) {
	if ( (L1.prezzo==L2.prezzo) && (strcmp(L1.titolo,L2.titolo)==0) ) {
		return 0;
	}
	return 1;
}

