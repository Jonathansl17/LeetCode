#include <iostream>
using namespace std;

void imprimirPatron(int filas) {
    int contador = 1;
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j <= i; j++) {
            cout << contador << " ";
            contador += 2;
        }
        cout << endl;

        if(i  == filas-2){
            contador+=2;
        } else{
            contador+=1;
        }
    }
}

int main() {
    int filas = 4;
    imprimirPatron(filas);
    return 0;
}