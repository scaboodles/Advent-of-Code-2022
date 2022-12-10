function start(){
    const fs = require("fs")
    const input = fs.readFileSync('./testInput.txt', {encoding:'utf8', flag:'r'});
    const splitlines = str => str.split(/\r?\n/);
    const indexesVisited = countRopeMovement(splitlines(input));
    //console.log(indexesVisited);
}

function countRopeMovement(instructions){
    let totalVisited = [];
    let headIndex = {"x": 0 , "y":0};
    let tailIndex = {"x": 0 , "y":0};
    let testMap = [[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."]];

    drawOnMap({"y":0, "x":0}, testMap, "s");
    printMap(testMap);

    for(i=0; i<instructions.length;i++){
        let step = instructions[i];
        let direction = step.match(/\D/)[0];
        let distance = parseInt(step.match(/\**\d+/)[0]);
        let toChange;
        let changeMult;
        switch(direction){
            case "U":
                toChange = "y";
                changeMult = 1;
                break; 
            case "D":
                toChange = "y";
                changeMult = -1;
                break; 
            case "L":
                toChange = "x";
                changeMult = -1;
                break; 
            case "R":
                toChange = "x";
                changeMult = 1;
                break; 
        }
        for(j=0; j<distance; j++){
            headIndex[toChange] += 1 * changeMult;
            tailIndex = updateTailIndex(tailIndex, headIndex);
            if(!checkIfIn(totalVisited, tailIndex)){
                totalVisited.push(Object.assign({}, tailIndex));
                drawOnMap(tailIndex, testMap, "#");
            }
        }
    }
    printMap(testMap);
    return totalVisited.length;
}

function drawOnMap(coords, map, char){
    newMap = map;
    newCoords = Object.assign({}, coords);
    console.log(coords["y"]);
    newCoords["y"] = newMap.length - 1 - parseInt(coords["y"]);
    newMap[newCoords["y"]][newCoords["x"]] = char;
}

function printMap(testMap){
    for(i = 0; i<testMap.length;i++){
        console.log(testMap[i].join(""));
    }
}

function shallowEqual(object1, object2){
    const keys1 = Object.keys(object1);
    const keys2 = Object.keys(object2);
    if (keys1.length !== keys2.length) {
      return false;
    }
    for (let key of keys1) {
      if (object1[key] !== object2[key]) {
        return false;
      }
    }
    return true;
}

function checkIfIn(list, key){
    for(i=0;i<list.length;i++){
        if(shallowEqual(list[i],key)){
            return true;
        }
    }
    return false;
}

function updateTailIndex(tail, head){
    if(shallowEqual(tail, head)){
       return tail; 
    } else if(tail["x"] == head["x"] -2){
        newTail = Object.assign({}, tail);
        newTail["x"] += 1;
        if(tail["y"] != head["y"]){
            if(tail["y"] > head["y"]){
                tail["y"] -= 1;
            }else{
                tail["y"] += 1;
            }
        }
        return newTail;
    } else if(tail["x"] == head["x"] +2){
        newTail = Object.assign({}, tail);
        newTail["x"] -= 1;
        if(tail["y"] != head["y"]){
            if(tail["y"] > head["y"]){
                tail["y"] -= 1;
            }else{
                tail["y"] += 1;
            }
        }
        return newTail;
    } else if(tail["y"] == head["y"] +2){
        newTail = Object.assign({}, tail);
        newTail["y"] -= 1;
        if(tail["x"] != head["x"]){
            if(tail["x"] > head["x"]){
                tail["x"] -= 1;
            }else{
                tail["x"] += 1;
            }
        }
        return newTail;
    } else if(tail["y"] == head["y"] -2){
        newTail = Object.assign({}, tail);
        newTail["y"] += 1;
        if(tail["x"] != head["x"]){
            if(tail["x"] > head["x"]){
                tail["x"] -= 1;
            }else{
                tail["x"] += 1;
            }
        }
        return newTail;
    }

    console.log("tail follow error");

    return tail;
}

start()