#include <stdio.h>
#include <stdlib.h>

int cmp(const void *pa, const void *pb)
{
  int a = *(int *)pa, b = *(int *)pb;
  return a == b ? 0 : (a < b ? 1:-1);
}

int main()
{
  int n, a[15], ab[2] = {0}, i;
  scanf("%d", &n);
  for (i=0; i<n; i++)
    scanf("%d", &a[i]);
  qsort(a, n, sizeof (int), cmp);
  for (i=0; i<n; i++)
    ab[i%2] += a[i];
  printf("%d %d\n", ab[0], ab[1]);
}
