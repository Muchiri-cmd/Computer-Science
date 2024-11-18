<?php
  $string = 'Hello world';

  //get length of a string
  echo strlen($string);

  //find position of first occurrence of a substring in a string
  echo strpos($string,'o');

  //find position of last occurrence of a substring in a string 
  echo strrpos($string,'o');

  //Reverser a string
  echo strrev($string);

  //conver to lowercase
  echo strtolower(($string));

  //convert to uppercase
  echo strtoupper($string);

  //convert uppercase of each first letter
  echo ucwords($string);

  //string replace
  echo str_replace('world','There',$string);

  //return portion of string specified by offser and length
  echo substr($string,0,5);
  echo substr($string,5);

  //check if string starts with
  if(str_starts_with($string,'Hello')){
    echo 'true';
  }

  //check if strinf ends with
  if(str_ends_with($string,'world')){
    echo 'true';
  }

  $string2 = '<script>alert("you have been hacked")</script>';
  echo htmlspecialchars($string2);

  //formatted string
  printf('%s likes to %s','Davis','code');
  printf('1+1=%d',1+1);