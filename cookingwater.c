#include <stdio.h>

int main()
{
  int times,a,b,left = -1,right = 1001,i;
  scanf("%d",&times);
  for(i=0;i<times;i++)
    {
      scanf("%d %d",&a,&b);
      if(a > left) left = a;
      if(b < right) right = b;
    }
  if(left <= right) printf("gunilla has a point\n");
  else printf("edward is right\n");
}
