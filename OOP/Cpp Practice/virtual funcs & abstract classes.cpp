#include <iostream>
//defined in base class redefined in direct class
//give u ability of 1 time polymorphism
using namespace std ;

class Instrument{
public:
//virtual- execute the most derived implementation of that function if invoked using a base class
//pure virtual - should force all their derived classes to make an implementation of their derived function n now class becomes abstract
//abstract class - class that has atleast one pure virtual function
    virtual void MakeSound()=0;
};
class Accordion:public Instrument {
public:
    void MakeSound(){
        cout << "Accordion is playing...\n" << endl ;
    }
};
class Piano:public Instrument {
public:
    void MakeSound(){
        cout << "Piano is playing...\n" << endl ;
    }
};


int main()
{
    Instrument * i1=new Accordion();
    //i1->MakeSound();

    Instrument * i2= new Piano();
    //i2->MakeSound();

    //polymorphic nature of virtual functions
    Instrument * instruments[2]={i1,i2};
    for (int i=0;i<2;i++){
        instruments[i]->MakeSound();
    }
    
}   