/*
    ./webpack.config.js
*/
const path = require('path');

const HtmlWebpackPlugin = require('html-webpack-plugin');
const HtmlWebpackPluginConfig = new HtmlWebpackPlugin({
  template: './prioritme/prioritime/templates/MainPage.html',
  filename: 'MainPage.html',
  inject: 'body'
})
module.exports = {
  entry: './prioritime/prioritime/static/index.jsx',
  output: {
    path: path.resolve('prioritime/prioritime/static'),
    filename: 'bundle.js',
  },
  module: {
    loaders: [
      { test: /\.js$/, use: 'babel-loader', exclude: /node_modules/ },
      { test: /\.jsx$/, use: 'babel-loader', exclude: /node_modules/ },
      { test: /\.scss$/,
        use: [{
                loader: "style-loader" // creates style nodes from JS strings
            }, {
                loader: "css-loader" // translates CSS into CommonJS
            }, {
                loader: "sass-loader" // compiles Sass to CSS
            }], exclude: /node_modules/ },
      { test: /\.(jpe?g|png|gif|svg)$/i,
      use: [
        'url-loader?limit=10000',
        'img-loader',
        'file-loader'
      ]},
      { test: /\.html$/, use: 'style-loader', exclude: /node_modules/ }
    ]
  }
}
