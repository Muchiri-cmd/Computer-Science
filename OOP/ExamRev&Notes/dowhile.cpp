#include <iostream>
using namespace std;


int main(){
    int ans;
    do
    {
        cout << "Choose a number from 1 to 4: "; // repeated action
        cin >> ans;
        
    } while (ans >= 1 && ans <= 4); // test expression(number 1->4 inclusive)
    cout << "Done";
        
}
