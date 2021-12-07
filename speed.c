#include <stdio.h>

double f(int n, int d[], int s[], double adjustment)
{
  double time = 0;
  int i;
  for (i=0; i<n; i++)
    time += d[i] / (s[i] + adjustment);
  return time;
}

int zero(double x)
{
  return -0.000000001 <= x && x <= 0.000000001;
}

int main()
{
  int n, t, d[1000], s[1000], i;
  double lo = -1000, hi = 10000000, mid, t_adjusted;
  scanf("%d %d", &n, &t);
  for (i=0; i<n; i++)
    {
      scanf("%d %d", &d[i], &s[i]);
      if (-s[i] > lo)
        lo = -s[i];
    }
  for (i=0; i<10000; i++)
    {
      mid = (lo + hi) / 2;
      t_adjusted = f(n, d, s, mid);
      if (zero(t_adjusted - t))
        break;
      else if (t_adjusted > t)
        lo = mid;
      else
        hi = mid;
    }
  printf("%.10lf\n", mid);
}
