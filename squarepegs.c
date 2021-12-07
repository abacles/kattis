#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int cmp(const void *pa, const void *pb)
{
  double a = *(double *)pa, b = *(double *)pb;
  return a == b ? 0 : (a < b ? -1:1);
}

int main()
{
  int nplots, ncircles, nsquares, tmp, i, nexthouse, fits;
  double plotsize[100], housesize[200];
  scanf("%d %d %d", &nplots, &ncircles, &nsquares);
  for (i=0; i<nplots; i++)
    scanf("%lf", &plotsize[i]);
  for (i=0; i<ncircles; i++)
    scanf("%lf", &housesize[i]);
  for (i=0; i<nsquares; i++)
    {
      scanf("%d", &tmp);
      housesize[ncircles + i] = tmp / sqrt(2);
    }
  qsort(plotsize, nplots, sizeof (double), cmp);
  qsort(housesize, ncircles + nsquares, sizeof (double), cmp);
  nexthouse = fits = 0;
  for (i=0; i<nplots; i++)
    {
      if (nexthouse < ncircles + nsquares &&
          plotsize[i] > housesize[nexthouse])
        {
          nexthouse++;
          fits++;
        }
    }
  printf("%d\n", fits);
}
