#include<stdio.h>

struct Automobile {
	int prezzo;
	char modello[50];
	float cilindrata;
	char colore[50];
};

int main() {
	struct Automobile veicolo1;

	printf("Inserisci il prezzo : \n");
	scanf("%d", &veicolo1.prezzo);

	printf("Inserisci il modello : \n");
	scanf("%s", veicolo1.modello);

	printf("Inserisci la cilindrata : \n");
	scanf("%f", &veicolo1.cilindrata);

	printf("Inserisci il colore : \n");
	scanf("%s", veicolo1.colore);
	

	printf("Veicolo 1 : Prezzo - %d; Modello - %s, Cilindrata - %0.1f; colore - %s \n",
			veicolo1.prezzo,veicolo1.modello,veicolo1.cilindrata,veicolo1.colore);
}

