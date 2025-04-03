#include <iostream>
using namespace std;

class node{
public:
    int data;
    node* next;

    node(int data){
        this->data = data;
        this->next = nullptr;
    }
};

class linkedList{
private:
    node* head;
    node* tail;

public:
    linkedList(){
        this->head = nullptr;
        this->tail = nullptr;
    }

    void addNodeAtTheEnd(int data){
        node* newNode = new node(data);

        if(head == nullptr){
            head = newNode;
            tail = newNode;
            return;
        }

        tail->next = newNode;
        tail = newNode;
    }

    void display(){
        node* temp = head;
        while(temp != nullptr){
            cout << temp->data<<" ";
            temp = temp->next;
        }
        cout<<endl;
    }

    string reversed() {
        if (head == nullptr) {
            return ""; 
        }
    
        string reverse = "";
        node* temp = head;
        node* siguiente = nullptr;
        node* prev = nullptr;
    
        while (temp != nullptr) {
            siguiente = temp->next;
            temp->next = prev;
            prev = temp;
            reverse += to_string(temp->data); 
            temp = siguiente;
        }
    
        head = prev; 
        return reverse;
    }

    node* getHead(){
        return head;
    }

};

linkedList addTwoLists(node* l1, node* l2) {
    linkedList result;
    int carry = 0;

    while (l1 || l2 || carry){
        int sum = carry;
        if(l1){
            sum += l1->data;
            l1 = l1->next;
        }

        if (l2){
            sum += l2->data;
            l2 = l2->next;
        }        

        result.addNodeAtTheEnd(sum%10);
        carry = sum/10;
    }

    return result;

}

int main() {
    linkedList list1;
    linkedList list2;

    int arr1[] = {2, 4, 3};
    int arr2[] = {5, 6, 4};
    int size1 = sizeof(arr1) / sizeof(arr1[0]);
    int size2 = sizeof(arr2) / sizeof(arr2[0]);

    for (int i = 0; i < size1; i++) {
        list1.addNodeAtTheEnd(arr1[i]);
    }

    for (int i = 0; i < size2; i++){

     list2.addNodeAtTheEnd(arr2[i]);
    };

    linkedList sumList = addTwoLists(list1.getHead(), list2.getHead());

    cout << "Resultado de la suma: ";
    sumList.display();

    return 0;
}