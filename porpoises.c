#include <stdio.h>

int main()
{
  long ncases, m, n, a = 0, b = 1, t, i, j;
  //scanf("%ld %ld", &n, &m);
  m = 10000000;
  for(i=0;;i++)
    {
      t = b;
      b = a;
      a = (a+t) % m;
      if(a == 0 && b == 1)
	break;
    }
  printf("%ld\n", i);
  /*for(i++,j=0,a=0,b=1;j<n%i;j++)
    {
      t = b;
      b = a;
      a = (a+t) % m;
    }
    printf("%ld\n", a);*/
}
