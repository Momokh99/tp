#include <stdio.h>
int main() {
  int a = 0;
  int b = 0;
  int c = 0;
  int d = 0;

  a = 4 + 2;
  printf("%d,%d,%d,%d\n", a, b, c, d);
  b = ++a;
  printf("%d,%d,%d,%d\n", a, b, c, d);

  c = a * b++;
  printf("%d,%d,%d,%d\n", a, b, c, d);
  int c2 = c * c;
  d = c2;
  printf("%d,%d,%d,%d\n", a, b, c, d);

  a /= 2;

  printf("%d,%d,%d,%d\n", a, b, c, d);

  d = ++d - c;
  printf("%d,%d,%d,%d\n", a, b, c, d);

  c -= b--;
  printf("%d,%d,%d,%d\n", a, b, c, d);

  b = (a-- + --c) / b;

  printf("%d,%d,%d,%d\n", a, b, c, d);

  return 0;
}
