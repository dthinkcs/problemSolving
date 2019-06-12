#include <bits/stdc++.h>
using namespace std;
int getMin(int *arr, int n){


    int* dp = new int[n];
    dp[0] = 1;

    for (int i = 1; i < n; i++)
        if (arr[i - 1] < arr[i])
            dp[i] = dp[i - 1] + 1;
        else
            dp[i] = 1;

    for (int i = n - 2; i >= 0; i--)
        if (arr[i] > arr[i + 1] && dp[i] <= dp[i + 1])
            dp[i] = dp[i + 1] + 1;

    return accumulate(dp, dp + n, 0);

}
