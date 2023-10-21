#include <stdio.h>

int main() {
    int i, j;
    int temp; // Temporary holding variable
    int num[5];

    // Input and initialize array
    for (i = 0; i < 5; i++) {
        printf("Enter a number: ");
        scanf("%d", &num[i]);
    }

    // Sort array in descending order
    for (i = 0; i < 4; i++) { // Element to be compared
        for (j = i + 1; j < 5; j++) { // Rest of the elements
            if (num[i] < num[j]) { // Compare for descending order
                temp = num[i]; // Swap
                num[i] = num[j];
                num[j] = temp;
            }
        }
    }

    // Print sorted array
    printf("\nSorted array in descending order:\n");
    for (i = 0; i < 5; i++) {
        printf("\t%d\n", num[i]);
    }

    return 0;
}
