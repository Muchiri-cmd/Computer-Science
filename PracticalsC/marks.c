#include <stdio.h>

int main() {
    int marks;

    printf("Please enter your MARKS: ");
    scanf("%d", &marks);

    if (marks >= 90 && marks <= 100) {
        printf("Your grade is A\n");
    }
    else if (marks >= 80 && marks <= 89) {
        printf("Your grade is B\n");
    }
    else if (marks >= 70 && marks <= 79) {
        printf("Your grade is C\n");
    }
    else if (marks >= 60 && marks <= 69) {
        printf("Your grade is D\n");
    }
    else if (marks > 100) {
        printf("Marks out of range\n");
    }
    else {
        printf("Your grade is F\n");
    }

    return 0;
}

