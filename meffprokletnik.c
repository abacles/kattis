#include <stdio.h>
#include <stdlib.h>

#define INTERVAL 50

#define MIN(A,B) A<B?A:B
#define MAX(A,B) A>B?A:B

struct set
{
  int length;
  int min;
  int max;
};

void copy(struct set *from,struct set *to)
{
  to->length = from->length;
  to->min = from->min;
  to->max = from->max;
}

int main()
{
  int len,queries;
  int *all;
  struct set **ans;
  struct set *prev,*curr;
  int i,j,start,end;
  scanf("%d",&len);
  all = malloc(sizeof(int)*len);
  ans = malloc(sizeof(struct set*)*len);
  prev = malloc(sizeof(struct set)*len);
  curr = malloc(sizeof(struct set)*len);
  for(i=0;i<len;i++)
    {
      scanf("%d",all+i);
      if(i%INTERVAL == 0)
	{
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
      else
	ans[i] = NULL;
    }
  prev[0].length = 1;
  prev[0].min = all[0];
  prev[0].max = all[0];
  if(len > 1)
    {
      curr[0].length = 2;
      curr[0].min = MIN(all[0],all[1]);
      curr[0].max = MAX(all[0],all[1]);
      curr[1].length = 1;
      curr[1].min = all[1];
      curr[1].max = all[1];
    }
  for(i=2;i<len;i++)
    {
      curr[i].length = 1;
      curr[i].min = all[i];
      curr[i].max = all[i];
      curr[i-1].length = 2;
      curr[i-1].min = MIN(all[i],all[i-1]);
      curr[i-1].max = MAX(all[i],all[i-1]);
      for(j=i-2;j>=0;j--)
	{
	  if((all[i]<=prev[j].min && all[j]>=prev[j].max) ||
	     (all[i]>=prev[j].max && all[j]<=prev[j].min))
	    curr[j].length = i-j+1;
	  else
	    curr[j].length = MAX(prev[j].length,curr[j+1].length);
	  curr[j].min = MIN(prev[j].min,all[i]);
	  curr[j].max = MAX(prev[j].max,all[i]);
	}
      for(j=0;j<i;j++)
	copy(curr+j,prev+j);
    }

  scanf("%d",&queries);
  for(;queries>0;queries--)
    {
      scanf("%d %d",&start,&end);
      if(end-start+1 == 1)
	printf("1\n");
      else if(end-start+1 == 2)
	printf("2\n");
      else
	{
	  start--;
	  end--;
	  for(i=0;i<end-end%INTERVAL;i++)
	    copy(&(ans[end-end%INTERVAL][i]),&(prev[i]));
	  for(i=end-end%INTERVAL+1;i<=end;i++)
	    {
	      curr[i].length = 1;
	      curr[i].min = all[i];
	      curr[i].max = all[i];
	      curr[i-1].length = 2;
	      curr[i-1].min = MIN(all[i],all[i-1]);
	      curr[i-1].max = MAX(all[i],all[i-1]);
	      for(j=i-2;j>=0;j--)
		{
		  if((all[i]<=prev[j].min && all[j]>=prev[j].max) ||
		     (all[i]>=prev[j].max && all[j]<=prev[j].min))
		    curr[j].length = i-j+1;
		  else
		    curr[j].length = MAX(prev[j].length,curr[j+1].length);
		  curr[j].min = MIN(prev[j].min,all[i]);
		  curr[j].max = MAX(prev[j].max,all[i]);
		}
	      for(j=0;j<i;j++)
		copy(curr+j,prev+j);
	    }
	  printf("%d\n",prev[start].length);
	}
    }
  
  free(all);
  free(prev);
  free(curr);
  for(i=0;i<len;i++)
    free(ans[i]);
  free(ans);
  return 0;
}
