const {spawn} = require('node:child_process');
const path = require('path');

let scrapeRunner = (args)=>{
    //spawn child process with python script file
    console.log(__dirname)
    console.log(path.resolve(process.cwd(), "../scraper/scraper"));
    let childProcess = spawn(`python3`, [...args], {cwd: path.resolve(process.cwd(), "../scraper"), env:process.env});
    childProcess.stdout.setEncoding('utf8');
    let output = { }
    childProcess.stdout.on('data', (data)=>{
        output.data = data;
        console.log(output.data)
    });
    childProcess.stderr.setEncoding('utf8')
    childProcess.stderr.on('data', (data)=>{
        output.error = data
        console.log(output.error)
    })
    //return process output
    return{ childProcess, output}
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