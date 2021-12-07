#include <stdio.h>

int main()
{
  int r, c, zr, zc, i, j, k, l;
  char line[51];
  scanf("%d %d %d %d", &r, &c, &zr, &zc);
  for(i=0;i<r;i++)
    {
      scanf("%s", line);
      for(l=0;l<zr;l++)
	{
	  for(j=0;j<c;j++)
	    {
	      for(k=0;k<zc;k++)
		printf("%c", line[j]);
	    }
	  printf("\n");
	}
    }
}
