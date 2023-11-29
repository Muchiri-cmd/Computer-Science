#include <iostream>
using namespace std;


int main(){
    int mark;
    int average;
    int marks=0;
    char grade;

    for (int i=0;i<6;i++){
        cout << "Enter Mark: "<<endl;
        cin>>mark;
        marks+=mark;
    }
    average=marks/6;
    cout<<"The average is: "<<average<<endl;
    
    if(average>=70&&average<=100)
        cout<<"A"<<endl;
    else if(average>=60&&average<=69)
        cout<<"B"<<endl;
    else if (average>=50&&average<=59)
        cout<<"C"<<endl;
    else if (average>=40&&average<=49)
        cout<<"D"<<endl;
    else if(average<40)
        cout<<"E"<<endl;
    else
        cout <<"Invalid"<<endl;
    






    return 0;
}