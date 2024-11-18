<?php
  //simple array
  $numbers = [1,5,10,50];
  $fruits = array('Apple','Berries','Cherry');

  print_r($numbers);
  print_r($fruits);

  echo($numbers[1]);
  echo($fruits[2]);
  // var_dump($numbers);

  //Associative arrays
  $french_int = [
    1 => 'Un',
    2 => 'Deux',
    3 => 'Treis',
    4 => 'quatre',
    5 => 'cinq',
    6 => 'six',
    7 => 'sept',
    8 => 'huit',
  ];

  echo $french_int[4];

  $color_codes = [
    'red' => '#ff0',
    'blue' => '#0f0',
    'green' => '#00f',
  ];

  echo($color_codes['green']);

  $person = [
    'first_name'=>'Davis',
    'last_name'=>'Muchiri',
    'email'=>'davismuchiri@gmail.com',
  ];

  echo $person['email'];

  //multi-dimensional arrays
  $people = [
    [
      'first_name'=>'Davis',
      'last_name'=>'Muchiri',
      'email'=>'davismuchiri@gmail.com',
    ],
    [
      'first_name'=>'Tchitchi',
      'last_name'=>'Muchiri',
      'email'=>'tchitchimuchiri@gmail.com',
    ]
  ];

  echo $people[1]['email'];

  var_dump(json_encode(value: $people));
  //json_decode if you want to tuen json object into an array
