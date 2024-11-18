<?php
  $fruits = ['Apple','Orange','Pear'];

  //get length
  echo count($fruits);

  //search array 
  // var_dump(in_array('apple',$fruits));

  //add to array 
  $fruits [] = 'berries';
  print_r($fruits);
  
  //add element to the end of an array
  array_push($fruits,'Mangoes','Bananas','Strawberry');
  print_r($fruits);

  // add element to the beginning of an array
  array_unshift($fruits,'Tangerine','Melon','Pineapple');
  print_r($fruits);

  //remove element from array
  array_pop($fruits);
  print_r($fruits);

  //remove from the front of the array
  array_shift( $fruits );
  print_r($fruits);

  //remove specific fruit at a certain index
  unset($fruits[4]);
  print_r($fruits);

  //split into 2 chunks
  $chunked_array =  array_chunk($fruits,3);
  print_r($chunked_array);

  //concatenate arrays
  $arr1=[1,2,3];
  $arr2=[4,5,6];
  
  $arr3 = array_merge($arr1,$arr2);
  $arr4 = [...$arr1,...$arr2];

  print_r($arr3);
  print_r($arr4);
  

  //combine arrays to dictionary
  $keys = ['username','password'];
  $values = ['davis','rockyou'];

  $user = array_combine($keys,$values);
  print_r($user);

  $keys_array = array_keys($user);
  print_r($keys_array);

  //flip array - keys are values & vice versa
  $flipped = array_flip($user);
  print_r($flipped);


  //array with range of numbers
  $numbers = range(1,20);
  print_r($numbers);

  //map - create new array using map from numbers
  $new_numbers = array_map(function($number){
    return "Number ${number}";
  }, $numbers);

  print_r($new_numbers);

  //filter
  $lessThan10 = array_filter($numbers,fn($number) => $number<=10);
  print_r($lessThan10);

  //reduce
  $sum = array_reduce($numbers, fn($carry,$number) => $carry + $number);

  var_dump($sum);