#include <iostream>
#include <list>
using namespace std;

class YouTubeChannel {
    //Enacpsulation-Shouldnt be accessible out of method class only thru getters/setters
private:
   
    string email;
    int SubscribersCount;
    list<string> PublishedVideoTitles;

protected:  
       string name;
       int contentQuality;

public:
    YouTubeChannel(string Name,string Email){
        name=Name;
        email=Email;
        SubscribersCount=0;
        contentQuality=0;

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
    void CheckAnalytics(){
        if (contentQuality<=3)
            cout << name << " has bad quality content"<< endl;
        else
            cout << name << " has good quality content" << endl;
    }
};
class CookingYouTubeChannel:public YouTubeChannel{
public:
    CookingYouTubeChannel(string name,string email):YouTubeChannel(name,email) {

    }
    void Practice(){
        cout <<name <<" is Practicing cooking,learning new recipes,experimenting with spices..."<<endl;
        contentQuality++;
    }
};

class SingersYouTubeChannel:public YouTubeChannel{
public:
    SingersYouTubeChannel(string name,string email):YouTubeChannel(name,email) {

    }
    void Practice(){
        cout <<name <<" is taking singing classes,learning new songs,learning how to dance."<<endl;
        contentQuality++;
    }
};

int main(){
    CookingYouTubeChannel cookingYtChannel("Amy's Kitchen","Amy@cook.to");
    SingersYouTubeChannel singersYtChannel("JohnSings","john@song.to");

    cookingYtChannel.Practice();
    singersYtChannel.Practice();
    singersYtChannel.Practice();
    singersYtChannel.Practice();
    singersYtChannel.Practice();

    
    YouTubeChannel * yt1 = &cookingYtChannel;
    YouTubeChannel * yt2 = &singersYtChannel;
    
    yt1->CheckAnalytics();
    yt2->CheckAnalytics();
    //singersYtChannel.CheckAnalytics();
    //cookingYtChannel.CheckAnalytics();
    
}