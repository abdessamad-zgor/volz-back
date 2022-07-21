const fs = require('fs');
const path = require('path');


let FeedListner = (cb)=>{
    let data;
    let feedStream = fs.createReadStream(path.join(__dirname, '../../../scraper/scraper/items.jsonl'));
    feedStream.on('error', function (error) {
        console.log(`error: ${error.message}`);
    });
    feedStream.on('data', (data)=>{
        
        data = cb(data);
    })
    feedStream.on('end', ()=>{
        console.log('feed end')
    });
    return data;
    
}

let FeedProcesser = (file)=>{
    let items = [];
    let lineReader = require('node:readline').createInterface({
        input: file,
        crlfDelay: Infinity
    });
    for (const line of lineReader){
        items.push(line)
    }
    return items
} 

module.exports= {
    FeedListner,
    FeedProcesser
}