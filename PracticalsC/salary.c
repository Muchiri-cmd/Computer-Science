#include <stdio.h>

int main() {
    float salary, tax_amount;

    // Manually set the salary value
    salary = 4000;

    if (salary > 5000) {
        tax_amount = salary * 1.5;
        printf("Tax charged is %f\n", tax_amount);
    }

    return 0;
}
