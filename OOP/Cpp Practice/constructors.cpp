#include <iostream>
using namespace std;
class User{
public:
    string FirstName;
    string LastName;
    int Age;
    string Email;

    //default constructor
    User(){
        FirstName="nn";
        LastName="nln";
        Age=0;
        Email="not set";
    }
    //params constructor
    User(string firstname,string lastname,int age){
        FirstName=firstname;
        LastName=lastname;
        Age=0;
        Email=firstname+"."+lastname+"@mail.com";
    }
};

void GetUserInfo(User u){
    cout<<"First name: "<<u.FirstName <<endl;
    cout<<"Last name: "<<u.LastName <<endl;
    cout<<"Age: "<<u.Age <<endl;
    cout<<"Email: "<<u.Email <<endl;
}

int main()
{
    User user1("saldina","nurak",27);
    GetUserInfo(user1);
    return 0;

}