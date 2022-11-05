#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main() {
	int ARRAY_SIZE = 50;
	char *array1 = (char*)malloc(ARRAY_SIZE * sizeof(char));
	if(array1 == NULL) {
		printf("Non è possibile allocare memoria! \n");
		return 0;
	}
	printf("Inserisci la stringa: \n");
	scanf("%s",array1);

	char *array2 = (char*)malloc(ARRAY_SIZE * sizeof(char));
	if(array2 == NULL) {
		printf("Non è possibile allocare memoria! \n");
		return 0;
	}

	printf("Inserisci la stringa: \n");
	scanf("%s",array2);
	
	char *array3 = (char*)malloc(ARRAY_SIZE * sizeof(char));
	if(array3 == NULL) {
		printf("Non è possibile allocare memmoria! \n");
		return 0;
	}
	
	strcpy(array3,strcat(array1, array2));

	printf("%s \n", array3);

	free(array1);
	free(array2);
	free(array3);	

	printf("Memoria liberata correttamente! \n");
	return 0;
}

