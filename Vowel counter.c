#include <stdio.h>
#include <ctype.h>

int main() {
    char str[200];
    int v=0, c=0, d=0, s=0;

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    for(int i = 0; str[i] != '\0'; i++) {
        if (isalpha(str[i])) {
            char ch = tolower(str[i]);
            if (ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u')
                v++;
            else
                c++;
        }
        else if (isdigit(str[i]))
