#include <iostream>
using namespace std;



class Node{
public:
    int data;
    Node* next;

    Node(int data){
        this->data = data;
        next = nullptr;
    }
};

class LinkedList{

public:
    Node* head;
    Node* tail;
    LinkedList(){
        head = nullptr;
        tail = nullptr;
    }

    void EndInserting(int value){
        Node* newNode = new Node(value);

        if(head == nullptr){
            head = newNode;
            tail = newNode;
        } else{
            tail->next = newNode;
            tail = newNode;
        }
    }

    void CargarDatos(int Array[],int Tamanio){
        for(int i = 0; i < Tamanio; i++){
            this->EndInserting(Array[i]);
        }
    }

    void Display(){
        Node* temp = head;
        while (temp!= nullptr){
            cout<<temp->data;
            temp = temp->next;
        }
    }

    void Reverse(){
        Node* temp = head;
        Node* nextNode = nullptr;
        Node* prevNode = nullptr;

        while(temp != nullptr){
            nextNode = temp->next;

            temp->next = prevNode;
            prevNode = temp;

            temp = nextNode;
        }
        
        tail = head;
        head = prevNode;
    }

};


LinkedList addTwoNumbers(LinkedList ListOne, LinkedList ListTwo) {
        Node* head1 = ListOne.head;
        Node* head2 = ListTwo.head;
        string result1 = "";
        string result2 = "";

        LinkedList FinalList;

        while (head1 != nullptr) {
            result1 += to_string(head1->data);
            head1 = head1->next;
        }

        while (head2 != nullptr) {
            result2 += to_string(head2->data);
            head2 = head2->next;
        }

        int num1 = stoi(result1);
        int num2 = stoi(result2);
        int result = num1+num2;

        while (result != 0){
            int NewNumber = result%10;
            FinalList.EndInserting(NewNumber);
            result /=10;
        }

        return FinalList;
    }

int main(){
    LinkedList List1;
    LinkedList List2;
    
    int Array1[] = {2,4,3};
    List1.CargarDatos(Array1,3);
    List1.Reverse();
    List1.Display();
    cout<<endl;

    int Array2[] = {5,6,4};
    List2.CargarDatos(Array2,3);
    List2.Reverse();
    List2.Display();
    cout<<endl;

    LinkedList AddedLists = addTwoNumbers(List1, List2);
    AddedLists.Display();

    return 0;
}