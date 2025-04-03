#include <iostream>
#include <queue>
using namespace std;

/*
Sumar números grandes con cola: Dado que una cola representa un número 
(cada dígito es un elemento de la cola), escribe una función para
sumar dos números representados como colas.
*/

int TwoQueuesSum(queue<int> Queu1, queue<int> Queu2){
    int resultOne = 0;
    int resultTwo = 0;


    while (!Queu1.empty() || !Queu2.empty()){

        if(!Queu1.empty()){
            if(resultOne == 0){
            resultOne += Queu1.front();
            Queu1.pop();
            } else{
                resultOne = resultOne*10 +Queu1.front();
                Queu1.pop();
            }
        }

        if(!Queu2.empty()){
            if(resultTwo == 0){
            resultTwo += Queu2.front();
            Queu2.pop();
            } else{
                resultTwo = resultTwo*10 +Queu2.front();
                Queu2.pop();
            }
        }

    }

    return resultOne+resultTwo;
}

int main(){
    queue<int> queueOne;
    queueOne.push(1);
    queueOne.push(2);
    queueOne.push(3);

    queue<int> queueTwo;
    queueTwo.push(2);
    queueTwo.push(4);
    queueTwo.push(6);
    queueTwo.push(1);

    cout<<TwoQueuesSum(queueOne, queueTwo);

    return 0;
}