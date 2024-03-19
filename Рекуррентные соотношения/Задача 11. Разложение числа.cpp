#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdint>

using ll = long long;
using ull = unsigned long long;
using namespace std;

ll MOD = 1000 * 1000 * 1000 + 7;

ll binpow(ll x, int pow){
    if (pow == 0)
        return 1;

    if (pow % 2 == 0){
        ll temp = binpow(x, pow/2);
        return (temp * temp) % MOD;
    }
    else{
        ll temp = binpow(x, pow-1);
        return (temp * x) % MOD;
    }
}

vector<int> find_divs(int x){
    vector<int> divs;

    for (int i = 1; i * i < x; i++){
        if (x % i == 0){
            divs.push_back(i);
        }
    }
    int size = divs.size();
    if (sqrt(x) == floor(sqrt(x))){
        divs.push_back(int(sqrt(x)));
    }
    for (int i = size - 1; i >= 0; i--){
        divs.push_back(x / divs[i]);
    }

    return divs;
}


int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int a, b, c;
    cin >> a >> b >> c;

    vector <int> divs = find_divs(a);

    int n = divs.size();

    vector <int> dp(n, INT32_MAX);
    dp[0] = 0;
    for (int i = 1; i < n; i++){
        for (int j = 0; j < i; j++){
            if (dp[j] == INT32_MAX) continue;
            if (divs[i] % divs[j] == 0){
                int d = divs[i] / divs[j];
                if (b <= d && d <= c){
                    dp[i] = min(dp[i], dp[j] + 1);
                }
            }
        }
    }

    // for (int i = 0; i < n; i++){
    //     cout << divs[i] << " " << dp[i] << endl;
    // }

    if (dp[n - 1] == INT32_MAX){
        cout << -1;
        return 0;
    }
    cout << dp[n - 1];

    return 0;
}