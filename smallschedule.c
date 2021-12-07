#include <stdio.h>

int main()
{
  int bigtime, nmach, nsmall, nbig, time;
  scanf("%d %d %d %d", &bigtime, &nmach, &nsmall, &nbig);
  time = bigtime * (nbig / nmach);
  if (nbig % nmach > 0)
    {
      nsmall -= (nmach - nbig % nmach) * bigtime;
      time += bigtime;
    }
  if (nsmall > 0)
    {
      time += nsmall / nmach;
      if (nsmall % nmach > 0)
        time++;
    }
  printf("%d\n", time);
}
