#include <stdio.h>

int main()
{
  int n,w,h,m;
  scanf("%d %d %d",&n,&w,&h);
  for(;n>0;n--)
    {
      scanf("%d",&m);
      if(m*m <= w*w + h*h)
	printf("DA\n");
      else
	printf("NE\n");
    }
}
