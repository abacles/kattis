#include <stdio.h>

int main()
{
  int q, k, i, j, a, b, next, seen_before[1000];
  scanf("%d", &q);
  for (i=0; i<q; i++)
    {
      scanf("%d", &k);
      a = b = 1;
      for (j=0; j<1000; seen_before[j++] = 0);
      for (j=2; ; j++)
        {
          next = (a + b) % k;
          if (seen_before[next]) break;
          seen_before[next] = j;
          a = b, b = next;
        }
      printf("%d\n", seen_before[next]);
    }
}
