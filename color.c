#include <stdio.h>
#include <stdlib.h>

int cmp(const void *pa, const void *pb)
{
  int a = *(int *)pa, b = *(int *)pb;
  return a == b ? 0 : (a < b ? -1:1);
}

int main()
{
  int nsocks, mcap, maxdiff, socks[100000], nmachines = 0, firstsock, i, j;
  scanf("%d %d %d", &nsocks, &mcap, &maxdiff);
  for (i=0; i<nsocks; i++)
    scanf("%d", &socks[i]);
  qsort(socks, nsocks, sizeof (int), cmp);
  for (i=0; i<nsocks; )
    {
      nmachines++;
      firstsock = socks[i];
      for (j=0; (i+j < nsocks && j<mcap &&
                 socks[i+j] - firstsock <= maxdiff); j++);
      i += j;
    }
  printf("%d\n", nmachines);
}
