#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
	char *ptr;

	if(argc < 3) {
		printf("Usage: %s <environment var> <target program name>\n", argv[0]);
		exit(-1);
	}

	ptr = getenv(argv[1]); /* Get env var location. */
	ptr += (strlen(argv[0]) - strlen(argv[2]))*2; /* Adjust for program name. */
	printf("%s will be at %p\n", argv[1], ptr);
	exit(0);
}
