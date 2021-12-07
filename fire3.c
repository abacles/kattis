#include <stdio.h>

int escape(char m[1000][], int r, int c)
{
  int i, d, q[4000][2], qsize = 1, fq[4000][2], fqsize = 0;
  for (i=0; i<r; i++)
    for (j=0; j<c; j++)
      {
        if (m[i][j] == 'J')
          {
            q[0][0] = i;
            q[0][1] = j;
            m[i][j] = '.';
          }
        else if (m[i][j] == 'F')
          {
            fq[fqsize][0] = i;
            fq[fqsize++][1] = j;
          }
      }
  while (qsize > 0)
    {
      for (i=0; i<fqsize; i++)
        {
          for (d=-1; d<=1; d+=2)
            {
              if (0 <= fq[i][0]+d && fq[i][0]+d < r &&
                  m[fq[i][0]+d][fq[i][1]] == '.')
                {
                  m[fq[i][0]+d][fq[i][1]] = 'F';
                }
              if (0 <= fq[i][1]+d && fq[i][1]+d < r &&
                  m[fq[i][0]][fq[i][1]+d] == '.')
                m[fq[i][0]][fq[i][1]+d] = 'F';
            }
        }
    }
  return -1;
}

int main()
{
  int r, c, i, tmp;
  char maze[1000][1001];
  scanf("%d %d", &r, &c);
  for (i=0; i<r; i++)
    scanf("%s", maze[i]);
  if ((tmp = escape(maze, r, c) >= 0)
    printf("%d\n", tmp);
  else
    printf("IMPOSSIBLE\n");
}
