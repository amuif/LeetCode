/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    const wait = (ms)=> new Promise((resolve)=>setTimeout(resolve,ms))
    return wait(millis)
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */