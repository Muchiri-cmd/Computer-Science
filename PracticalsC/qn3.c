#include <stdio.h>

int main(){

    //declaring variables
    char outcome;

    //prompt a user to enter his/her outcome
    printf("Enter your outcome: ");
    scanf("%c",&outcome);

    switch (outcome){
    case 'E':
        printf("Exceed Expectation\n");
        break;
    case 'M':
        printf("Met expectation\n");
        break;
    case 'A':
        printf("Approaching Expectation\n");
        break;
    case 'B':
        printf("Below Expectations\n");
        break;

    }
    return 0;
}

program Outcomes;

//Declaring a variable
var
  outcome: char;

begin
  writeln('Enter the outcome (E/M/A/B): ');
  readln(outcome);

  case outcome of
    'E':
      writeln('Meaning: Exceed Expectation');
    'M':
      writeln('Meaning: Met Expectation');
    'A':
      writeln('Meaning: Approaching Expectation');
    'B':
      writeln('Meaning: Below Expectation');
  else
    writeln('Enter a valid outcome (E/M/A/B)');
  end;

  readln;
end.
















