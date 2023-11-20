#include <iostream>
using namespace std;

class base {
public:
    virtual void show() {
    cout << "base\n";
    }
};
class derived : public base {
    public:
        void show() {
        cout << "derived\n\n";
        }
};

int main(){
    base b1;
    b1.show(); 
    derived d1;
    d1.show();

    base *pb=&b1;
    pb->show();
    pb=&d1;
    pb->show();
}