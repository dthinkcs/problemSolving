class Node
{
  int data;
  Node next;

  Node(int n)
  {
    this.data = n;
    this.next = null;
  }
}

class ll0
{
  static void printLL(Node head)
  {
    if (head != null)
    {
      System.out.println(head.data);
      printLL(head.next);
    }
  }

  static void printRev(Node head)
  {
    if (head != null)
    {
      printRev(head.next);
      System.out.println(head.data);
    }
  }

  public static void main(String[] args)
  {
    Node head = new Node(10);
    head.next = new Node(20);
    head.next.next = new Node(30);
    printLL(head);
    printRev(head);
  }
}
