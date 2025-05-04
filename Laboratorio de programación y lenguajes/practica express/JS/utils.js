const lodash = require('lodash');

const flatten = (array) => {
    return lodash.flatten(array);
}

const ultimo = (array) => {
    return lodash.last(array)
}

module.exports = {flatten, ult:ultimo}