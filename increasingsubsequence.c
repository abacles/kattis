#include <stdio.h>

int is[200][200];

int less(int a, int b, int len)
{
  int i;
  for(i=0;i<len;i++)
    {
      if(is[a][i] < is[b][i])
	return 1;
      else if(is[a][i] > is[b][i])
	return 0;
    }
  return 0;
}

int main()
{
  int nnums, seq[200], len[200], ml, i, j, k;
  while(scanf("%d", &nnums), nnums)
    {
      for(i=0;i<nnums;i++)
	{
	  scanf("%d", &seq[i]);
	  len[i] = 1;
	  for(j=0;j<i;j++)
	    {
	      if(seq[j] < seq[i] &&
		 (len[j]+1 > len[i] || (len[j]+1 == len[i] && less(j, i, len[j]))))
		{
		  len[i] = len[j]+1;
		  for(k=0;k<len[j];k++)
		    is[i][k] = is[j][k];
		}
	    }
	  is[i][len[i]-1] = seq[i];
	}
      for(ml=i=0;i<nnums;i++)
	{
	  if(len[i] > len[ml] || (len[i] == len[ml] && less(i, ml, len[i])))
	    ml = i;
	}
      printf("%d", len[ml]);
      for(i=0;i<len[ml];i++)
	printf(" %d", is[ml][i]);
      printf("\n");
    }
}
