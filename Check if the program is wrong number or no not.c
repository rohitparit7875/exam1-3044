#include <stdio.h>

int fact(int n) {
    int f = 1;
    for(int i=1; i<=n; i++) f *= i;
    return f;
}

int main() {
    int n, temp, sum = 0;
    printf("Enter a number: ");
    scanf("%d", &n);

    temp = n;
    while(temp > 0) {
        int digit = temp % 10;
        sum += fact(digit);
        temp /= 10;
    }

    if(sum == n)
        printf("%d is a Strong Number\n", n);
    else
        printf("%d is NOT a Strong Number\n", n);

    return 0;
}
