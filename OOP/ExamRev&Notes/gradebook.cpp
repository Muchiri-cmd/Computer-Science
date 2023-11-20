#include <iostream>
using namespace std;


class Gradebook{
public:
    void displayMessage(string courseName){
        cout <<" Welcome to the gradebook for \n"<<courseName<<" !"<<endl;
    }

};
int main(){
    string courseName;
    Gradebook myGradeBook;
    cout << " Please Enter Course Name"<<endl;
    cin >> courseName;
    myGradeBook.displayMessage(courseName);
}