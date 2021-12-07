#include <stdio.h>
#include <math.h>

double f(int d, int s, double a)
{
  return a + s - a * cosh(d / (2*a));
}

int almost_zero(double x)
{
  return -0.00000001 <= x && x <= 0.00000001;
}

int main()
{
  int d, s;
  double a, top = 10000000000, bot = 0, error;
  scanf("%d %d", &d, &s);
  while (1)
    {
      a = (top + bot) / 2.0;
      error = f(d, s, a);
      if (almost_zero(error))
        break;
      else if (error > 0)
        top = a;
      else
        bot = a;
    }
  printf("%lf\n", 2 * a * sinh(d / (2*a)));
}
