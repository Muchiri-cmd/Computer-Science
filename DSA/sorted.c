#include <stdio.h>

void main()
{
    int i, j;
    int temp; // holding variable
    int num[5];
    //intialize array
    for(i = 0; i <= 4; i++) {
        printf("Enter a number:");
        scanf("%d", &num[i]);
    }
    //sort array
    for (i = 0; i < (4); i++) // element to be compared
    {
        for(j = (i + 1); j < 5; j++) // rest of the elements
        {
            if (num[i] < num[j]) // descending order
            {
                temp = num[i]; // swap
                num[i] = num[j];
                num[j] = temp;
            }
        }
    }
    //print sorted array
    printf("\nSorted array:\n");
    for(i = 0; i <= 4; i++) {
        printf("\t%d\n", num[i]);
    }
    return;
}
