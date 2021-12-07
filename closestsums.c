#include <stdio.h>
#include <stdlib.h>

int main()
{
  int c,nc,nums[1000],qc,q,i,j,k,closest = -1;
  for(c=1;scanf("%d",&nc) != EOF;c++)
    {
      for(i=0;i<nc;i++) scanf("%d",&nums[i]);
      printf("Case %d:\n",c);
      scanf("%d",&qc);
      for(i=0;i<qc;i++)
	{
	  scanf("%d",&q);
	  for(j=0;j<nc;j++)
	    {
	      for(k=j+1;k<nc;k++)
		{
		  if(closest == -1 || abs(q-(nums[j]+nums[k])) < abs(q-closest))
		    closest = nums[j]+nums[k];
		}
	    }
	  printf("Closest sum to %d is %d.\n",q,closest);
	}
    }
}
