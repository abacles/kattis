#include <stdio.h>

int main()
{
  int n, k, i;
  scanf("%d", &n);
  for (i=0; i<n; i++)
    {
      scanf("%d", &k);
      printf("%d\n", (1<<k) - 1);
    }
}
