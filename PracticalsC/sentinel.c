#include <stdio.h>

int main() {
    int number;

    printf("Enter numbers (999 to stop):\n");

    while (1) {
        printf("Enter a number: ");
        scanf("%d", &number);

        if (number == 999) {
            printf("Loop terminated.\n");
            break;
        }

        // Process the number or perform desired operations
        printf("Number entered: %d\n", number);
    }

    return 0;
}
