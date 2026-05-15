#include <stdio.h>
int main() {
  int moyenne=0;
  int somme = 0;    
  int a=0;
  int i=0;
  do {
    printf("entrer un nombre \n");
    scanf("%d", &a);
    somme += a;
    i++;
  }while (a >= 10);
  moyenne = somme/i;
  printf("la moyenne est :%d", moyenne);
  return 0;
}
