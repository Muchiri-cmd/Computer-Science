// This program demonstrates the order in which base and
// derived class constructors and destructors are called.
// For the sake of simplicity, all the class declarations
// are in this file.
#include <iostream>
using namespace std;

// BaseDemo class
class BaseDemo
{
public:
    BaseDemo(void) // Constructor
    { 
        cout << "This is the BaseDemo constructor.\n";
    }
~BaseDemo(void) // Destructor
{ 
    cout << "This is the BaseDemo destructor.\n";
}
};
class DeriDemo : public BaseDemo
{
public:
    DeriDemo(void) //Constructor
    { 
        cout << "This is the DeriDemo constructor.\n"; 
    }
~DeriDemo(void) // Destructor
    { cout << "This is the DeriDemo destructor.\n"; }
};

int main()
{
    cout << "We will now declare a DeriDemo object.\n";
    DeriDemo object;
    cout << "The program is now going to end.\n";
}