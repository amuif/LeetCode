/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function (...args) {
    let output = 0
    // console.log(args.length)
    for (let i = 0; i < args.length; i++) {
        output = output + 1
    }
    return output

};

/**
 * argumentsLength(1, 2, 3); // 3
 */