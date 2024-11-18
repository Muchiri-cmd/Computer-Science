function fib(n){
  if (n <=1 )
    return n
  else
    return res = fib (n - 1) + fib(n - 2)

}

console.log(fib(3))
console.log(fib(7))
console.log(fib(88))