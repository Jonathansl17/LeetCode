#include <iostream>

using namespace std;


class ListNode{

    public:
        int data;
        ListNode *next;

    ListNode(int data){
        this->data = data;
        next = nullptr;
    }

};



class LinkedList{
    
private:
    ListNode *head;
    ListNode *tail;

public:

    LinkedList(){
        head = nullptr;
        tail = nullptr;
    }

    void Insert(int value){

        ListNode *NewNode = new ListNode(value);

        if(head == nullptr){
            head = NewNode;
            tail = NewNode;

        } else{
            tail->next = NewNode;
            tail = NewNode;
        }
    }
    


    void rotateRight(int Mover) {
        // Si la lista está vacía (head es nullptr) o Mover es 0, no hay nada que hacer.
        if (!head || Mover == 0)
            return;

        // Encontrar la longitud de la lista y el último nodo
        ListNode* temp = head;

        int length = 1; // Empezamos con longitud 1 porque ya estamos en el head
        // Recorremos la lista hasta encontrar el último nodo
        while (temp->next != nullptr) {
            temp = temp->next;
            length++; // Incrementamos la longitud en cada iteración
        }

        // Conectar el último nodo con el head para hacer la lista circular
        temp->next = head;

        // Normalizar Mover para que no sea mayor que la longitud de la lista
        Mover = Mover % length; // Esto reduce Mover al rango [0, length-1]

        // Calcular cuántos pasos debemos dar desde el final de la lista para llegar al nuevo head
        int stepsToNewHead = length - Mover;
        ListNode* newTail = temp; // Inicializamos newTail en el último nodo (temp)

        // Encontrar el nuevo tail de la lista después de la rotación
        // Debemos dar stepsToNewHead pasos desde temp para llegar al nuevo tail
        while (stepsToNewHead != 0) {
            newTail = newTail->next;
            stepsToNewHead--; // Decrementamos el contador de pasos en cada iteración
        }
        //{1,2,3,4,5};

        // El nuevo head es el siguiente nodo después del nuevo tail
        head = newTail->next;
        // Desconectamos el nuevo tail del nuevo head para hacer la lista lineal de nuevo
        newTail->next = nullptr;
    }


    // void rotateRight(int mover){
    //     ListNode *Temp = head;

    //     int lenght = 1;
    //     while (Temp->next != nullptr){
    //         Temp= Temp->next;
    //         lenght++;
    //     }

    //     Temp->next = head;

    //     mover = mover%lenght;

    //     int totalmovimientos = lenght-mover;

    //     ListNode *NewTail = Temp;

    //     while (totalmovimientos != 0){
    //         NewTail = NewTail->next;
    //         totalmovimientos--;
    //     }

    //     head = NewTail->next;
    //     NewTail->next = nullptr;
        


    // }

    void Display(){
        ListNode *temp = head;

        while(temp != nullptr){
            cout << temp->data;
            temp = temp->next;
        }
        cout <<endl;
    }
        


};


int main(){

    LinkedList ListaEnlazada;

    int Array[] = {1,2,3,4,5};
    for (int i = 0 ; i < 5; i++){
        ListaEnlazada.Insert(Array[i]);
    }

    ListaEnlazada.rotateRight(2);
    ListaEnlazada.Display();

    return 0;
}