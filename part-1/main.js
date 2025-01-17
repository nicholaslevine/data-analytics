function sum_equation(arr){
    let sum = arr.reduce((sum, current) => sum + current, 0);
    let strings = arr.join(" + ");
    return `${strings} = ${sum}`

}
console.log(sum_equation([1, 5, 7]))