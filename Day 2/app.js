function correctBrackets(str) {
    let stack = [];
    let openBr = ["{", "(", "["];
    let closeBr = ["}", ")", "]"];

    for (let i = 0; i < str.length; i++) {
        let char = str[i];
        if (openBr.includes(char)) {
            stack.push(char)
        }
        else if (closeBr.includes(char)) {
            if (stack.length === 0 || stack.pop() !== reBr(char)) {
                return false
            }
        }
    }

    return stack.length === 0
}

function reBr(inp) {
    if (inp === "}") {
        return "{"
    }
    else if (inp === "]") {
        return "["
    }
    else if (inp === ")") {
        return "("
    }
}

console.log(correctBrackets("{check brackets}"))
console.log(correctBrackets("{Hello Wolrd)}"))