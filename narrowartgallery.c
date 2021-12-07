#include <stdio.h>

int max(int x, int y)
{
  return x>y ? x:y;
}

int row_max(int a[3])
{
  return max(max(a[0], a[1]), a[2]);
}

int main()
{
  int nrows, nclose, values[200][2], maxval[201][201][3], i, j, k;
  /* maxval[i][j][k] holds the maxval for the first i rows after 
     closing j rooms, and k determines which room in the ith row
     is closed:
      - 0: none
      - 1: left
      - 2: right */
  while (1)
    {
      scanf("%d %d", &nrows, &nclose);
      if (nrows == 0 && nclose == 0) break;
      for (i=0; i<nrows; i++)
        scanf("%d %d", &values[i][0], &values[i][1]);
      maxval[0][0][0] = 0;
      for (j=1; j<=nclose; j++)
        maxval[0][j][0] = maxval[0][j][1] = maxval[0][j][2] = -1;
      for (i=1; i<=nrows; i++)
        {
          for (j=0; j<=nclose; j++)
            {
              maxval[i][j][0] = maxval[i][j][1] = maxval[i][j][2] = -1;
              if (row_max(maxval[i-1][j]) != -1)
                maxval[i][j][0] = (row_max(maxval[i-1][j]) +
                                   values[i-1][0] + values[i-1][1]);
              if (j > 0)
                {
                  k = max(maxval[i-1][j-1][0], maxval[i-1][j-1][1]);
                  if (k != -1)
                    maxval[i][j][1] = k + values[i-1][1];
                  k = max(maxval[i-1][j-1][0], maxval[i-1][j-1][2]);
                  if (k != -1)
                    maxval[i][j][2] = k + values[i-1][0];
                }
            }
        }
      printf("%d\n", row_max(maxval[nrows][nclose]));
    }
}
