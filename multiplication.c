#include <stdio.h>
int main()
{   int a = 0;
    int b = 0; 
    int resultat = 0 ;
    printf("la multiplication de A et B\n");
    printf("entrer A : ");
    scanf("%i", &a);
    printf("entrer B :");
    scanf("%i", &b);
    resultat = a*b ;
    printf("la resultat de la multiplication est %i", resultat);
    return 0;
}