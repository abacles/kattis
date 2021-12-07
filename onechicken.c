#include <stdio.h>

int main()
{
  int nppl, nchicken;
  scanf("%d %d", &nppl, &nchicken);
  if (nppl > nchicken)
    printf("Dr. Chaz needs %d more %s of chicken!\n", nppl - nchicken,
           nppl-nchicken > 1 ? "pieces":"piece");
  else
    printf("Dr. Chaz will have %d %s of chicken left over!\n",
           nchicken - nppl, nchicken-nppl > 1 ? "pieces":"piece");
}
