#include "vehicles.h"
#include <iostream>
using namespace::std;

int main()
{
    Vehicle car1 = Vehicle("red","audi","r6",30000,3999);
    cout<<"Initial vehicle1"<<endl;
    cout<<endl;
    car1.describeCar();

    
    //accessor methods
    car1.set_color("green");
    car1.set_make("toyota");
    car1.set_model("corolla");
    car1.set_price(40000);
    car1.set_mileage(300);

    cout<<endl;
    cout<<"vehicle 1 changed attributes"<<endl;

    car1.describeCar();

    cout<<endl;
    cout<<"Vehicle2"<<endl;
    Vehicle car2 = Vehicle("blue","aston martin","s8",29999,546);
    car2.describeCar();
   
   
}