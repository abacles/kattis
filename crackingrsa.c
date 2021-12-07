#include <stdio.h>

int pfac(int n)
{
  int i;
  for(i=2;i<1000;i++)
    if(n%i == 0)
      return i;
}

int main()
{
  int cases;
  long int n,e,d,totient,f1,f2;
  int i;
  scanf("%d",&cases);
  for(i=0;i<cases;i++)
    {
      scanf("%ld %ld",&n,&e);
      f1 = pfac(n);
      f2 = n / f1;
      totient = (f1-1) * (f2-1);
      for(d=2;(d*e)%totient!=1;d++) {}
      printf("%ld\n",d);
    }
}
