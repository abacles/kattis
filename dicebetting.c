#include <stdio.h>

int main()
{
  int nthrows, nsides, diff, i, j;
  double prob[500][10000];
  scanf("%d %d %d",&nthrows,&nsides,&diff);
  for(i=0;i<nthrows;i++)
    {
      prob[0][i] = 1;
      for(j=i+1;j<diff;j++)
	prob[j][i] = 0;
      for(j=1;j<=i && j<diff;j++)
	prob[j][i] = prob[j][i-1] + (prob[j-1][i-1]-prob[j][i-1]) * (nsides-j) / nsides;
    }
  printf("%.10f\n", prob[diff-1][nthrows-1]);
}
