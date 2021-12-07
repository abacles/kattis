#include <stdio.h>

int reachable(int xrow, char xcol, int yrow, char ycol)
{
  int rowdiff = xrow - yrow, coldiff = xcol - ycol;
  return rowdiff == coldiff || rowdiff == -coldiff;
}

int main()
{
  int ncases, i, xrow, yrow, r;
  char xcol, ycol, c, solved;
  scanf("%d", &ncases);
  getchar();
  for (i=0; i<ncases; i++)
    {
      scanf("%c %d %c %d", &xcol, &xrow, &ycol, &yrow);
      getchar();
      if (xcol == ycol && xrow == yrow)
        printf("0 %c %d\n", xcol, xrow);
      else
        {
          solved = 0;
          for (r=1; r<=8 && !solved; r++)
            for (c='A'; c<='H' && !solved; c++)
              {
                if (!(r == xrow && c == xcol) &&
                    reachable(r, c, xrow, xcol))
                  {
                    if (r == yrow && c == ycol)
                      {
                        printf("1 %c %d %c %d\n", xcol, xrow, c, r);
                        solved = 1;
                      }
                    else if (reachable(yrow, ycol, r, c))
                      {
                        printf("2 %c %d %c %d %c %d\n",
                               xcol, xrow, c, r, ycol, yrow);
                        solved = 1;
                      }
                  }
              }
          if (!solved)
            printf("Impossible\n");
        }
    }
}
