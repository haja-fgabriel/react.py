import app from './app.py'

var root = document.getElementById("__reactpy-root");


var pyscriptAppRoot = document.createElement('py-script')
var pyscriptRunner = document.createElement('py-script')

pyscriptAppRoot.setAttribute('src', app)

root.appendChild(pyscriptAppRoot);
root.appendChild(pyscriptRunner);

pyscriptRunner.innerHTML = `print(app())`