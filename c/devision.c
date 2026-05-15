#include <stdio.h>
int main() {
  int x = 0;
  int y = 0;
  printf("choise x : ");
  scanf("%d", &x);
  printf("choise y : ");
  scanf("%d", &y);
  if (y != 0) {
    int z = x / y;
    printf("the devision of X and Y is %d : ", z);
  } else {
    printf("error");
    printf("hii ");
  }
}
