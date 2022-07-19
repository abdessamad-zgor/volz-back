const {spawn} = require('node:child_process');
const path = require('path');

let scrapeRunner = (args)=>{
    //spawn child process with python script file
    let childProcess = spawn(`python3 -m scraper.scripts.main`, [...args], {cwd: path.join(__dirname, "../scraper"), env:process.env});
    let output = { }
    childProcess.stdout.on('data', (data)=>{
        output.data = data
    });
    childProcess.stderr.on('data', (data)=>{
        output.error = data
    })
    //return process output
    return output
}



let ArgsChecker = ()=>{
    // checks for valid command line arguments and outputs Errors if invalid
    let args = process.argv
    if (args.length == 1){
        console.log("Error: no arguments provided")
        process.exit(1)
    }
    let isArgumentInvalid = ()=>{
        let valids = 
        args.slice(1).forEach(opt=>{
            
        })
    }
}

// available command line options

let commandLineOptions = [
    {
        syntax: "-l"||"--limit",
        acceptValue:true,
        valueRequired: true,
        valueType: Number.name
    },
    {
        syntax: "-n"||"--name",
        acceptValue: true,
        valueRequired: true,
        valueType: String.name
    },
    {
        syntax: "-a"||"--all",
        acceptValue: false,
        valueRequired: false,
        valueType: undefined
    }
]

module.exports = scrapeRunner;