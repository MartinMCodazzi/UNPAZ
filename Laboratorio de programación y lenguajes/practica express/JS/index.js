const express = require('express');
const app = express();

const PORT = process.env.PORT ?? 3001 ;
const userRoute = require('./src/routes/user.routes');

app.use('/user',userRoute);

console.log()

app.listen(PORT , () => {

})