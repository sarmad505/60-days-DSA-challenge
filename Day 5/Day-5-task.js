/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if(x < 0) return false;
    x = x.toString()
    var i = 0;
    var j = x.length - 1;
    while(i < j){
        if(x[i] !== x[j]) return false;
        i++;
        j--;
    }
    return true;
};