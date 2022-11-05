#include<stdio.h>

struct DataNascita {
	int giorno;
	char mese[50];
	int anno;
};

struct Persona {
	char nome[50]; 
	char cognome[50]; 
	int eta; 
	struct DataNascita dataNascita;
};

int main() {
	
	struct Persona persone[2];

	for(int i=0;i<2;i++) {

		printf("Inserisci il nome: \n");
		scanf("%s",persone[i].nome);
		
		printf("Inserisci cognome: \n");
		scanf("%s",persone[i].cognome);

		printf("Inserisci l'età: \n");
		scanf("%d",&persone[i].eta);

		printf("Inserisci Il giorno della data di nascita: \n");
		scanf("%d", &persone[i].dataNascita.giorno);

		printf("Inserisci il mese della data di nascita: \n");
		scanf("%s", persone[i].dataNascita.mese);

		printf("Inserisci l'anno della data di nascita: \n");
		scanf("%d", &persone[i].dataNascita.anno);
	}
	for(int i=0; i<2;i++) {
		printf("Persona %d : Nome - %s; Cognome - %s; Età - %d; nato il : %d/%s/%d \n", 
				i, persone[i].nome, persone[i].cognome, persone[i].eta,
				persone[i].dataNascita.anno,
				persone[i].dataNascita.mese,
				persone[i].dataNascita.anno);
	}	
}

