#include <iostream>
#include <list>
using namespace std;

class YouTubeChannel {
public:
    string name;
    string Email;
    int SubscribersCount;
    list<string> PublishedVideoTitles;
};

int main(){
    YouTubeChannel Channel101;
    Channel101.name="Davis Develops";
    Channel101.Email="davis@dev.com";
    Channel101.SubscribersCount=2100;
    Channel101.PublishedVideoTitles={"Javascript for beginners"};

    cout << "Name" << Channel101.name <<endl;
    cout << "Email" << Channel101.Email <<endl;
    cout << "Subscribers" << Channel101.SubscribersCount << endl;
    cout << "Videos:" <<endl;
    for (string title : Channel101.PublishedVideoTitles){
        cout << title << endl;
    }
}