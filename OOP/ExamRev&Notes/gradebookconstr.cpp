#include <iostream>
using namespace std;


class Gradebook{
private:
    string courseName;
public:
    Gradebook(string name){//constructor
        setCourseName(name);
    }
    void setCourseName(string name){
        courseName=name;
    }
    string getCourseName(){
        return courseName;
    }


    void displayMessage(string courseName){
        cout <<" Welcome to the gradebook for \n"<<courseName<<" !"<<endl;
    }

};
int main(){
    string courseName;
    Gradebook gradebook1("CS101 Intro to C++");
    Gradebook gradebook2("CS102 Object Oriented Programming");
    
    cout << "gradeBook1 created for course: "<<gradebook1.getCourseName()<<endl;
    cout << "gradeBook1 created for course: "<<gradebook2.getCourseName()<<endl;

}