const fs = require('fs');
const path = require('path');


let FeedListner = (cb)=>{
    let feedStream = new fs.createReadStream(path.join(__dirname, '../../../scraper/scraper/items.jsonl'));
    feedStream.on('error', function (error) {
        console.log(`error: ${error.message}`);
    });
    feedStream.on('data', (data)=>{
        
        cb(data);
    })
}

let FeedProcesser = (file)=>{
    let items = [];
    let lineReader = require('node:readline').createInterface({
        input: file,
        crlfDelay: Infinity
    });
    for await (const line of lineReader){
        items.push(line)
    }
    return items
} 

module.exports= {
    FeedListner,
    FeedProcesser
}