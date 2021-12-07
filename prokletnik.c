#include <stdio.h>
#include <stdlib.h>

#define MIN(A,B) A<B?A:B
#define MAX(A,B) A>B?A:B

struct set
{
  int length;
  int min;
  int max;
};

int main()
{
  int len,queries;
  int *all;
  struct set **ans;
  int i,j;
  scanf("%d",&len);
  all = malloc(sizeof(int)*len);
  ans = malloc(sizeof(struct set*)*len);
  for(i=0;i<len;i++)
    {
      scanf("%d",all+i);
      ans[i] = malloc(sizeof(struct set)*(i+1));
      ans[i][i].length = 1;
      ans[i][i].min = all[i];
      ans[i][i].max = all[i];
      if(i>0)
	{
	  ans[i][i-1].length = 2;
	  ans[i][i-1].min = MIN(all[i],all[i-1]);
	  ans[i][i-1].max = MAX(all[i],all[i-1]);
	}
    }
  for(i=2;i<len;i++)
    {
      for(j=i-2;j>=0;j--)
	{
	  if((all[i]<=ans[i-1][j].min && all[j]>=ans[i-1][j].max) ||
	     (all[i]>=ans[i-1][j].max && all[j]<=ans[i-1][j].min))
	    ans[i][j].length = i-j+1;
	  else
	    ans[i][j].length = MAX(ans[i-1][j].length,ans[i][j+1].length);
	  ans[i][j].min = MIN(ans[i-1][j].min,all[i]);
	  ans[i][j].max = MAX(ans[i-1][j].max,all[i]);
	}
    }
  /* for(i=0;i<len;i++)
    {
      for(j=0;j<=i;j++)
	printf("%ld ",ans[i][j].length);
      printf("\n");
    } */

  scanf("%d",&queries);
  for(;queries>0;queries--)
    {
      scanf("%d %d",&i,&j);
      printf("%d\n",ans[j-1][i-1].length);
    }
  
  free(all);
  for(i=0;i<len;i++)
    free(ans[i]);
  free(ans);
  return 0;
}
