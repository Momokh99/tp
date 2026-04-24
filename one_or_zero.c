#include <stdio.h>
int main(){
int a;
printf("shoose a number :");
scanf("%d",&a);
switch (a)
{
case 0:
    printf("your number is zero");
    break;
case 1:
    printf("your number is one");
    break;
case 2:
    printf("your number is 2");
    break;
case 3:
    printf("your number is 3");
    break;
default:
    printf("your number isn't in the list ");
    break;
}
return 0;
}