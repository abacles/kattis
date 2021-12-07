#include <stdio.h>
#include <stdlib.h>

int compar(const void *a,const void *b)
{
  int *na = (int*)a,*nb = (int*)b;
  return *na - *nb;
}

int abs(int n)
{
  if(n < 0) return -n;
  return n;
}

int closer(int a,int b,int g)
{
  if(abs(a-g) < abs(b-g)) return 1;
  if(abs(a-g) == abs(b-g)) return a > b;
  return 0;
}

int main()
{
  int count,weights[1000],closest[1001],i,j,k,m;
  char used[1001][1000];
  scanf("%d",&count);
  for(i=0;i<count;i++) scanf("%d",&weights[i]);
  qsort(weights,count,sizeof(weights[0]),compar);
  closest[0] = 0;
  for(j=0;j<count;j++) used[0][j] = 0;
  for(i=1;i<=1000;i++)
    {
      closest[i] = closest[i-1];
      k = i-1;
      m = -1;
      for(j=0;j<count;j++)
	{
	  if(weights[j] > i) break;
	  if(!used[i-weights[j]][j] && closer(closest[i-weights[j]] + weights[j],closest[i],i))
	    {
	      k = i-weights[j];
	      m = j;
	      closest[i] = closest[k] + weights[j];
	    }
	}
      for(j=0;j<count;j++) used[i][j] = used[k][j];
      if(m >= 0) used[i][m] = 1;
    }
  for(j=0;j<count;j++)
    if(!used[1000][j] && closer(closest[1000] + weights[j],closest[1000],1000))
      closest[1000] += weights[j];
  printf("%d\n",closest[1000]);
}
