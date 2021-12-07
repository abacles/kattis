#include <stdio.h>

int main()
{
  int presses,i;
  long long int a=1,b=0,achange,bchange;
  scanf("%d",&presses);
  for(i=0;i<presses;i++)
    {
      achange=-a;
      bchange=a;
      achange+=b;
      a+=achange;
      b+=bchange;
    }
  printf("%lld %lld\n",a,b);
  return 0;
}
