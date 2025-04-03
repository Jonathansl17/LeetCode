#include <iostream>
#include <stack>
using namespace std;

void PrintStack(stack<int> Pila);
void deleteLowerElements(stack<int> &Pila, int Number);

void deleteLowerElements(stack<int> &Pila, int Number) {
    stack<int> PilaAuxiliar;


    while (!Pila.empty()) {
        if (Pila.top() < Number) {
            Pila.pop();  
        } else {
            PilaAuxiliar.push(Pila.top());  
            Pila.pop();
        }
    }

    while (!PilaAuxiliar.empty()) {
        Pila.push(PilaAuxiliar.top());
        PilaAuxiliar.pop();
    }


    PrintStack(Pila);
}

void PrintStack(stack<int> Pila) {
    stack<int> Temp = Pila;  

    while (!Temp.empty()) {
        cout << Temp.top() << " ";  
        Temp.pop();  
    }
    cout << endl;  
}

int main() {
    stack<int> pila;
    pila.push(5);
    pila.push(2);
    pila.push(8);
    pila.push(1);
    pila.push(6);

    int number = 4;
    deleteLowerElements(pila, number);

    return 0;
}
