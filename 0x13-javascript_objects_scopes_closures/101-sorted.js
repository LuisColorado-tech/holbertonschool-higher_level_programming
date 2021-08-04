#!/usr/bin/node
const dict = require('./101-data').dict;
let keys = Object.entries(dict);
const ndict = {};


for (let x of keys) {
    if (!ndict[x[1]]){ 
        
        ndict[x[1]] = [x[0]]

    } else {
    ndict[x[1]].push(x[0])
    }
    //console.log(x[1]);
    
}
console.log(ndict);
