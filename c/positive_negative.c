#include <stdio.h>
int imain() {
   int a;
    printf("Enter a: ");
    scanf("%d", &a);
    if (a<=0){
        if (a==0)
        printf("Zero\n");
        else
        printf("Non-positive\n");
    }
    else
    {
        printf("Positive\n");
    } 
return 0; }
