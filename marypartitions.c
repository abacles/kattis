#include <stdio.h>
#include <math.h>

int main()
{
  int ncases, c, base, num, hp, mp[9][10001], next, i, j, k;
  for(scanf("%d", &ncases), c=0;c<ncases;)
    {
      scanf("%d %d %d", &c, &base, &num);
      hp = log2(num) / log2(base);
      for(i=0;i<=num;i++)
	mp[0][i] = 1;
      for(i=1;i<=hp;i++)
	{
	  mp[i][0] = 1;
	  next = pow(base, i+1);
	  for(j=1;j<=num && j<=next;j++)
	    {
	      for(mp[i][j]=k=0;k<
	    }
	}
    }
}
