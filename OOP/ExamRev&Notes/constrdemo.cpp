// This program demonstrates a constructor.
#include <iostream>
using namespace std;

class Demo
{
public:
    Demo(void);
};
 // Constructor
Demo::Demo(void)
{
    cout << "Welcome to the constructor!\n";
}
   
int main()
    {
    Demo demoObj;
    // Declare a Demo object;
    cout << "This program demonstrates an object\n";
    cout << "with a constructor.\n";
}