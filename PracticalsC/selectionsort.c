#include <stdio.h>

void selectionSort(int arr[], int size) {
    int i, j, first, temp;


    // 5, 2, 9, 1, 5
    for (i = size - 1; i > 0; i--) {
        first = 0; // stores index of current smallest element
        for (j = 1; j <= i; j++) {
            if (arr[j] < arr[first])2<5
                first = j;
        }
        temp = arr[first]; // Swap smallest found with element in position i.
        arr[first] = arr[i];
        arr[i] = temp;
    }
}

int main() {
    int num[5] = {5, 2, 9, 1, 5}; // Example array
    int size = sizeof(num)  / sizeof(num[0]);

    printf("Original array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", num[i]);
    }

    selectionSort(num, size);//calling the function selection sort

    printf("\nSorted array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", num[i]);
    }

    return 0;
}
