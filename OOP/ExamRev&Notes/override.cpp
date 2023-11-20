#include <iostream>
using namespace std;


class area {
public:
    double dim1, dim2;
    area(double x, double y) {dim1 = x; dim2 = y;}
    // pure virtual function
    virtual double getarea() = 0;
};
class rectangle : public area {
public:
    // function overriding
    double getarea() {
    return dim1 * dim2;
    }
};
class triangle : public area {
public:
    // function overriding
    double getarea() {
    return 0.5 * dim1 * dim2;
    }
};
int main(){

}