const express = require ('express');
const app = express();

const path = require('path')
app.use('/public', express.static(path.join(__dirname, 'public')))

app.get('/', (request, response) => {
    response.sendFile(path.join(__dirname, 'public', 'index.html'));
})

const port = 3000;
app.listen(port);

console.log(`Server running on port ${port}`)