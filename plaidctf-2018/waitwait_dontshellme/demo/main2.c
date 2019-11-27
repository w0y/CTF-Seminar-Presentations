#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <fcntl.h>

extern char __executable_start;
const char* flag_file_name = "flag.txt";

extern void demo2 (void);

int main (int argc, char** argv) {
	printf("code located at: 0x%lx\n", (unsigned long)&__executable_start);
	printf("flag file name is: %s\n", flag_file_name);
	printf("flag file name located at: %p\n", flag_file_name);
	printf("Executing Demo1\n");
	printf("Closing stdin & stdout\n");
	fclose(stdin);
	fclose(stdout);
	demo2();
	printf("Goodbye.\n");
	return EXIT_SUCCESS;
}
