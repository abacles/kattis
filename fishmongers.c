#include <stdio.h>
#include <stdlib.h>

int cmp(const void *pa, const void *pb)
{
  int a = *(int *)pa, b = *(int *)pb;
  return a == b ? 0 : (a > b ? -1:1);
}

int main()
{
  int n, m, w[100000], xp[100000][2], i, monger;
  long long monies = 0;
  scanf("%d %d", &n, &m);
  for (i=0; i<n; i++)
    scanf("%d", &w[i]);
  for (i=0; i<m; i++)
    scanf("%d %d", &xp[i][1], &xp[i][0]);
  /* sort in descending order */
  qsort(w, n, sizeof (int), cmp);
  qsort(xp, m, sizeof (int) * 2, cmp);
  for (i=monger=0; i<n; i++)
    {
      if (xp[monger][1] == 0)
        monger++;
      monies += (long long int)w[i] * xp[monger][0];
      xp[monger][1]--;
    }
  printf("%lld\n", monies);
}
