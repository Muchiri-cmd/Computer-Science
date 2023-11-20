#include<iostream>
using namespace std;

class Room {
public:
    double length;
    double breadth;
    double height;

    double calculateArea(){
        return length * breadth;
    }
    double calculateVolume(){
        return length * breadth * height;
    }// calculate and display the area and volume

    //constructor function
    Room(int l,int b,int h){
        length=l;
        breadth=b;
        height=h;
    }
};
int main() {
// create object of Room class
/*Room room1;
// assign values to data members
room1.length = 42.5;
room1.breadth = 30.8;
room1.height = 19.2;*/
//using constructor function
Room room1=Room(42.5,30.8,19.2);

cout << "Area of Room = " << room1.calculateArea() << endl;
cout << "Volume of Room = " << room1.calculateVolume() << endl;
};