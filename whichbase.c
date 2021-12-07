#include <stdio.h>

int main()
{
  char val[8];
  int ncases, c, oct, dec, hex, i;
  for(scanf("%d",&ncases),c=0;c<ncases;)
    {
      scanf("%d %s", &c, val);
      for(oct=i=0;val[i] && val[i]<'8';i++);
      if(!val[i])
	sscanf(val, "%o", &oct);
      sscanf(val, "%d", &dec);
      sscanf(val, "%x", &hex);
      printf("%d %d %d %d\n", c, oct, dec, hex);
    }
}
