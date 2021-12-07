#include <stdio.h>

int main()
{
  int n, junk, minjunk = 0x7fffffff, wait, i;
  scanf("%d", &n);
  for(i=0;i<n;i++)
    {
      scanf("%d", &junk);
      if(junk < minjunk)
	{
	  minjunk = junk;
	  wait = i;
	}
    }
  printf("%d\n", wait);
}
