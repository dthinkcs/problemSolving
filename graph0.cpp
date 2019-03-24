#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void DFS_H(int** A, int n, int sv, bool* visited)
{
  cout << sv << " ";
  visited[sv] = true;
  for (int i = 0; i < n; i++)
  {
    if (A[sv][i] == 1 && !visited[i])
      DFS_H(A, n, i, visited);
  }
}


void DFS(int** A, int n, int sv)
{
  bool* visited = new bool[n];
  for (int i = 0; i < n; i++)
    visited[i] = false;

  DFS_H(A, n, sv, visited);
  cout << endl;
}



void BFS_H(int** A, int n, int sv, bool* visited)
{
  queue<int> q;
  q.push(sv);
  // 'visited' is MORE like 'CONSIDERED' here
  visited[sv] = true;
  while (!q.empty())
  {
    int frontNode = q.front(); q.pop();
    cout << frontNode << ' ';
    for (int i = 0; i < n; i++)
    {
      if (A[frontNode][i] == 1 && !visited[i])
      {
        q.push(i);
        visited[i] = true;
      }
    }
  }
}

void BFS(int** A, int n, int sv)
{
  bool* visited = new bool[n];
  for (int i = 0; i < n; i++)
    visited[i] = false;

  BFS_H(A, n, sv, visited);
  cout << endl;
}



int main()
{
    int V, E;
    cin >> V >> E;

    // adjacency matrix [ 0 0 0 ]
    //                  [ 0 0 0 ]
    //                  [ 0 0 0 ]
    int** edges = new int*[V];
    for (int i = 0; i < V; i++)
    {
        edges[i] = new int[V];
        for (int j = 0; j < V; j++)
            edges[i][j] = 0;
    }

    // cin into edges and vertices
    for (int i = 0; i < E; i++)
    {
        int f, s;
        cin >> f >> s;
        edges[f][s] = 1;
        edges[s][f] = 1;
    }

    /*
    for (int i = 0; i < V; i++)
    {
        for (int j = 0; j < V; j++ )
            cout << edges[i][j] << ' ';
        cout << endl;
    }
    */

  /*
    TST MAN - gamification
  	   Write Your Code Here
	   Complete the Rest of the Program
	   You have to take input and print the output yourself

  */

   BFS(edges, V, 0);

    return 0;
}
