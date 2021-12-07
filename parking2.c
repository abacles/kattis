#include <stdio.h>

int main()
{
  int t, n, x, min, max, i, j;
  scanf("%d", &t);
  for (i=0; i<t; i++)
    {
      scanf("%d", &n);
      min = 99;
      max = 0;
      for (j=0; j<n; j++)
        {
          scanf("%d", &x);
          if (x < min) min = x;
          if (x > max) max = x;
        }
      printf("%d\n", 2 * (max - min));
    }
}
