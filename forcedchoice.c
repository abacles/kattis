#include <stdio.h>

int main()
{
  int n, p, s, m, card, keep, i, j;
  scanf("%d %d %d", &n, &p, &s);
  for (i=0; i<s; i++)
    {
      scanf("%d", &m);
      keep = 0;
      for (j=0; j<m; j++)
        {
          scanf("%d", &card);
          if (card == p)
            keep = 1;
        }
      printf("%s\n", keep ? "KEEP":"REMOVE");
    }
}
