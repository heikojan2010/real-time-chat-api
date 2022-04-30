
module.exports = {
    webpack: {
        entry: {
            Comp1: './src/Comp1.js',
            module: {
                rules: [
                    {
                        loader: ['django-react-loader'],
                    },
                ],
            },
        }
    }
};
