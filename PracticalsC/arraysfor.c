#include <stdio.h>

int main() {
    int n[10];// n is an array of 10 integers
    int i, j;//declaring variables







    // i   0,  1,  2,  3,  4 , 5,   6,  7,  8,  9 container
    //n=[100,101,102,103,104,105,  106,107, 108, 109  ]; values

    // Initialize elements of the array n
    for (i = 0; i < 10; i++) {
        n[i] = i + 100;
    }








    // Output the value of each array element
    for (j = 0; j < 10; j++) {
        printf("Element[%d] = %d\n", j, n[j]);
    }

    return 0;
}
