#include <stdio.h>

int main() {
    int array[5] = {10, 7, 8, 2, 5};
    int searchValue, index;

    printf("Enter the number to search: ");
    scanf("%d", &searchValue);//8

    for (i = 0; i < 5; i++) {
        if (array[i] == searchValue) {//array[2]=8
            printf("\t\n%d is present at location %d.\n", searchValue, index + 1);
            break;
        }
    }

    if (index == 5) {
        printf("%d is not present in the array.\n", searchValue);
    }

    return 0;
}
