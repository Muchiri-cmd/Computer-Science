//constructors have same name as class
//constructoes dont have return type
#include <iostream>
#include <list>
using namespace std;

class YouTubeChannel {
    //Enacpsulation-Shouldnt be accessible out of method class only thru getters/setters
private:
    string name;
    string email;
    int SubscribersCount;
    list<string> PublishedVideoTitles;
public:
    YouTubeChannel(string Name,string Email){
        name=Name;
        email=Email;
        SubscribersCount=0;

    }
    void Getinfo(){
   
    YouTubeChannel Channel101("Davisdevelops","davis@dev.to");
    cout << "Name: " << name <<endl;
    cout << "Email:" << email <<endl;
    cout << "Subscribers: " << SubscribersCount << endl;
    cout << "Videos: " <<endl;
    for (string title : PublishedVideoTitles){
        cout << title << endl;
    }
    }
    void Subscribe(){
        SubscribersCount++;
    }
    void Unsubscribe(){
        if(SubscribersCount>0){
            SubscribersCount--;
        }
        
    }
    void PublishVideo(string title){
        PublishedVideoTitles.push_back(title);
    }
};

int main(){
    YouTubeChannel Channel101("Davisdevelops","davis@dev.to");
    Channel101.PublishVideo("Javascript for beginners");
    Channel101.PublishVideo("GO for dummies");
    Channel101.PublishVideo("Python for babies");
    Channel101.Subscribe();
    Channel101.Subscribe();
    Channel101.Subscribe();
    Channel101.Subscribe();
    Channel101.Unsubscribe();
   
    Channel101.Getinfo(); 
}