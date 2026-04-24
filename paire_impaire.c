#include <stdio.h>

int main() {
    int x = 0;
    printf("Veuillez choisir un nombre : ");
    scanf("%d", &x);
    if (x % 2 == 0) {
        printf("%d est pair\n", x);
    } 
    else {
        printf("%d est impair\n", x);
    }

    return 0;
}
