#include <stdio.h>
#include <string.h>

char xorhash(char *s)
{
  char h = *s;
  while(*(++s) != '\n')
    h ^= *s;
  return h;
}

long long strhash(char *s)
{
  long long h = *s;
  while(*(++s) != '\n')
    h = (h*31 + *s) % 1000000007;
  return h;
}

int main()
{
  int n, ncollisions, ndups, i, j;
  char files[500][52], xhash[500], tmp;
  long long shash[500];
  while(scanf("%d", &n), n != 0)
    {
      getchar();
      for(i=0; i<n; i++)
	{
	  fgets(files[i], 52, stdin);
	  xhash[i] = xorhash(files[i]);
	  shash[i] = strhash(files[i]);
	}
      ncollisions = ndups = 0;
      for(i=0; i<n; i++)
	{
	  tmp = 0;
	  for(j=i+1; j<n; j++)
	    {
	      if(xhash[i] == xhash[j])
		{
		  if(shash[i] == shash[j] && strcmp(files[i], files[j]) == 0)
		    tmp = 1;
		  else
		    ncollisions++;
		}
	    }
	  ndups += tmp;
	}
      printf("%d %d\n", n-ndups, ncollisions);
    }
}
