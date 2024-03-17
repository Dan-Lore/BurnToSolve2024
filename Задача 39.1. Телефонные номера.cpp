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
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    string s;
    cin >> s;

    // Конченное условие задачи, легче задать так
    map<char, int> dict;
    dict['A'] = '2';
    dict['B'] = '2';
    dict['C'] = '2';
    dict['D'] = '3';
    dict['E'] = '3';
    dict['F'] = '3';
    dict['G'] = '4';
    dict['H'] = '4';
    dict['I'] = '1';
    dict['J'] = '1';
    dict['K'] = '5';
    dict['L'] = '5';
    dict['M'] = '6';
    dict['N'] = '6';
    dict['O'] = '0';
    dict['P'] = '7';
    dict['Q'] = '0';
    dict['R'] = '7';
    dict['S'] = '7';
    dict['T'] = '8';
    dict['U'] = '8';
    dict['V'] = '8';
    dict['W'] = '9';
    dict['X'] = '9';
    dict['Y'] = '9';
    dict['Z'] = '0';
    dict['0'] = '0';
    dict['1'] = '1';
    dict['2'] = '2';
    dict['3'] = '3';
    dict['4'] = '4';
    dict['5'] = '5';
    dict['6'] = '6';
    dict['7'] = '7';
    dict['8'] = '8';
    dict['9'] = '9';

    int T;
    cin >> T;

    string input, trans;
    vector<string> a, words;

    for (int t = 0; t < T; t++){
        cin >> input;
        trans = "";
        for (char c: input){
            trans.push_back(dict[c]);
        }
        a.push_back(input);
        words.push_back(trans);
    }
    int words_len = words.size();

    // for (auto e: words){
    //     cout << e << "\n";
    // }
    
    int n = s.length();
    vector <vector<int>> dp(n + 1);

    for (int i = 0; i < n; i++){ // по буквам в заданном слове
        for (int j = 0; j < words_len; j++){ // по данным словам
            int word_len = words[j].length();
            if (i + word_len <= n){
                int k = 0;
                while (k < word_len && words[j][k] == s[i+k])
                    k++;
                if (k == word_len){
                    vector<int> temp = dp[i];
                    temp.push_back(j);
                    if ((dp[i].size() != 0 || i == 0) && (dp[i + word_len].size() == 0 || temp.size() < dp[i + word_len].size())){
                        dp[i + word_len] = temp;
                    }
                }
            }
        }
    }

    if (dp[n].size() > 0){
        cout << dp[n].size() << "\n";
        for(auto elem: dp[n]){
            cout << a[elem] << " ";
        }
    } else {
        cout << "No solution";
    }

    return 0;
}