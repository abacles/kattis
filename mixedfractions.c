#include <stdio.h>

int main()
{
  int top,bot;
  while(1)
    {
      scanf("%d %d",&top,&bot);
      if(!top && !bot) break;
      printf("%d %d / %d\n",top/bot,top%bot,bot);
    }
}
