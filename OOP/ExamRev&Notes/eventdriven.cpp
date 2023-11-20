#include <iostream>
using namespace std;


int main(){
   double salary;
    cout << "Enter you salary: ";
    //sentinel controlled eg. cout << Enter -1 to exit"(Salary cant be negative)
    cin >> salary;
    int years = 0;
    while (salary < 50000) {
        salary = salary * 1.02;
        years++;
    }
    cout << "You need " << years << "years to get to 50K";
        
}
