#include<stdio.h>
int main()
{int j;
printf("itroduire un numero de nombre :");
scanf("%d",&j);
switch (j)
{
case 1:printf("\033[1;33mdimanch\n");break;
case 2:printf("lundi\n");break;
case 3:printf("mardi\n");break;
case 4:printf("mercredi\n");break;
case 5:printf("jeudi\n");break;
case 6:printf("vendredi\n");break;
case 7:printf("\033[1;33msamedi\033[0m\n");break;
default:printf("\033[1;31m Error");
}
return 0;
}