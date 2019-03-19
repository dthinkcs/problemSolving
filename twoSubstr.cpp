#include <bits/stdc++.h>
using namespace std;

int findMy(string s, string sub)
{

    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == sub[0])
        {
            int j = 0;
            for (int inner_i = i; j < sub.length(); j++, inner_i++)
                if (s[inner_i] != sub[j])
                    break;


            if (j == sub.length())
                return i;

            //j = 0;
        }

    }
    return -1;
}

void twoSubstrings(string s)
{
	int indexAB = findMy(s, "AB");
    if (indexAB == -1)
    {
        cout << "no" << endl;
        return;
    }

    int indexBA = findMy(s, "BA");
    if (indexBA == -1)
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
