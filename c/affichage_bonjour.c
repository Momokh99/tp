#include <stdio.h>
int main() {
  int b;
  printf("ce programe repete une phrase de n fois :");
  scanf("%d", &b);
  for (size_t i = 0; i < b; i++) {
    printf("hello world !\n");
  }

  return 0;
}
