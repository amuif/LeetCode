/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
 value = 0
var createCounter = function(init) {
    let num = init
    console.log(num)
    return {
        increment:function(val){
            return ++num
        },
        decrement:function(val){
            return --num
        },
        reset:function(val){
            return (num = init)
        }
    }
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */