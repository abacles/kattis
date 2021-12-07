#include <stdio.h>

int main()
{
  int nlocs,xsum,ysum,x,y,mindist,bx,by,i;
  while(1)
  {
    scanf("%d",&nlocs);
    if(!nlocs) break;
    for(xsum=ysum=0,i=0;i<nlocs;i++)
    {
      scanf("%d %d",&x,&y);
      xsum += x;
      ysum += y;
    }
    for(mindist=-1,x=0;x<=1000;x++)
    {
      for(y=0;y<=1000;y++)
      {
        i = nlocs*x*x + nlocs*y*y - 2*xsum*x - 2*ysum*y;
        if(mindist == -1 || i < mindist)
        {
          mindist = i;
          bx = x;
          by = y;
        }
      }
    }
    printf("%d %d\n",bx,by);
  }
}
