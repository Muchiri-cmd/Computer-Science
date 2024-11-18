function fibsRec(n) {
  if (n <= 0) return []
  if (n === 1) return [0]
  if (n === 2) return [0, 1]
  
  const result = fibsRec(n - 1)
  return [...result, result[result.length - 1] + result[result.length - 2]]
}

console.log(fibsRec(8))