#include <stdio.h>
int counter = 0;
void incrementer(int n) {
  n++;
  printf("%d", n);
}
int main() {
  incrementer(counter);
  incrementer(counter);
  incrementer(counter);
}
