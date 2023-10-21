#include <stdio.h>

// Function definition
int max(int num1, int num2)
{

    if (num1 > num2)
        int greater = num1;
    else
        int greater = num2;

    return greater;
}




// Function declaration
int max(int , int );

int main()
{
    int a, b;

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    int greater = max(a, b);

    printf("The maximum of %d and %d is: %d\n", a, b, maximum);

    return 0;
}
