const express = require("express");
const app = express();
var bodyParser = require('body-parser');
app.use(bodyParser.json());
var myPythonScriptPath = 'gasto_energetico_python_tesis/gastoenergetico.py';
var consultasPython = 'pythonconsultas/verificarentidad.py';
const { PythonShell } = require('python-shell');
//let pyshell = new PythonShell(myPythonScriptPath);


app.post('/existenciaEnditidad', function (req, res) {
    //funcion para verificar si existe la entidad a registrar
    var entidad = req.body.entidad
    console.log('entidad: ', entidad);
    let options = {
        mode: 'text',
        args: [entidad] 
    };
    PythonShell.run(consultasPython, options, function (err, result) {
        if (err) throw err;
        res.send(result[0])
    });
});

app.post('/obteinvectorecuento', function (req, res) {
    //verrificar variables primero
    var entidad = req.body.entidad
    var epocas = req.body.epocas
    var cortedown = req.body.cortedown
    var corteup = req.body.corteup

    let options = {
        mode: 'text',
        args: [entidad, epocas, cortedown, corteup] //An argument which can be accessed in the script using sys.argv[1]
    };
    PythonShell.run(myPythonScriptPath, options, function (err, result) {
        if (err) throw err;
        // result is an array consisting of messages collected
        //during execution of script.
        //let data=JSON.parse(result)
        console.log('result: ', typeof (result));
        res.send(result[1])
    });


});

app.get('/getvectorecuento', function (req, res) {
    let options = {
        mode: 'text',
        args: ['CaminataAntonio2', '10', '0.2', '2.5'] //An argument which can be accessed in the script using sys.argv[1]
    };
    PythonShell.run(myPythonScriptPath, options, function (err, result) {
        if (err) throw err;
        // result is an array consisting of messages collected
        //during execution of script.
        //let data=JSON.parse(result)
        console.log('result: ', typeof (result));
        res.send(result[1])
    });

});

app.listen(3300, () => {
    console.log("El servidor está inicializado en el puerto 3300");
});