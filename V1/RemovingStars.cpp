#include <iostream>
#include <stack>
using namespace std;

class Solution {
public:
    string removeStars(string s) {
        stack<char> Pila;

        for (int i = 0; i < s.length(); i++) {
            if (s[i] != '*') {
                Pila.push(s[i]);
            } else if (!Pila.empty()) {
                Pila.pop();
            }
        }

        string Caracter;
        while (!Pila.empty()) {
            Caracter = Pila.top() + Caracter;
            Pila.pop();
        }

        return Caracter;
    }
};

int main(){

    Solution Hola;
    cout<<Hola.removeStars("leet**cod*e");


    return 0;
}