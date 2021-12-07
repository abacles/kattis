#include <stdio.h>

int main()
{
  int count,prev = 0,c,len = 0,gis[1000000],i;
  scanf("%d",&count);
  for(i=0;i<count;i++)
    {
      scanf("%d",&c);
      if(c > prev)
	gis[len++] = prev = c;
    }
  printf("%d\n",len);
  for(i=0;i<len;i++) printf("%d%c",gis[i],i==len-1?'\n':' ');
}
