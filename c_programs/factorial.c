#include <stdio.h>

/* Iterative factorial for 0 <= n <= 20 (fits in unsigned long long). */
unsigned long long factorial(int n) {
    unsigned long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main(void) {
    int tests[] = {0, 1, 5, 10, 20};
    for (int i = 0; i < 5; i++) {
        printf("%d! = %llu\n", tests[i], factorial(tests[i]));
    }
    return 0;
}
