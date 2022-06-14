var path = require('path')

const HtmlWebpackPlugin = require('html-webpack-plugin')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')


const mode = process.env.NODE_ENV || "development"

module.exports = {
  mode,
  entry: './react.py/index.js',
  output: {
    filename: './react-py.js',
    path: path.resolve(__dirname, 'dist')
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: "./public/index.html",
      filename: './index.html'
    }),
    new CleanWebpackPlugin()
  ]
}