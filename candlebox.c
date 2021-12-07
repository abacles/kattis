#include <stdio.h>

int sum(int start, int end)
{
  return (start + end) * (end-start+1) / 2;
}

int main()
{
  int diff, rbox, tbox, rita, theo;
  scanf("%d%d%d", &diff, &rbox, &tbox);
  for (rita=4; ; rita++)
    {
      theo = rita - diff;
      if (rbox + tbox == sum(4, rita) + sum(3, theo))
        break;
    }
  printf("%d\n", rbox - sum(4, rita));
}

/*
  26 = 4 + 5 + 6 + 7 + (4)
  8 = 3 + 4 + 5 - (4)
 */
