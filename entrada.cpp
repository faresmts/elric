#include <iostream>

int main() {
    // Declaração de variáveis
    int a = 5;
    int b = 3;

    // Operações de atribuição
    int c = a + b;
    int d = a * b;

    // Operações aritméticas com uso de parênteses
    int resultado1 = (a + b) * (a - b);
    int resultado2 = a * (b + 2);

    // Expressões Lógicas
    bool expressaoLogica = (a > b) && (c <= d);

    // Laço condicional if-else
    if (expressaoLogica) {
        std::cout << "A é maior que B, e C é menor ou igual a D." << std::endl;
    } else {
        std::cout << "A não é maior que B, ou C não é menor ou igual a D." << std::endl;
    }

    // Laço while
    int i = 0;
    while (i < 5) {
        std::cout << "Iteração " << i << std::endl;
        i++;
    }

    // Laço for
    for (int j = 0; j < 3; j++) {
        std::cout << "Loop for: " << j << std::endl;
    }

    return 0;
}
