#include <iostream>
using namespace std;

class base {
public:
  virtual ~base() {
    cout << "destructing base\n";
    }
};
class derived : public base {
public:
    ~derived() {
        cout << "destructing derived\n";
    }
};

int main() {
    base *p = new derived;
    delete p;
}
//output: destructing derived
//destructuring base