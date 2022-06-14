var path = require('path')
const webpack = require('webpack')

const HtmlWebpackPlugin = require('html-webpack-plugin')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')


const mode = process.env.NODE_ENV || "production"

module.exports = {
  mode,
  entry: './src/index.js',
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
  ],
  module: {
    noParse: /pyscript\.js/,
    rules: [
      {
          test: /\.py$/,
          use: 'file-loader'
      }
    ]
  }
}