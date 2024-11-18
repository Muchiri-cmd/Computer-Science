<?php

  $y = 21;
  function registerUser($email){
    $x = 10;
    echo "Registering user... ";
    global $y; // to use a global variable in a fun you have to use global varname
    echo $y;

    echo "<br> User registred successfully.<br> Check your email($email) for account activation";

  }
  // echo $x; - error x is defined in scope of the function only
  // registerUser('davismuchiri21@gmail.com');

  function sum ($num1 = 5,$num2 =5){
    return $num1 + $num2;
  }
  echo sum(1,2);

  $total = sum(565,932);
  echo "<br> $total";


  //anonymous function
  $subtract = function($num1,$num2){
    return $num1 - $num2;
  };

  echo '<br>' .$subtract(54,24);
 
  //arrow function
  $multiply = fn($num1,$num2) => $num1 * $num2;
  echo '<br>' .$multiply(5,5);