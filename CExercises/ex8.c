#include<stdio.h>
#include<stdlib.h>

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

	int i = 0;
	int j = 0;
	while (array1[i] != '\0') {
		array3[j] = array1[i];
		i++;
		j++;
	}
	i = 0;
	while (array2[i] != '\0') {
		array3[j] = array2[i];
		i++;
		j++;
	}
	array3[j] = '\0';

	printf("%s \n", array3);

	free(array1);
	free(array2);
	free(array3);

	printf("Memoria liberata correttamente! \n");
	return 0;
}

