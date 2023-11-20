#include <iostream>
using namespace std;

class  Rectangle{
private:
    //members/attributes
    float width;
    float length;
    float area;
public:
//methods
    void setData(float, float);
    void calcArea();
    float getWidth();
    float getLength();
    float getArea();
};
//implimentation
/* setData copies the argument w to private member width and
 l to private member length.*/
void Rectangle::setData(float w, float l)
{
    width = w;
    length = l;
}
/* calcArea multiplies the private members width and length.
The result is stored in the private member area.*/
void Rectangle::calcArea()
{
    area = width * length;
}
// getWidth returns the value in the private member width.
float Rectangle::getWidth(){
    return width;
}
// getLength returns the value in the private member length.
float Rectangle::getLength(){
    return length;
}
// getArea returns the value in the private member area.
float Rectangle::getArea(){
    return area;
}

int main()
{
    Rectangle box;//default constructor
    float wide;
    float length;
    cout << "This program will calculate the area of a\n";
    cout << "rectangle. What is the width? ";
    cin >> wide;
    cout << "What is the length? ";
    cin >> length;
    box.setData(wide, length);
    box.calcArea();
    cout << "Here is the rectangle's data:\n";
    cout << "width: " << box.getWidth() << endl;
    cout << "length: " << box.getLength() << endl;
    cout << "area: " << box.getArea() << endl;
}