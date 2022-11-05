#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char *concat(char *s1, char *s2);

int main() {

	char s1[30] = "prima parte";
	char s2[30] = "seconda parte";
	char *p1;
	char *p2;

	p1 = &s1[0];
	p2 = &s2[0];

	char *ris = concat(p1, p2);
	printf("%s", ris);
	free(ris);
	return 0;
}

char *concat(char *s1, char *s2) {

	int l1 = 0;
	int l2 = 0;
	while(*s1 != '\0') {
		l1 += 1;
		s1++;
	}

	while(*s2 != '\0') {
		l2 += 1;
		s2++;
	}

	s1 = s1 - l1;
	s2 = s2 - l2;

	//printf("%d \n", l1);
	//printf("%d \n", l2);

	char *s3 = malloc((l1 + l2 + 1) * sizeof(char));
	if (s3 == NULL) {
		printf("Allocation error !");
		exit(0);
	}

	for (int i = 0; i < l1; i++) {
		*(s3 + i) = *s1;
		s1++;
	}

	for (int i = l1; i < (l1 + l2); i++) {
		*(s3 + i) = *s2;
		s2++;
	}

	*(s3 + (l1+l2)) = '\0';

	return s3;

}

