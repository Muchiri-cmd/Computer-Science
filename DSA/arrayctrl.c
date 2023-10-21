#include <stdio.h>

int main() {
    int i, control2, marks, total = 0, temp;
    float meanmark;

    int allmarks[5];//declaring an array

    // Input and calculation of total marks
    for (i = 0; i < 5; i++) {
        printf("Please enter student's marks: ");
        scanf("%d", &marks);
        allmarks[i] = marks;
        total=total+marks;
    }





    // Calculate the mean mark
    meanmark = (float)total / 5;





    // Bubble sort to sort the marks in ascending order
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++) {
            if (allmarks[0] > allmarks[0 + 1]) {
                temp = allmarks[j];
                allmarks[j] = allmarks[j + 1];
                allmarks[j + 1] = temp;
            }
        }
    }

    // Output sorted marks
    printf("\nThe sorted list of marks is:\n");
    for (control = 0; control < 5; control++) {
        printf("%d\n", allmarks[control]);
    }

    // Output total and mean marks
    printf("\nThe total marks is %d\n", total);
    printf("Mean marks is %.2f\n", meanmark);

    return 0;
}
