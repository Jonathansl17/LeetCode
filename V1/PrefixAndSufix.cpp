#include <iostream>
#include <stack>
#include <queue>

using namespace std;

int preFijo(const std::string& Expresion) {
    std::stack<int> Pila;

    for (int i = Expresion.length() - 1; i >= 0; --i) {
        if (isdigit(Expresion[i])) {
            Pila.push(Expresion[i] - '0'); // Convertir carácter a entero
        } else {
            
            int Valor1 = Pila.top(); Pila.pop();
            int Valor2 = Pila.top(); Pila.pop();

            switch (Expresion[i]) {
                case '+':
                    Pila.push(Valor1 + Valor2);
                    break;
                case '-':
                    Pila.push(Valor1 - Valor2);
                    break;
                case '*':
                    Pila.push(Valor1 * Valor2);
                    break;
                case '/':
                    Pila.push(Valor1 / Valor2);
                    break;
            }
        }
    }
    return Pila.top();
}

int postFijo(string Expresion) {
    stack<int> Pila;

    for (int i = 0; i < Expresion.length(); ++i) {
        if (isdigit(Expresion[i])) {
            Pila.push(Expresion[i] - '0'); // Convertir caracter a entero
        } else {

            int Valor2 = Pila.top(); Pila.pop();
            int Valor1 = Pila.top(); Pila.pop();

            if (Expresion[i] == '+') {
                Pila.push(Valor1 + Valor2);
            } else if (Expresion[i] == '-') {
                Pila.push(Valor1 - Valor2);
            } else if (Expresion[i] == '*') {
                Pila.push(Valor1 * Valor2);
            } else if (Expresion[i] == '/') {
                Pila.push(Valor1 / Valor2);
            } 
        }
    }
    return Pila.top();
}



int main(){
    //Fifo
    queue<int> Hola;

    //Lifo
    stack<int> Hola2;


    cout<<postFijo("4293/*+")<<endl;
    cout<<preFijo("+*/9321")<<endl;
}