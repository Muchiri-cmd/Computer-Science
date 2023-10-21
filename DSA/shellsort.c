#include <stdio.h>

void ShellSort(int arr[], int size) {
    int i, d, temp;
    int flag = 1; // Initialize flag for swapping

    d = size; // Initialize d with the size of the array

    while (d > 1 && flag == 1) {
        d = (d + 1) / 2; //size=(5+1)/3
        flag = 0; // Reset flag for each iteration

        for (i = 0; i < (size - d); i++) {
            if (arr[i + d] > arr[i]) {
                temp = arr[i + d]; // Swap positions i+d and i
                arr[i + d] = arr[i];
                arr[i] = temp;
                flag = 1; // Indicates that a swap occurred
            }
        }
    }
}

int main() {
    int num[5] = {5, 2, 9, 1, 5}; // Example array
    int size = sizeof(num) / sizeof(num[0]);

    printf("Original array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", num[i]);
    }

    customSort(num, size);

    printf("\nSorted array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", num[i]);
    }

    return 0;
}
