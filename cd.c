#include <stdio.h>

int main()
{
  int jack[1000000],jackc,jillc,i,cd,shared,s;
  while(1)
    {
      scanf("%d %d",&jackc,&jillc);
      if(!jackc && !jillc) break;
      shared = s = 0;
      for(i=0;i<jackc;i++) scanf("%d",&jack[i]);
      for(i=0;i<jillc;i++)
	{
	  scanf("%d",&cd);
	  for(;s<jackc && jack[s]<=cd;s++);
	  shared += jack[(s-1>0)?s-1:0] == cd;
	}
      printf("%d\n",shared);
    }
}
