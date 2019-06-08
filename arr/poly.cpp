#define SIZE 100000000

class Polynomial
{
public:
  int * degCoeff;

  Polynomial()
  {
    degCoeff = new int[SIZE];
  }

  Polynomial(Polynomial const & p)
  {
    for (int i = 0; i < SIZE; i++)
      this->degCoeff[i] = p.degCoeff[i];
  }

  void operator=(Polynomial const & p)
  {
    for (int i = 0; i < SIZE; i++)
      this->degCoeff[i] = p.degCoeff[i];
  }

  

};
