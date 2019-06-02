#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int data;
  struct Node* next;
} Node;

void printLL(Node* head)
{
  if (head)
  {
    printf("%d\n", head->data);
    printLL(head->next);
  }
}

void printRev(Node* head)
{
  if (head)
  {
    printRev(head->next);
    printf("%d\n", head->data);

  }
}

int main()
{
  Node* head = (Node*)malloc(sizeof(Node));
  head->next = malloc(sizeof(Node));
  head->next->next = malloc(sizeof(Node));
  head->data = 10;
  head->next->data=20;
  head->next->next->data = 30;
  printLL(head);
  printRev(head);
}
