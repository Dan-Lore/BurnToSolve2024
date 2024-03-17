#include <iostream>
#include <algorithm>
#include <cstdint>
#include <cmath>

#include <vector>
#include <string>
#include <map>

using ll = long long;
using ull = unsigned long long;
using namespace std;

ll MOD = 1000 * 1000 * 1000 + 7;

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n;
    cin >> n;
    
    vector <ull> lenta(n + 1, 0);
    vector <vector<ull>> dp(n + 1, vector<ull>(n + 1, 0));
    for (int i = 1; i <= n; i++){
        cin >> lenta[i];
        dp[i][i] = lenta[i];
    }

    vector <ull> ps(n + 1, 0);
    ps[1] = lenta[1];
    for (int i = 2; i <= n; i++){
        ps[i] = ps[i - 1] + lenta[i];
    }


    for (int l = 1; l < n; l++){
        for (int i = 1; i + l <= n; i++){
            int j = i + l;
            ull x = lenta[i] + (ps[j] - ps[i]) - dp[i + 1][j];
            ull y = lenta[j] + (ps[j - 1] - ps[i - 1]) - dp[i][j - 1];
            dp[i][j] = max(x, y);
        }   
    }

    cout << dp[1][n];

    return 0;
}