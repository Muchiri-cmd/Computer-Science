#include <iostream>
using namespace std;

class Book{
public:
    string Title;
    string Author;
    int* Rates;
    int RatesCounter;

    Book(string title,string author){
        Title=title;
        Author=author;
        RatesCounter=2;
        Rates=new int[RatesCounter];
        Rates[0]=4;
        Rates[1]=5;

        cout << Title + "constructor invoked\n"<<endl;
    }
    ~Book(){
        delete [] Rates;
        Rates=nullptr;
        cout << Title + "destructor invoked\n"<<endl;
    }

};
int main()
{
    Book book1("Millionaire FastLane","M.J. Demarco");
    Book book2("C++ Lambda Story","Bartek Filipek");
}