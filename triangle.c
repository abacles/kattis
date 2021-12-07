#include <stdio.h>
#include <math.h>

int main()
{
  int n, i, c = 1;
  double ans;
  while (scanf("%d", &n) != EOF)
    {
      ans = log10(3);
      for (i=0; i<n; i++)
        ans = ans + log10(3) - log10(2);
      printf("Case %d: %d\n", c, (int)ceil(ans));
      c++;
    }
}
