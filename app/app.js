const express = require("express");
const app = express();
const {PythonShell} =require('python-shell');
app.post('/hola', function (req, res) {
    res.send('[POST]Saludos desde express');
});
app.get('/holaperro', function (req, res) {
    res.send('[GET]Saludos desde express perro');
});
app.listen(3000, () => {
    console.log("El servidor está inicializado en el puerto 3000");
});