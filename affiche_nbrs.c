#include<stdio.h>
int main(){
int i,N;
printf("entrer la valeur de nombre N :");
scanf("%d",&N);
i = 0;
do{
    printf("%d\n",i);
    i++;
}while (i<=N);

    return 0;
}