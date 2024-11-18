function sumRange(n){
  let total = 0;
  for ( let i = n ; i > 0 ; i-- ){
    total += i
  }
  return total
}

// console.log(sumRange(2))

function sumRangeRecursive(n,sum=0){
  if ( n <= 0 ){
    return sum
  }
  
  return sumRangeRecursive(n - 1,sum + n)

}

console.log(sumRangeRecursive(3))