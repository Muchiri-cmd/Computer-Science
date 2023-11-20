#include <iostream>
using namespace std;


int main(){
   int count ;
    count = 0;
    while (count < 5)
    {
            cout << count++ << " ";
    }
    cout << "Post Increment Done.\n.\n" << endl ;

    count = 0;
    while (count < 5)
    {
        cout << ++count <<" ";
    }
    cout << "Pre Increment Done " << endl ;
        
}
