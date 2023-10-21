#include <stdio.h>

int main()
{
    int control, control2, marks, total = 0, temp;
    float meanmark;
    int allmarks[5];

    for (control = 0; control <= 4; control++)
    {
        printf("Please enter student's marks:");
        scanf("%d", &marks);
        allmarks[control] = marks;
        total = total + marks;
    }

    meanmark = (float)total / control;

    for (control = 0; control < 4; control++)
    {
        for (control2 = 0; control2 < 4; control2++)
        {
            if (allmarks[control2] > allmarks[control2 + 1])
            {
                temp = allmarks[control2];
                allmarks[control2] = allmarks[control2 + 1];
                allmarks[control2 + 1] = temp;
            }
        }
    }

    printf("\nThe sorted list of marks is:\n");
    for (control = 0; control <= 4; control++)
    {
        printf("%d\n", allmarks[control]);
    }

    printf("\nThe total marks is %d\n", total);
    printf("Mean marks is %f\n", meanmark);

    return 0;
}
