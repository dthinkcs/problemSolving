
#include <iostream>
using namespace std;

int count = 0;

void fun2(int m, int n = 1)
{
  if (n <= 0)
    return;
  if (n > m)
    return;
  count += 1;
  fun2(m, 2*n);
 }

int main(){

  fun2(128, 2);


  cout << count << endl;

}


// -webkit-linear-gradient(65deg,  rgb(233, 187, 101) 50%, #AA0505 50%)
