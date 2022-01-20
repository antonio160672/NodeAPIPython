const express = require("express");
const app = express();
var myPythonScriptPath = 'gasto_energetico_python_tesis/gastoenergetico.py';
const { PythonShell } = require('python-shell');
let pyshell = new PythonShell(myPythonScriptPath);


app.post('/consultarentidades', function (req, res) {
    res.send('[POST]Saludos desde express');
});

app.get('/getvectorecuento', function (req, res) {
    let options = {
        mode: 'text',
        args: ['ExperimentoReposoAntonio', '10', '0.2', '2.5'] //An argument which can be accessed in the script using sys.argv[1]
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