const express = require("express");
const app = express();
var myPythonScriptPath = 'script.py';
const {PythonShell} =require('python-shell');
app.post('/hola', function (req, res) {
    res.send('[POST]Saludos desde express');
});
app.get('/hola', function (req, res) {
    PythonShell.run(myPythonScriptPath, null, function (err, result){
        if (err) throw err;
        // result is an array consisting of messages collected
        //during execution of script.
        console.log('result: ', result.toString());
        res.send(result.toString())
  });
});
app.listen(3000, () => {
    console.log("El servidor está inicializado en el puerto 3000");
});