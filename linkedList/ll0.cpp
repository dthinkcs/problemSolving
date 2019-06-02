#include <iostream>
using namespace std;

class Node
{
public:
  int data;
  Node* next;

  Node(int n=0){
    this->data = n;
    this->next = NULL;
  }
};

void printLL(Node* head)
{

  if (head)
  {
    cout << head->data << endl;
    printLL(head->next);

  }
}

void printRev(Node* head)
{
  if (head)
  {
    printRev(head->next);
    cout << head->data << endl;
  }
}

int main()
{
  Node* head = new Node(10);
  head->next = new Node(20);
  head->next->next = new Node(30);
  printLL(head);
  printRev(head);
}
