#include <stdio.h>

int add(int a, int b);

int main() {
    int a, b, sum;

    printf("Enter the first integer: ");
    scanf("%d", &a);

    printf("Enter the second integer: ");
    scanf("%d", &b);

    sum = add(a, b);

    printf("The sum of the two numbers is %d\n", sum);

    return 0;
}

int add(int a, int b) {
    int result;
    result = a + b;
    return result;
}
