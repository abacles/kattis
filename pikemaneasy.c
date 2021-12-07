#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b)
{
  int ia = *(int*)a, ib = *(int*)b;
  if(ia == ib) return 0;
  return ia < ib ? -1 : 1;
}

int main()
{
  int nprob, time, a, b, c, t[10000], tsum = 0, pen = 0, i;
  scanf("%d %d", &nprob, &time);
  scanf("%d %d %d %d", &a, &b, &c, &t[0]);
  for(i=1;i<nprob;i++)
    t[i] = ((long long)a*t[i-1]+b) % c + 1;
  qsort(t, nprob, sizeof(int), cmp);
  for(i=0; i<nprob && tsum+t[i]<=time; i++)
    {
      tsum += t[i];
      pen = ((long long)pen + tsum) % 1000000007;
    }
  printf("%d %d\n", i, pen);
}
