#include <stdio.h>

void sretan(int k)
{
  int length, count, totcount = 0;
  if (k == 0) return;
  for (length = 1, count = 2; totcount+count < k; length++, count *= 2)
    totcount += count;
  if (k <= totcount + count/2)
    {
      printf("4");
      sretan(k - count/2);
    }
  else
    {
      printf("7");
      sretan(k - count);
    }
}

int main()
{
  int k;
  scanf("%d", &k);
  sretan(k);
  printf("\n");
}

/*
  4 7 . 44 47 74 77 . 444 447 474 477 744 747 774 777
 */
