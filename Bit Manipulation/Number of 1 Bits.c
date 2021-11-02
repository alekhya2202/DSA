/* Interview Bit*/

#include <stdio.h>

int numSetBits(unsigned int A) {
    int cnt = 0;
    while(A > 0){
        cnt += (A & 1);
        A = A >> 1;
    }
    return cnt;
}

int main(){
    printf("%d", numSetBits(11));
}
