#include <stdio.h>

int main()
{
  int n, nways[31] = {1, 0}, i, j;
  for (i=2; i<=30; i++)
    {
      nways[i] = 0;
      for (j=2; j<=i; j+=2)
        nways[i] += 2 * nways[i-j];
      nways[i] += nways[i-2];
    }
  while (1)
    {
      scanf("%d", &n);
      if (n == -1) break;
      printf("%d\n", nways[n]);
    }
}
