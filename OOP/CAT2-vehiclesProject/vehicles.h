#ifndef VEHICLES_H
#define VEHICLES_H
#include <string>

class Vehicle {
private:
    std::string Color;
    std::string Model;
    std::string Make;
    int Price;
    int Mileage;

public:
    //constructor method
    Vehicle(const std::string& color, const std::string& make, const std::string& model, int price, int mileage);


    //destructor 
    ~Vehicle();
    

    //Accessor methods
    void set_color( std::string color );
    std::string get_color();
    void set_model(std::string model);
    std::string get_model();
    void set_make(std::string make );
    std::string get_make();
    void set_price( int price );
    int get_price();
    void set_mileage(int mileage);
    int get_mileage();
    
    //describe car
    void describeCar();

};

#endif