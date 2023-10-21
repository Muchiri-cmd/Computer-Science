#include <stdio.h>

void modifyValue(int *value) {
    *value = 100; // Modify the value at the memory location pointed by 'value'
}

int main() {
    int number = 50;
    printf("Before function call: %d\n", number);

    modifyValue(&number);

    printf("After function call: %d\n", number);

    return 0;
}
