#include <stdio.h>

/* Prints the first n Fibonacci numbers, starting 0, 1, 1, 2, ... */
void fibonacci(int n) {
    long long a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        printf("%lld ", a);
        long long next = a + b;
        a = b;
        b = next;
    }
    printf("\n");
}

int main(void) {
    fibonacci(10);
    return 0;
}
