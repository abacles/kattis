#include <stdio.h>
#include <string.h>

int mapping[] = {0,0,1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,3};

int main()
{
  char apple[10001],swine[5001];
  int costs[4],alen,i,j,k,cost,mincost = 100000000;
  scanf("%s%s",apple,swine);
  for(i=0;i<4;i++) scanf("%d",&costs[i]);
  for(alen=strlen(apple),i=0;i<=alen;i++)
    {
      for(cost=0,j=0,k=0;swine[j];j++)
	{
	  if(i+k>=alen || apple[i+k] != swine[j])
	    cost += costs[mapping[swine[j]-'A']];
	  else k++;
	}
      if(cost < mincost) mincost = cost;
    }
  printf("%d\n",mincost);
}
