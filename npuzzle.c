#include <stdio.h>

int abs(int x)
{
  return x > 0 ? x:-x;
}

int main()
{
  char row[5];
  int i, j, di, dj, scatter = 0;
  for (i=0; i<4; i++)
    {
      scanf("%s", row);
      for (j=0; j<4; j++)
        {
          di = (row[j]-'A') / 4;
          dj = (row[j]-'A') % 4;
          if (row[j] != '.')
            scatter += abs(di-i) + abs(dj-j);
        }
    }
  printf("%d\n", scatter);
}
