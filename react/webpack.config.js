const config = {
    mode: 'production', // "production" | "development" | "none"
    resolve: {
        extensions: ['*', '.mjs', '.js', '.json']
    },
    module: {
        rules: [
            {
                test: /\.mjs$/,
                include: /node_modules/,
                type: 'javascript/auto'
            }
        ]
    },
    devServer: {
        headers: { "Access-Control-Allow-Origin": "*" },
        proxy: {
            '/localhost:8000': {
                target: 'http://localhost:8000/',
                changeOrigin: false,
                ws: true
            }
        }
    },
}

module.exports = config