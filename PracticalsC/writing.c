#include <stdio.h>

int main() {
    FILE *fp;//declaring a varaiable
    fp = fopen("C:\\Users\\pc\\Documents\\test.txt", "w+");
    fprintf(fp, "This is testing for fprintf...\n");
    fputs("This is testing for fputs...\n", fp);
    fclose(fp);

    return 0;
}
