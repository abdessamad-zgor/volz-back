
const {FeedListner, FeedProcesser} = require('./utils/feedUtils');
const {CommitItems} = require('./utils/dbUtils');
const scrapeRunner = require('./utils/scraperRunner')

const OrchController = (req, res)=>{
    let args = req.body.params;
    let {childProcess, output} = scrapeRunner(['-m', 'scraper.scripts.main' ,args.keyword, args.limit]);
    
    childProcess.on('exit', (code)=>{
        let data = FeedListner(FeedProcesser);
        res.json(data);
         CommitItems(data)
    })
}

module.exports = OrchController