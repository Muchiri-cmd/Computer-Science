#include <iostream>
using namespace std;

int main(){
    int length;
    int width;

    cout<<"Enter the length of the rectangle: "<<endl;
    cin>>length;
    cout<<"Enter the width of the rectangle: "<<endl;
    cin>>width;
    cout << "The perimeter of the rectangle is: "<<(width*2)+(length*2)<<endl;
    cout<< "The Area of the rectangle is: "<<length*width<<endl;

    return 0;

}