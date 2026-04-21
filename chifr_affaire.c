#include <stdio.h>
int main() {
  int qte_vend;
  float prix_vendre;
  printf("le qantite des produit vendus est ");
  scanf("%d", &qte_vend);
  printf("le prix de vendre est ");
  scanf("%f", &prix_vendre);
  float chifre_dafaire = qte_vend * prix_vendre;
  printf("le chifre d'affaire set %f ", chifre_dafaire);
  return 0;
}
