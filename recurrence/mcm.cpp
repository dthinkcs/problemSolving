#include <bits/stdc++.h>
using namespace std;
int mcmMEMO(int* a, int start, int end, int** memo)
{
    if (memo[start][end] != -1)
        return memo[start][end];

    if (end - start <= 1)
        return 0;

    int minSoFar = INT_MAX;
    for (int k = start + 1; k <= end - 1; k++)
        minSoFar = min(minSoFar, mcmMEMO(a, start, k, memo) + mcmMEMO(a, k, end, memo) + a[start]*a[k]*a[end]);
    memo[start][end] = minSoFar;
    return memo[start][end];
}

int mcm(int* a, int n)
{

    int** memo = new int*[n + 1]; // start = s + 1, e - 1 // start from 0 to n (included)
    for (int i = 0; i <= n; i++)
    {
        memo[i] = new int[n + 1];
        for (int j = 0; j <= n; j++)
            memo[i][j] = -1;
    }
    return mcmMEMO(a, 0, n, memo);
}

int main(){

  int n;
  cin >> n;
  int* p = new int[n];

  for(int i = 0; i <= n; i++){
    cin >> p[i];
  }

  cout << mcm(p, n);

}
