#include <stdio.h>
#include <stdlib.h>

int cmp(const void *pa, const void *pb)
{
  int a = *(int *)pa, b = *(int *)pb;
  return a == b ? 0 : (a < b ? -1:1);
}

int main()
{
  int n, t[100000], mid, step, direction, i;
  scanf("%d", &n);
  for (i=0; i<n; i++)
    scanf("%d", &t[i]);
  qsort(t, n, sizeof (int), cmp);
  mid = n / 2;
  printf("%d", t[mid]);
  for (step=1; ; step++)
    {
      for (direction=-1; direction<=1; direction+=2)
        {
          i = mid + step * direction;
          if (i < 0 || i >= n)
            {
              printf("\n");
              return 0;
            }
          printf(" %d", t[i]);
        }
    }
}
