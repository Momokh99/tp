#include <stdio.h>
int main()
{
    int x = 0;
    int y = 0;
    int z = 0;
    printf("choise x : ");
    scanf("%d", &x);
    printf("choise y : ");
    scanf("%d", &y);
    z = x;
    x = y;
    y = z;
    printf("your x is %d \nyour y is %d",x ,y);
    return 0;
}
