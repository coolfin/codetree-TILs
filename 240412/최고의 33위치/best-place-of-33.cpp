#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;

    int arr[30][30] = {0,};

    for(int i = 0; i< N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> arr[i][j];
        }
    }

    int r_pos = 0;
    int c_pos = 0;
    
    int res = 0;
    while (true) {
        int total =0;
        for(int i = r_pos; i< r_pos+3; i++) {
            for(int j = c_pos; j < c_pos+3; j++) {
                if (arr[i][j]) total += 1;
            }
        }

        res = max(res, total);

        c_pos += 1;
        if(r_pos == N-3 && c_pos > N-3) break;
        if(c_pos == N-2) {
            c_pos = 0;
            r_pos += 1;
        }
    }
    
    cout << res;
    return 0;
}