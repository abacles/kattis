#include <stdio.h>
#include <stdlib.h>

int max(int x, int y)
{
  return x>y ? x:y;
}

int main()
{
  int k, *calendar = calloc(1000000, sizeof (int)), **maxfilms, d, i, j;
  calendar = calloc(1000000, sizeof (int));
  maxfilms = malloc(sizeof (int *) * 1000001);
  /* 
     maxfilms[i][j] is the max # of films they can watch after i days;
     j stores who liked the last film.
   */
  for (i=1; i<=2; i++)
    {
      scanf("%d", &k);
      for (j=0; j<k; j++)
        {
          scanf("%d", &d);
          calendar[d] += i;
        }
    }
  maxfilms[0] = malloc(2 * sizeof (int));
  maxfilms[0][0] = maxfilms[0][1] = 0;
  for (i=1; i<=1000000; i++)
    {
      maxfilms[i] = malloc(2 * sizeof (int));
      maxfilms[i][0] = maxfilms[i-1][0];
      maxfilms[i][1] = maxfilms[i-1][1];
      if (calendar[i-1] == 1)
        {
          /* first guy likes today's movie */
          if (maxfilms[i-1][1] + 1 > maxfilms[i][0])
            maxfilms[i][0] = maxfilms[i-1][1] + 1;
        }
      else if (calendar[i-1] == 2)
        {
          /* second guy likes today's movie */
          if (maxfilms[i-1][0] + 1 > maxfilms[i][1])
            maxfilms[i][1] = maxfilms[i-1][0] + 1;
        }
      else if (calendar[i-1] == 3)
        maxfilms[i][0] = maxfilms[i][1] = max(maxfilms[i-1][0],
                                              maxfilms[i-1][1]) + 1;
    }
  printf("%d\n", max(maxfilms[1000000][0], maxfilms[1000000][1]));
}
