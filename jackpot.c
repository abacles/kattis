#include <stdio.h>

int gcf(int a, int b)
{
  if (a == 0) return b;
  return gcf(b % a, a);
}

long long int lcm(int a, int b)
{
  return (long long int)a / gcf(a, b) * b;
}

int main()
{
  int n, nwheels, p[5], i, j;
  long long int jackpot;
  scanf("%d", &n);
  for (i=0; i<n; i++)
    {
      scanf("%d", &nwheels);
      for (j=0; j<nwheels; j++)
        scanf("%d", &p[j]);
      for (j=0, jackpot=1; j<nwheels && jackpot <= 1000000000; j++)
        jackpot = lcm(jackpot, p[j]);
      if (jackpot <= 1000000000)
        printf("%lld\n", jackpot);
      else
        printf("More than a billion.\n");
    }
}
