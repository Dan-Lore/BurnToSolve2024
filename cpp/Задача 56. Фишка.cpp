#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

const int mod = 1'000'000'007;

int solve(int n, int k) {
    if (n == 1) {
        return 1;
    }
    vector<int> dp(n + 1, 0);
    dp[1] = 1;
    dp[2] = 1;
    for (int i = 3; i <= n; i++) {
        dp[i] = (2 * dp[i-1] - dp[max(0, i-1-k)]) % mod;
    }
    return dp[n];
}

int main() {
    int t = 1;
    vector<string> result;
    ifstream inputFile("input.txt");
    if (inputFile.is_open()) {
        inputFile >> t;
        for (int i = 0; i < t; i++) {
            int n, k;
            inputFile >> n >> k;
            result.push_back(to_string(solve(n, k)));
        }
        inputFile.close();
    }
    ofstream outputFile("output.txt");
    if (outputFile.is_open()) {
        for (const string& res : result) {
            outputFile << res << endl;
        }
        outputFile.close();
    }
    return 0;
}