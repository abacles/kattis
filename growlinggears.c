#include <stdio.h>

int main()
{
  int ncases, n, a, b, c, best, i;
  double x, maxtorque;
  scanf("%d", &ncases);
  while (ncases--)
    {
      scanf("%d", &n);
      best = -1;
      for (i=0; i<n; i++)
        {
          scanf("%d %d %d", &a, &b, &c);
          x = (double)b / (2*a);
          x = -a*x*x + b*x + c;
          if (best == -1 || x > maxtorque)
            {
              maxtorque = x;
              best = i+1;
            }
        }
      printf("%d\n", best);
    }
}
