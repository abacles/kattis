#include <stdio.h>

int main()
{
  int want,size = 1;
  int i,j;
  scanf("%d",&want);
  while(size < want)
    size <<= 1;
  for(i=0,j=size;want>0 && want!=size;i++)
    {
      j >>= 1;
      want %= j;
    }
  printf("%d %d\n",size,i);
}
