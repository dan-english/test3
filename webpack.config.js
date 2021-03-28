const path = require('path');
const { join } = require('path');
const { VueLoaderPlugin } = require('vue-loader');

const webpack = require("webpack");
const dotenv = require('dotenv')

module.exports = (env) => {

}
module.exports ={
    entry: {
        app: { import: './resources/js/app.js', filename: 'app.js' },
    },
    devServer: {
            publicPath: '/storage/public/',
            port: 3000,
            index: '',
            hot: true,
            proxy: {}
    },

    // devtool: 'inline-source-map',

    watch: false,
    watchOptions: {
        aggregateTimeout: 200,
        poll: 1000
    },
    output: {
        filename: '[name].js',
        publicPath: '/',
        path: path.resolve(__dirname, 'storage/public'),
        hotUpdateChunkFilename: '../hot/hot-update.js',
        hotUpdateMainFilename: '../hot/hot-update.json'
    },
    externals: {
        'vue': 'Vue',
        'vue-router': 'VueRouter',
        'vuex': 'Vuex',
        'axios': 'axios',
        'moment':'moment',
    },

    resolve: {
       alias: {
          'vue$': 'vue/dist/vue.esm.js'
        },
       extensions: ['.js', '.jsx', '.scss', '.vue'],

       modules: [
            path.resolve('./resources/js/components'),
            path.resolve('node_modules'),
            path.resolve('./resources/scss'),
            path.resolve( './resources/js'),


        ]
    },
    module: {
           rules: [
                    {
                        test: /\.js$/,
                        loader: 'babel-loader',
                        options: {
                            presets: ['@babel/preset-env']
                        },
                        exclude: /node_modules/,
                    },
                    {
                        test: /.vue$/,
                        loader: 'vue-loader'
                    },
                {
                        test: /\.(scss|css)$/,
                        use: ['style-loader', 'css-loader', 'sass-loader'],
                    },
                {
                        test: /\.(woff(2)?|ttf|eot)(\?v=\d+\.\d+\.\d+)?$/,
                        use: [
                            {
                                loader: "file-loader",
                                options: {
                                    name: "[name].[ext]",
                                    outputPath: "fonts/",
                                },
                            },
                        ],
                    },


           ]
    },
    plugins: [
        new VueLoaderPlugin(),
         new webpack.DefinePlugin({
       'process.env': JSON.stringify(dotenv.config().parsed) // it will automatically pick up key values from .env file
         })
    ]
};
