#include <bits/stdc++.h>
using namespace std;



void twoSubstrings1( string s)
{
	int indexAB = s.find("AB");
    if (indexAB == string::npos)
    {
        cout << "no" << endl;
        return;
    }

    int indexBA = s.find("BA");
    if (indexBA == string::npos)
    {
        cout << "no" << endl;
        return;
    }
    // difference between 2 indices must be 2 or greater
    if (abs(indexAB - indexBA) < 2)
    {
        cout << "no" << endl;

    }
    else
        cout << "yes" << endl;

}

bool twoSubstrings2( string s)
{
	int indexAB = s.find("AB");
    if (indexAB == string::npos)
        return false;

    int indexBA = s.find("BA");
    if (indexBA == string::npos)
        return false;

    return (abs(indexAB - indexBA));
}
