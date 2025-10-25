const keypress = require('keypress');

keypress(process.stdin);

const keyActions = {
    q: () => {
        console.log('Saliendo del programa...');
        process.exit(0);
    },
    left: () => {
        console.log('Tecla izquierda presionada');
    }
};

process.stdin.on('keypress', (ch, key) => {
    if (key && keyActions[key.name]) {
        keyActions[key.name]();
    }
});