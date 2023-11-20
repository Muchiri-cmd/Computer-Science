#include <iostream>
using std::string;

class AbstractEmployee {
    //any class that signs this contract has to provide implementation for this method
    virtual void AskForPromotion()=0;
};
class Employee:AbstractEmployee {
    //members or attributes of the class.Private by default
    //types of modifiers r Public,Private and Protected
//private:(default)
protected:
       string Name;
private:
    string Company;
    int Age;
public:
    void setName(string name){//setter
        Name=name;
    }
    string getName(){//getter
        return Name;
    }
    void SetCompany(string company){
        Company=company;
    }
    string getCompany(){
        return Company;
    }
    void setAge(int age){
        if (age>=18){
              Age=age;
        }
    }
    int getAge(){
        return Age;
    }

    //describe behaviours of an employee.Using class methods
    void IntroduceYourself(){
        std::cout<<"Name - "<<Name << std::endl;
        std::cout<<"Company - "<<Company << std::endl;
        std::cout <<"Age - "<<Age << std::endl;
    }
    Employee(string name, string company,int age){
        Name=name;
        Company=company;
        Age=age;

    }
    void AskForPromotion(){
        if(Age>30)
            std::cout<< Name << "got promoted!" <<std ::endl;
        else
            std::cout<< Name <<" sorry NO promotion for you!"<<std::endl;
    }
    virtual void Work(){
        std::cout<<Name<<" is checking email,tasklog and doing tasks"<<std::endl;
    }
};

class Developer:public Employee {
public:
    string Language;
    Developer(string name,string company,int age,string language)
        :Employee(name,company,age)
        {
            Language=language;
        }
        void Tasks(){
            std::cout<<Name<< " fixed bug using "<<Language<<std::endl;
        }
        void Work(){
        std::cout<<Name<<" is writing "<<Language<<" code"<<std::endl;
        }
       
};

class Teacher:public Employee {
public:
    string Subject;
    Teacher(string name,string company,int age,string subject)
    :Employee(name,company,age)
    {
        Subject=subject;
    }
    void PrepareLesson(){
        std::cout<<Name<< " is preparing "<<Subject<<" lesson"<<std::endl;
    };
    void Work(){
        std::cout<<Name<<" is teaching "<<Subject<<std::endl;
    }
};
//The most common use of polymorphism is when a 
//parent class reference is used to refer to a child class object
int main()
{
    /*Employee employee1;//user defined var type Employee.Object of class Employee
    employee1.Name="Davis";
    employee1.Company="Davis&Shirtliff";
    employee1.Age=20;
    employee1.IntroduceYourself();*/
    
    Employee employee1=Employee("Davis","Davis&Shirtliff",20);
    Employee employee2=Employee("James","ICT Authority",34);
    /*employee1.IntroduceYourself();
    employee1.setAge(15);
    std::cout<<employee1.getName()<<" is "<<employee1.getAge()<<" years old";
    employee1.AskForPromotion();
    employee2.AskForPromotion();*/
    
    
    Developer dev1=Developer("Jake the Brogrammer","Devslopes",25,"Rust");
    /*dev1.Tasks();
    dev1.Tasks();
    dev1.Tasks();
    dev1.AskForPromotion();*/
    //dev1.Work();
    Teacher t=Teacher("Nana","Tech World",30,"Devops");
    /*t.PrepareLesson();
    t.AskForPromotion();*/
    //t.Work();
    Employee* e1=&dev1;
    Employee* e2=&t;

    e1->Work();
    e2->Work();
    
}