#include<stdio.h>

struct Articolo {
	int codice;
	float prezzo;
};

int main() {
	//dichiarazione e inizializzazione
	struct Articolo art1 = { 467, 12.5};
	
	//dichiarazione
	struct Articolo art2;
	//accesso ai campi in scrittura
	art2.codice = 189;
	art2.prezzo = 34.99;

	//accesso ai campi in lettura
	printf("art1 - codice: %d, prezzo: %0.2f \n", art1.codice, art1.prezzo);
	printf("art2 - codice: %d, prezzo: %0.2f \n", art2.codice, art2.prezzo);

}

