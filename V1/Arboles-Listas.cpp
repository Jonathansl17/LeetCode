
#include <iostream>
using namespace std;



//Lista Simple
class Node{
public:
    int data;
    Node* next;

    Node(int data){
        this->data = data;
        next = nullptr;
    }
};

class SimpleLinkedList{
private:
    Node* head;
    Node* tail;

public:
    SimpleLinkedList(){
        head = nullptr;
        tail = nullptr;
    }


    void InsertAtTheEndSimpleLinkedList(int value){
        Node* newNode = new Node(value);

        if(head == nullptr){
            head = newNode;
            tail = newNode;
        } else{
            tail->next = newNode;
            tail = newNode;
        }
    }

    void InsertAtTheBeginningSimpleLinkedList(int value){
        Node* newNode = new Node(value);

        if(head == nullptr){
            head = newNode;
            tail = newNode;
        } else{
            newNode->next = head;
            head = newNode;
        }
    }

    void ReverseSimpleLinkedList(){
        Node* temp = head;
        Node* prev = nullptr;
        Node* nextOne = nullptr;

        while (temp != nullptr){
            nextOne = temp->next;
            temp->next = prev;
            prev = temp;
            temp = nextOne;
        }
        tail = head;
        head= prev;

    }

    void DisplaySimpleLinkedList(){
        Node* temp = head;
        while (temp != nullptr){
            cout <<temp->data;
            temp = temp->next;
        }
    }

    void DeleteNodeSimpleLinkedList(int value){

        if(head == nullptr){
            return;
        }

        if(head->data == value){
            Node* DeleteThisNode = head;
            head = head->next;
            delete DeleteThisNode;
            return;
        }

        Node* temp = head;

        while (temp->next != nullptr){
            if(temp->next->data == value){
                Node* DeleteThisNode = temp->next;
                temp->next = temp->next->next;
                delete DeleteThisNode;
                return;
            }
            temp = temp->next;
        }
    }
    
};

//Doubly linked list

class DoubleNode{
public:
    int data;
    DoubleNode* next;
    DoubleNode* prev;

    DoubleNode(int data){
        this->data = data;
        next = nullptr;
        prev = nullptr;
    }

};

class DoublyLinkedList{
private:
    DoubleNode* head;
    DoubleNode* tail;

public:
    DoublyLinkedList(){
        head = nullptr;
        tail = nullptr;
    }

    void InsertAtTheBeginningDoublyLinkedList(int value) {
        DoubleNode* newNode = new DoubleNode(value);

        if (head == nullptr) {
            head = newNode;
            tail = newNode;
        } else {
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
        }
    }

    void InsertAtTheEndDoublyLinkedList(int value) {
        DoubleNode* newNode = new DoubleNode(value);

        if (head == nullptr) {
            head = newNode;
            tail = newNode;
        } else {
            newNode->prev = tail;
            tail->next = newNode;
            tail = newNode;
        }
    }


    void DeleteNodeDoublyLinkedList(int value) {
        if (head == nullptr) {
            return;
        }

        if (head->data == value) {
            DoubleNode* deleteThisNode = head;
            if (head->next == nullptr) {
                head = nullptr;
            } else {
                head = head->next;
                head->prev = nullptr;
            }
            delete deleteThisNode;
            return;
        }

        DoubleNode* temp = head;
        while (temp != nullptr) {
            if (temp->data == value) {
                DoubleNode* deleteThisNode = temp;

                if (temp->next != nullptr) {
                    temp->next->prev = temp->prev;
                }

                if (temp->prev != nullptr) {
                    temp->prev->next = temp->next;
                }

                delete deleteThisNode;
                return;
            }
            temp = temp->next;
        }
    }
        
    void DisplayDoublyLinkedList(){
        DoubleNode* temp = head;
        while (temp != nullptr){
            cout <<temp->data;
            temp = temp->next;
        }
    }

    void DisplayDoublyLinkedListBackwards(){
        DoubleNode* temp = tail;
        while (temp != nullptr){
            cout <<temp->data;
            temp = temp->prev;
        }
    }
};


//Lista Simple
class CircularNode{
public:
    int data;
    CircularNode* next;

    CircularNode(int data){
        this->data = data;
        next = nullptr;
    }
};

class CircularLinkedList{
private:
    CircularNode* head;
    CircularNode* tail;

public:
    CircularLinkedList(){
        head = nullptr;
        tail = nullptr;
    }


    void InsertAtTheEndCircularLinkedList(int value) {
        CircularNode* newNode = new CircularNode(value);

        if (head == nullptr) {
            head = newNode;
            tail = newNode;
            tail->next = head;
        } else {
            tail->next = newNode;
            tail = newNode;
            tail->next = head;
        }
    }

    void InsertAtTheBeginningCircularLinkedList(int value) {
        CircularNode* newNode = new CircularNode(value);

        if (head == nullptr) {
            head = newNode;
            tail = newNode;
            tail->next = head;
        } else {
            newNode->next = head;
            head = newNode;
            tail->next = head;
        }
    }

    void DeleteNodeCircularLinkedList(int value) {
        if (head == nullptr) {
            return;
        }

        if (head->data == value) {
            CircularNode* deleteThisNode = head;
            
            if (head->next == head) {
                head = nullptr;
                tail = nullptr;
            } else {
                head = head->next;
                tail->next = head;
            }

            delete deleteThisNode;
            return;
        }

        CircularNode* temp = head;
        do {
            if (temp->next->data == value) {
                CircularNode* deleteThisNode = temp->next;
                temp->next = temp->next->next;
                if (deleteThisNode == tail) {
                    tail = temp;
                }
                delete deleteThisNode;
                return;
            }
            temp = temp->next;
        } while (temp != head);
    }
    

    void DisplayCircularLinkedList(){
        CircularNode* temp = head;
        
        do{
            cout<<temp->data;
            temp = temp->next;
        }while(temp!= head);
    }
    
};



//Binary Tree
class TreeNode {
public:
    int data;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int data) {
        this->data = data;
        left = nullptr;
        right = nullptr;
    }
};

class BinaryTree {
private:
    TreeNode* root;

public:
    BinaryTree() {
        root = nullptr;
    }

    void Insert(int value) {
        TreeNode* newNode = new TreeNode(value);
        if (root == nullptr) {
            root = newNode;
        } else {
            TreeNode* temp = root;
            while (true) {
                if (value < temp->data) {
                    if (temp->left == nullptr) {
                        temp->left = newNode;
                        return;
                    } else {
                        temp = temp->left;
                    }
                } else {
                    if (temp->right == nullptr) {
                        temp->right = newNode;
                        return;
                    } else {
                        temp = temp->right;
                    }
                }
            }
        }
    }



    void DisplayBinaryTree(TreeNode* node) {
        if (node == nullptr) {
            return;
        }
        DisplayBinaryTree(node->left);
        cout << node->data << " ";
        DisplayBinaryTree(node->right);
    }

    void Display() {
            this->DisplayBinaryTree(this->root);
            cout << endl;
        }
};



int main(){
    // int Array[] = {1,2,4,6};
    // SimpleLinkedList Hola;
    
    // for(int i = 0 ; i < 4; i++){
    //     Hola.InsertAtTheBeginningSimpleLinkedList(Array[i]);
    // }


    // Hola.DisplaySimpleLinkedList();
    // Hola.ReverseSimpleLinkedList();
    // cout<<endl;
    // Hola.DisplaySimpleLinkedList();
    // cout<<endl;
    // Hola.DeleteNodeSimpleLinkedList(6);
    // Hola.DisplaySimpleLinkedList();


    // DoublyLinkedList Hola;
    // int array[] = {2,5,6,3};
    // for(int x = 0; x < 4; x++){
    //     Hola.InsertAtTheBeginningDoublyLinkedList(array[x]);
    // }

    // Hola.DisplayDoublyLinkedList();
    // Hola.DeleteNodeDoublyLinkedList(6);
    // cout<<endl;
    // Hola.DisplayDoublyLinkedList();
    // cout<<endl;
    // Hola.DisplayDoublyLinkedListBackwards();


    // CircularLinkedList Hola;
    // int array[] = {4,5,6,2};
    // for(int x: array){
    //     Hola.InsertAtTheEndCircularLinkedList(x);
    // }

    // Hola.DisplayCircularLinkedList();
    // cout<<endl;
    // Hola.DeleteNodeCircularLinkedList(2);
    // Hola.DisplayCircularLinkedList();


    BinaryTree Hola;
    int Array[] = {5,4,6};
    for(int x: Array){
        Hola.Insert(x);
    }

    Hola.Display();

    return 0;
}