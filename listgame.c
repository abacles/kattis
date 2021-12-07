#include <stdio.h>
#include <math.h>

int factor(int n)
{
  int total = 0;
  int next = 2;
  int max = sqrt(n);
  while(n > 1 && next <= max)
    {
      if(n%next == 0)
	{
	  n /= next;
	  total++;
	}
      else
	next++;
    }
  if(next > max)
    total++;
  return total;
}

int main()
{
  long int x;
  scanf("%ld",&x);
  printf("%d\n",factor(x));
  return 0;
}
