#include <stdio.h>
#include <string.h>

int main()
{
  char trades[100001];
  long int queries;
  long int i,j,c,q,len;
  scanf("%s",trades);
  scanf("%ld",&queries);
  len = strlen(trades);
  for(q=0;q<queries;q++)
    {
      scanf("%ld %ld",&i,&j);
      c = 0;
      for(;i<len && j<len;i++,j++,c++)
	{
	  if(trades[i] != trades[j])
	    break;
	}
      printf("%ld\n",c);
    }
}
