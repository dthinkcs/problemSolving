class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

function printLL(head) {
  if (head) {
    console.log(head.data);
    printLL(head.next);
  }
}

function printRev(head) {
  if (head) {
    printRev(head.next);
    console.log(head.data);
  }
}
let head = new Node(10);
head.next = new Node(20);
head.next.next = new Node(30);
printLL(head);
printRev(head);
