#include<stdio.h>
int main(){
float T[10];
int i;
float S=0;
    for (size_t i = 0; i < 10; i++){
        printf("element %d :",i+1);
        scanf("%f",&T[i]);}
    for (size_t i = 0; i < 10; i++)
    {
        printf("l'element numero %d est %.2f ",i,T[i]);
        printf("\n");
    }for (size_t i = 0; i < 10; i++)
    {
        S=T[i]+S;
    }
printf("la somme est :%.2f\n",S);
return 0;
}