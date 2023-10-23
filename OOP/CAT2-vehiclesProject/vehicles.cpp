#include <iostream>
#include "vehicles.h"

//constructor method
Vehicle::Vehicle(const std::string& color, const std::string& make, const std::string& model, int price, int mileage) {
    // Constructor implementation
    Color = color;
    Make = make;
    Model = model;
    Price = price;
    Mileage = mileage;
}

//destructor
Vehicle::~Vehicle(){
    //none
}
    //Accessor methods
    void Vehicle::set_color(std::string color) {
    Color = color;
}

std::string Vehicle::get_color() {
    return Color;
}

void Vehicle::set_model(std::string model) {
    Model = model;
}

std::string Vehicle::get_model() {
    return Model;
}

void Vehicle::set_make(std::string make) {
    Make = make;
}

std::string Vehicle::get_make() {
    return Make;
}

void Vehicle::set_price(int price) {
    Price = price;
}

int Vehicle::get_price() {
    return Price;
}

void Vehicle::set_mileage(int mileage) {
    Mileage = mileage;
    if (Mileage < 1)
        std::cout << "Invalid mileage. It can't be negative " << std::endl;
}

int Vehicle::get_mileage() {
    return Mileage;
}


    //describe car
    void Vehicle::describeCar(){
        std::cout<<"Color - "<< Color<< std::endl;
        std::cout<<"Make - "<< Make<< std::endl;
        std::cout<<"Model - "<< Model<< std::endl;
        std::cout<<"Price - "<< Price<< std::endl;
        std::cout<<"Mileage - "<< Mileage<< std::endl;
    }

