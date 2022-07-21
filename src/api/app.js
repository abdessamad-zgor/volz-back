const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const bodyParser = require('body-parser');

const OrchController = require('./orch');

const app = express();
app.use(morgan('dev'));
app.use(cors());
app.use(helmet());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.route('/api/parse')
.get((req, res)=>{
    res.status(200).json({
        status: 'working',
        name: "volz-back/api"
    })
}).post(OrchController);

module.exports = app