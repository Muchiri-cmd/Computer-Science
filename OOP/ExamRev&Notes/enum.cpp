#include <iostream>
using namespace std;

enum week { Sunday, Monday, Tuesday, Wednesday,
Thursday, Friday, Saturday };
int main()
{
    week today;
    today = Wednesday;
    cout << "Day " << today+1;//returns 4 (Wedenesday is day 4)
    return 0;
}