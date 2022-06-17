# react.py

It's React, but in Python. It includes `react_cli`, which helps developing and building frontend web applications without depending on Node.js and/or Webpack, **and without JavaScript knowledge**.

## Preparing the development environment

1. Create a new virtual environment: `python -m venv env/`
2. Install the dependencies: `pip install -r requirements-dev.txt`
3. Install the library as editable (for development or until it is available on PyPI): `pip install -e .` - searches for setup.py, which is going to install the `react` and `react_cli` packages as editable

## Using `react_cli`

    $ python -m react_cli
    usage: react_cli [-h] {dev,build}
    react_cli: error: the following arguments are required: command



## Developing a project

    python -m react_cli dev

It is going to start a live development server, which is going to reload the page automatically when saving.

The entrypoint of the web application is going to be `src/app.py`, so the app.py file must be created prior opening the command above.

## Building a project

    python -m react_cli build

It is going to deliver the built assets in the build/ folder, including the provided modules.


## Example:

src/app.py:

```python
def app():
    return """
    <h2> Best frontend frameworks: </h2>

    <ol>
        <li> React.py </li>
        <li> React.js </li>
        <li> Angular </li>
    </ol>
    """

from app2 import powers_of_two

print(app())
print(powers_of_two())
```

src/app2.py
```python

def powers_of_two():
    result = "<table>")
    result += "<tr> <th>N</th> <th>2<sup>N</sup></th></tr>"
    for i in range(20):
        result += f"<tr> <td> {i} </td> <td> {2**i} </td> </tr>"

    result += "</table>"
    return result
```

Running example:
![Running example](pyscript-shot.gif)

## Customizing the HTML template

`react_cli` makes use of Jinja2 to compile an HTML file based on the template at the following path: `public/index.html.jinja`.



### Adding dependencies

PyScript makes use of the `<py-env>` tag, which is a list of dependencies in YAML format, like so:

```html
<py-env>
- numpy
- scipy
...
</py-env>
```

There is a special entry in this list called `- paths`, which allows listing custom modules written by the user. `react_cli` searches for all the Python files in the `src/` folder and provides the list of found files through the provided `imports` variable.

| Template arguments | Description | Default |
| :------- | :--- | :--- |
| `imports` | The list of imported modules | All Python modules from `src/`, returned by `react_cli._resolve_imports` |

### Modifying the entry point

By default, `react_cli` lists all files from `src/` and automatically imports the `app` module, which implicitly is going to run it

```html
<py-script>
    import app
</py-script>
```

### Adding JavaScript and/or CSS

For JavaScript, add the `<script>` tag anywhere in the template. For CSS, add inline styling with the `style` attribute or use the `<link rel="stylesheet" href="...">` tag.

