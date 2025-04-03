#include <iostream>

using namespace std;

class Node{
public:
    int data;
    Node *next;

    Node(int data){
        this->data = data;
        next = nullptr;
    }

};


class LinkedList{

private:
    Node* head;
    Node* tail;

public:
    LinkedList(){
        head = nullptr;
        tail = nullptr;
    }

    void Insert(int value){
        
        Node* newnode = new Node(value);

        if(head == nullptr){
            head = newnode;
            tail = newnode;

        } else{
            tail->next = newnode;
            tail = newnode;
        }
    }


    void Display(){
        Node* Temp = head;

        while(Temp != nullptr){
            cout <<Temp->data <<" ";
            Temp = Temp->next;
        }
        cout<<endl;
    }


    Node *Merge(Node *FirstList, Node *SecondList){

        //Creamos un nodo temporal y una tail temporal para evitar cambios en los originales
        Node* Temp = new Node(0);
        Node* tail = Temp;
        
        while(FirstList && SecondList){
            //Comparamos los valores de las listas
            if(FirstList->data  < SecondList->data){
                tail->next = FirstList;//Hacemos que el next de la tail apunte a la primera lista
                FirstList = FirstList->next;//Movemos el nodo de la primera lista

            } else{
                tail->next = SecondList;//Lo mismo con la segunda
                SecondList = SecondList->next;
            }

            tail = tail->next;//Movemos la cola
        }

        //En el caso de que una queda vacia, enlazamos la cola a todos los nodos restantes
        if(FirstList != nullptr){
            tail->next  = FirstList;

        } else if(SecondList != nullptr){
            tail->next = SecondList;
        }

        return Temp->next;
    }


    Node* getHead() {
        return head;
    }

    void setHead(Node* newHead) {
        head = newHead;
    }
};






int main(){

    LinkedList List1;
    LinkedList List2;

    int Array1[] = {1,2,4};
    for(int i = 0; i < 3; i++){
        List1.Insert(Array1[i]);
    }

    int Array2[] = {1,3,5,6,7};
    for(int i = 0; i < 5; i++){
        List2.Insert(Array2[i]);
    }

    Node* mergedHead = List1.Merge(List1.getHead(), List2.getHead());
    LinkedList mergedList;
    mergedList.setHead(mergedHead);

    mergedList.Display();


    return 0;
}