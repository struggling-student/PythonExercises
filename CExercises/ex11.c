#include<stdio.h>
#include<stdlib.h>

int voto_alto(int array[], int lunghezza);
int voto_basso(int array[], int lunghezza);
int media(int array[], int lunghezza);

int main() {
	FILE *fp;
	
	char nome[50];
	char cognome[50];
	int voto;

	int numeri_voti=0;	
	int voti[50];

	fp=fopen("voti.txt","r");
	if(fp!=NULL) {
		int i = 0;
		while(fscanf(fp,"%s %s %d",nome,cognome,&voto)>0) {
			voti[i] = voto;
			i++;
			numeri_voti++;
			printf("%s %s %d \n", nome,cognome,voto);

		}			
			fclose(fp);
		} else {
			printf("Error opening the file \n");
	}
	int votomin = voto_basso(voti,numeri_voti);
	int votomax = voto_alto(voti, numeri_voti);
	int med = media(voti, numeri_voti);

	printf("il voto più basso: %d \n", votomin);
	printf("Il voto più alto: %d \n", votomax);
	printf("la media : %d \n", med);
}


int voto_basso(int array[], int lunghezza) {
	int votomin = array[0];
	for(int i = 1; i<lunghezza; i++) {
		int val = array[i];
		if( val < votomin) {
			votomin = val;
		} else {
			// do nothing
		}
	}
	return votomin;
}

int voto_alto(int array[], int lunghezza) {
	int votomax = array[0];
	for(int i = 1; i<lunghezza; i++) {
		int val = array[i];
		if( val > votomax) {
			votomax = val;
		} else {
			// do nothing
		}
	}
	return votomax;
}

int media(int array[], int lunghezza) {
	int somma = 0;
	for(int i = 0; i<lunghezza; i++) {
		somma += array[i];
	}
	int med = somma / lunghezza;
	return med;

}

