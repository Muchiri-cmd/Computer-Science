// This program demonstrates a destructor.
#include <iostream>
using namespace std;

class Demo
{
public:
    Demo(void); // Constructor
    ~Demo(void); // Destructor
};
//constructor
Demo::Demo(){
cout << "Welcome to the constructor!\n";
}
//destructor
Demo::~Demo(){
cout << "The destructor is now running.\n";
}

int main(){
    Demo demoobj;
    cout << "This program demonstrates an object\n";
    cout << "with a constructor and destructor.\n";
}