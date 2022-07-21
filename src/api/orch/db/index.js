const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/').then()

const ProductSchema = new mongoose.Schema({
    title : String,
    price: String,
    link: String,
    imageURI: String,
});

module.exports = mongoose.model('product', ProductSchema);