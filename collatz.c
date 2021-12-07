#include <stdio.h>

int collatz(long long x, long long s[])
{
  int i = 0;
  s[i++] = x;
  while(x > 1)
    {
      if(x%2 == 0)
	s[i++] = (x /= 2);
      else
	s[i++] = (x = 3*x+1);
    }
  return i;
}

int main()
{
  long long a, b, asteps[100000], bsteps[100000], ac, bc, i;
  while(scanf("%lld %lld", &a, &b), a || b)
    {
      ac = collatz(a, asteps);
      bc = collatz(b, bsteps);
      for(i=1; ac-i >= 0 && bc-i >= 0 && asteps[ac-i] == bsteps[bc-i]; i++);
      printf("%lld needs %lld steps, %lld needs %lld steps, they meet at %lld\n", a, ac-i+1, b, bc-i+1, asteps[ac-i+1]);
    }
}
