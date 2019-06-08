#include <iostream>
using namespace std;

class Node
{
public:
  int data;
  Node* next;

  Node(int data)
  {
    this->data = data;
    this->next = NULL;
  }
};

Node* takeInput()
{

  cout << "Enter -1 to extit" << endl;
  Node* head = NULL; Node* ptr;
  while (true)
  {
    int n;
    cin >> n;
    if (n == -1)
      break;
    if (!head)
    {
      head = new Node(n);
      ptr = head;
    }
    else
    {
      ptr->next = new Node(n);
      ptr = ptr->next;
    }
  }
  return head;
}

void printLL(Node* head)
{
  if (head)
  {
    cout << head->data << endl;
    printLL(head->next);
  }
}

int main()
{
  Node* head = takeInput();
  printLL(head);
}
