<?php
  /* --------------- For loop ---------------------- */

  /* 
    for (initialize; condition;increment){
      code
    }
  */
  echo '<h3>Numbers</h3>';
  for($x = 0; $x<=10 ; $x++ ){
    echo 'Number ' . $x . '<br>';
  }

/*
  ============================= while loop
  while(condition){

  }
*/
$x=0;
while( $x<10 ){
  echo $x .',';
  $x+=2;
}

/* 
  ============================ do while 
  do {
    code
  } while(condition)
*/
$x=10;
do {
  echo $x .',';
  $x-=2;
} while($x>=0);

/* 
  ========================= for each loop 
  foreach($array as value){
    code
  }
*/

$cars = ['Mustang Shelby','Nissan Skyline','Dodge Challenger'];
//count - counts length of array 
echo '<h3> Cars </h3>';
forEach($cars as $index => $car){
  echo '<br>'. $index . ' - ' .$car;
}

$person = [
  'name' => 'Davis',
  'username' => 'capalot',
  'email' => 'davismuchiri21@gmail.com'
];
echo '<h3>User</h3>';
foreach($person as $key => $value){
  echo '<br>'. $key .' - ' . $value;
}