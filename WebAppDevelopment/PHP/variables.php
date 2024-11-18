<?php
  //PHP Data Types

  /*
  String - Series of characters surrounded by quotes
  Integer - Whole numbers 
  Float - Decimal Numbers
  Boolean - True or false
  Array - Special variable which can hold more than 1 value 
  Object - A class 
  NULL - Empty Variable
  Resource - Special Variable that holds a resource
  */

  //Variable Rules
  /*
  - Must be prefixed with $
  - Must start with a letter or the underscore
  - cant start with a number
  - can only contain alphanumeric characters and underscores (A-z,0-9 and _)
  - Are case senisitve ($name and $NAME are different variables)
  */

  $name = 'Davis';
  $age = 21;
  $has_money = true;
  $cash_on_hand = 0.00;

  echo $name . ' is  ' .$age . ' years old <br>';
  echo "$name has $cash_on_hand dollars <br>";

  $sum = '5' + '5';
  // echo 10 % 2;

  //constants
  define('HOST','localhost');
  define('DB_NAME','Prod_db');

  echo 'Host:' .HOST . '<br>';
  echo 'DATABASE: ' . DB_NAME . '<br>';


  // var_dump($sum);
  // var_dump( $has_money );
  // var_dump( $cash_on_hand );
  // var_dump($age);
  // var_dump($name);