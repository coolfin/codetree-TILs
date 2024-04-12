#include <iostream>
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
    
    int res =0;
    while (true) {
        for(int i = 0; i< 3; i++) {
            for(int j = 0; j < 3; j++) {
                if (arr[i][j]) res += 1;
            }
        }

        c_pos += 1;
        if(c_pos == N) {
            c_pos = 0;
            r_pos += 1;
        }

        if(r_pos == N-3 && c_pos > N-3) break;
    }
    
    cout << res;
    return 0;
}