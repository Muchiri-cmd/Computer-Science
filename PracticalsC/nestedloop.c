#include <stdio.h>

int main() {
    int rows = 3;
    int columns = 4;

    // Nested for loop
    for (int i = 0; i < rows; i++) {

        for (int j = 0; j < columns; j++) {
            printf("(%d, %d) ", i, j);
        }
        printf("\n");
    }

    return 0;
}
