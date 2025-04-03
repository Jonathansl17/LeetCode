#include <iostream>
#include <stack>
using namespace std;

void StackPalindrome(string word) {
    stack<char> Pila;
    int length = word.length();
    int mid = length / 2;


    for (int i = 0; i < mid; i++) {
        Pila.push(word[i]);
    }


    if (length % 2 != 0) {
        mid++;
    }

    for (int j = mid; j < length; j++) {
        if (!Pila.empty() && Pila.top() == word[j]) {
            Pila.pop();
        } else {
            cout << "No es palindromo" << endl;
            return;
        }
    }

    cout << "Es palindromo" << endl;
}


int main(){
    StackPalindrome("radaer");
    return 0;
}