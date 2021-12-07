#include <stdio.h>

int main()
{
  int dp[1000001], nstones, nmoves, moves[10], i, j;
  dp[0] = 0;
  while(scanf("%d %d", &nstones, &nmoves) != EOF)
    {
      for(i=0;i<nmoves;scanf("%d", &moves[i++]));
      for(i=1;i<=nstones;i++)
	{
	  dp[i] = 0;
	  for(j=0;j<nmoves;j++)
	    {
	      if(i >= moves[j] && !dp[i-moves[j]])
		{
		  dp[i] = 1;
		  break;
		}
	    }
	}
      printf("%s wins\n", dp[nstones] ? "Stan" : "Ollie");
    }
}
