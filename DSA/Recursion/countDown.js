function countDown(n){
  for ( let i = n; i > 0; i-- ){
    console.log(i)
  }
  console.log('Hooray')
}

// countDown(5)

function countDownRecursive(n){
  if ( n === 0){
    console.log('Hooray')
    return 
  } else {
    console.log(n)
    return countDownRecursive(n-1)
  }
}

countDownRecursive(5)