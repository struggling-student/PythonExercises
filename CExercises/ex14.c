#include<stdio.h>

struct Articolo{
	int codice;
	float prezzo;
};

int main(){
	
	struct Articolo art = {1234, 12.99};
	printf("codice:%d,prezzo:%0.2f \n",  art.codice, art.prezzo);
	
	struct Articolo *p;	
	p = &art;
	p->codice = 567;
	p->prezzo = 3.99;
	
	printf("codice:%d,prezzo:%0.2f \n", art.codice,art.prezzo);

}

