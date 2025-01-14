function find_matching(arr, search){
    let result = [];
    for (let i = 0; i < arr.length; i++){
        let string = arr[i]
        if (string.includes(search)){
            result.push(i);
        }
    }
    return result;
}
console.log(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"));