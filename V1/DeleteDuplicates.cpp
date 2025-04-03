#include <iostream>
#include <stack>
using namespace std;

string DeleteDuplicates(string word) {
    stack<char> Pila;
    string result = "";

 
    for (int i = 0; i < word.length(); i++) {
        if (!Pila.empty() && Pila.top() == word[i]) {
            Pila.pop(); 
        } else {
            Pila.push(word[i]);  
        }
    }

    while (!Pila.empty()) {
        result = Pila.top() + result;  
        Pila.pop();
    }

    return result;
}

int main(){
    cout<<DeleteDuplicates("abbaca")<<endl;
    return 0;
}