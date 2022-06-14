var path = require('path')

module.exports = {
  mode: "development",
  output: {
    filename: './react-py.js',
    path: path.resolve(__dirname, 'dist')
  }
}