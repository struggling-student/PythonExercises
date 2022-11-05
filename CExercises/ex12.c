#include<stdio.h>
#include<string.h>

int main() {
	FILE *fp;
	char parola[50];
	char stringa[] = "ciao";
	int num=0;
	fp=fopen("sample.txt","r");
	if(fp!=NULL) {
		int i = 0;
		while(fscanf(fp,"%s",parola)>0) {
			if(strcmp(parola, stringa)==0) {
				num++;
			 }
		}
	}
	printf("La stringa compare all'interno del file : %d volte \n", num);
}	

