#include<stdio.h>

void inverti(int *p1, int *p2);

int main() {
	
	int a,b;

	printf("Inserisci il primo numero: ");
	scanf("%d", &a);
	printf("Il valore di a: %d \n", a);
	printf("Inserisci il secondo numero: ");
	scanf("%d", &b);
	printf("Il valore di b: %d \n", b);
	inverti(&a,&b);
	printf("Il valore di a: %d \n", a);
	printf("Il valore di b: %d \n", b);

	return 0;
}

void inverti(int *p1, int *p2) {
	int temp;
	temp = *p1;
	*p1 = *p2;
	*p2 = temp;
}

