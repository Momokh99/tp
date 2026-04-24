#include <stdio.h>
#include <math.h>
int main() { 
    char opperation = 0;
    double i = 0;
    double o = 0;
    printf("\033[1;33m=====this is an calculator=====\033[0m\n") ;
    printf("\n\033[1;31m A.\033[0maddition\n\033[1;31m B.\033[0msustraction\n\033[1;31m C.\033[0mmultiplication\n\033[1;31m D.\033[0mdivision\n\nyour choice is : ");
    scanf(" %c", &opperation);
    printf("\nenter two numbers: ");
    scanf("%lf %lf",&i ,&o);
    switch (opperation){
        case 'A' :
            printf("your result is %.2lf", i + o);
            break;
        case 'B':
            printf("your result is %.2lf",  i - o);
            break;
        case 'C':
            printf("your result is %.2lf", i * o);
            break;
        case 'D':
            if (o==0)
            {
             printf("you can't devise by zero");
            }
            else
            printf("your result is %.2lf", i / o);
            break;
    default:
        printf("\033[1;31mplease choose a valid ");
        break;
}
return 0;
}
