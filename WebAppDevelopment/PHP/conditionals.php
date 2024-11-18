<?php
  /*
  < less than 
  > Greater than
  <= less than or equal to
  >= Greater than or equal to
  == Equal to
  === Identical to (both value and type matches)
  != Not equal to
  !== Not identical to
  */

  /* 
    if statement syntax
    if (condition){
      code
    }
  */

  $t = date("H");

  if($t < 12){
    echo " Good Morning. ";
  } elseif($t < 16){
    echo "Good afternoon";
  }
  else {
    echo "Good evening. ";
  }

  $age = 18;
  if ($age>=18){
    echo "You are eligible for services offered - ";
  } else {
    echo "Sorry, you have not reached the eligible age to access our services. ";
  }

  $services = ['Helb','Fuliza','Voting'];

  //empty - checks if a variable is empty i.e doesnt contain values
  // if(!empty($services)){
  //   echo $services[0];
  // } else {
  //   echo 'No Services currently';
  // }

  //ternary operator
  echo !empty($services) ? $services[0] : 'No Services currently';

  //coalesing operator
  $notifications = [' <br> Welcome <br>'];
  echo $notifications[0] ?? null ;

  $num = 5;
  //switch 
  switch($num){
    case 1:
      echo 'un';
      break;
    case 2:
      echo 'deux';
      break;
    case 3:
      echo 'treis';
      break;
    case 4:
      echo 'quatre';
      break;
    case 5:
      echo 'cinq';
      break;
  }
