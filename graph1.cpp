#include <iostream>
using namespace std;
#include <bits/stdc++.h>

void printDFS_H(int** edges, int n, int sv, bool* visited, int ev, string outputD="")
{
    outputD = to_string(sv) + " " + outputD;
    visited[sv] = true;

    if (sv == ev)
        cout << outputD << endl;

    for (int i = 0; i < n; i++)
    {
        if (edges[sv][i] == 1 && !visited[i])
            printDFS_H(edges, n, i, visited, ev, outputD);
    }

}


int main()
{
    int V, E;
    cin >> V >> E;

  /*

  	   Write Your Code Here
	   Complete the Rest of the Program
	   You have to take input and print the output yourself

  */

    int** edges = new int*[V];
    for (int i = 0; i < V; i++)
    {
        edges[i] = new int[V];
        for (int j = 0; j < V; j++)
            edges[i][j] = 0;
    }

    for (int i = 0; i < E; i++)
    {
        int f, s;
        cin >> f >> s;
        edges[f][s] = 1;
        edges[s][f] = 1;
    }

    int sv, ev;
    cin >> sv >> ev;

    bool* visited = new bool[V];
    for (int i = 0; i < V; i++)
        visited[i] = false;

    printDFS_H(edges, V, sv, visited, ev);

    return 0;
}
