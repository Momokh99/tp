#include<stdio.h>
int main(){
int b,nbr,somme,a;
printf("ce programe faire ladition de fois :");
scanf("%d",&nbr);
while (b < nbr)
{
    printf("entrer le nombre %d :",b);
    scanf("%d",&a);
    b++;
    somme += a;
}
printf("la somme est : %d\n",somme);
return 0;
}