#include <iostream>
using namespace std;

class base {
public:
    int i;
    base (int x) { i = x; }
    virtual void func() {cout << i; }
};
class derived : public base {
public:
      derived (int x) 
        : base (x) 
        {}
      void func() {cout << i * i; } 
};

int main(){
    base ob(10), *p;
    derived d_ob(10);
    
    p = &ob;
    p->func(); // use base’s func()
    p = &d_ob;
    p->func(); // use derived’s func()
}