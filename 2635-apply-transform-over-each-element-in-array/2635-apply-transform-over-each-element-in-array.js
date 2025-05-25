/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const mutated = []
    for(let i = 0;i < arr.length; i++){
       mutated.push( fn(arr.at(i), i))
   } 
   console.log(mutated)
   return mutated
};