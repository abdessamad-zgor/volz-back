const db = require('../db');
let CommitItems = async(items)=>{
   await db.insertMany(items)
}

module.exports = {CommitItems}