#include <stdio.h>

int main()
{
  int count,temp,cold = 0,i;
  scanf("%d",&count);
  for(i=0;i<count;i++)
    {
      scanf("%d",&temp);
      if(temp < 0) cold++;
    }
  printf("%d\n",cold);
}
