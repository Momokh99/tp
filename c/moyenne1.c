#include <stdio.h>
int main() {
  int moyenne=0;
  int somme = 0;    
  int a=0;
  int b=0;
  for (size_t i = 0; a < 10; i++)
  {
    printf("entrer un nombre :");
    scanf("%d", &a);
    somme += a;
    b++;
    moyenne = somme/b;
  }
  printf("la moyenne est :%d", moyenne);
  return 0;
}