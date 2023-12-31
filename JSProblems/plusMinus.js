/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function plusMinus(arr) {
    let pos = 0;
    let neg = 0;
    let zero = 0;
    let total = arr.length

    // Dont use for-in, use For-Of
    for (let num of arr) {
        if (num > 0) {
            pos ++;
        } else if (num < 0) {
            neg ++;
        } else {
            zero ++;
        }
    }
    console.log(pos/total)
    console.log(neg/total)
    console.log(zero/total)
}

function main() {
    const n = parseInt(readLine().trim(), 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    plusMinus(arr);
}
