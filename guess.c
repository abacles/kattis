#include <stdio.h>

int main()
{
  int lo = 1, hi = 1000, mid;
  char status[10];
  while (1)
    {
      mid = (lo + hi) / 2;
      printf("%d\n", mid);
      fflush(stdout);
      scanf("%s", status);
      if (status[0] == 'l')
        hi = mid-1;
      else if (status[0] == 'h')
        lo = mid+1;
      else
        break;
    }
}
