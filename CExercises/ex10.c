#include<stdio.h>
int main() {
	
	FILE *fp1;
	FILE *fp2;

	char stringa1[50];
	char stringa2[50];

	fp1=fopen("world.txt","r");
	if(fp1!=NULL) {
		while(fscanf(fp1,"%s",stringa1)>0) {
			fp2=fopen("hello.txt","r");
			if(fp2!=NULL) {
				while(fscanf(fp2,"%s",stringa2)>0) {
					fp2=fopen("hello.txt","w");
					if(fp2!=NULL) {
						fprintf(fp2,"%s%s \n",stringa2,stringa1);
				} fclose(fp2);
					fclose(fp1);
			}	
	}
	}
} else {
	printf("Errore nella lettura del file\n");

}
}

