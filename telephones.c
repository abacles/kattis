#include <stdio.h>

int main()
{
  int ncalls, nint, st[10000], dur[10000], is, id, i, j, k;
  while(scanf("%d %d", &ncalls, &nint), ncalls || nint)
    {
      for(i=0;i<ncalls;i++)
	scanf("%d %d %d %d", &j, &k, &st[i], &dur[i]);
      for(i=0;i<nint;i++)
	{
	  scanf("%d %d", &is, &id);
	  for(k=j=0;j<ncalls;j++)
	    {
	      if((st[j] <= is && is < st[j]+dur[j]) ||
		 (st[j] < is+id && is+id <= st[j]+dur[j]) ||
		 (is <= st[j] && st[j]+dur[j] <= is+id))
		k++;
	    }
	  printf("%d\n", k);
	}
    }
}
