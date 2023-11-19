#include <iostream>
using namespace std;

class Smartphone{
public:
    virtual void TakeASelfie()=0;
    virtual void MakeACall()=0;
    //whoever inherits this class needs to implelement the selfie functionality
};
class Android:public Smartphone{
public:
    void TakeASelfie(){
        cout << "Android Selfie\n" <<endl;
    }
    void MakeACall(){
        cout << "Android call\n" << endl;
    }

};
class Iphone:public Smartphone{
public:
    void TakeASelfie(){
        cout << "Iphone selfie\n" <<endl;
    }
    void MakeACall(){
        cout << "Iphone call\n" << endl;
    }
};

int main(){

    Smartphone * s1 = new Iphone();//base class pointer to an object of derived class
    s1->TakeASelfie();
    s1->MakeACall();

    Smartphone * s2 = new Android();
    s2->TakeASelfie();
    s2->MakeACall();
    
}