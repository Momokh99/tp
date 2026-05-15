#include <stdio.h>
int main(int argc, char const *argv[]) {
  int count;
  printf("this program will count to :");
  scanf("%d", &count);
  for (size_t i = 0; i <= count; i++) {
    printf("%zu\n", i);
  }

  return 0;
}
