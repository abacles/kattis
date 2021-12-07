#include <stdio.h>
#include <string.h>

#define MAX(A, B) (A > B ? A:B)

double mem[5][5][5][5][9];

double prob(int r, int g, int b, int y, int s)
{
  double p = 0;
  int n = 2, most_fruits = MAX(MAX(r, g), MAX(b, y));

  if (mem[r][g][b][y][s] >= 0) return mem[r][g][b][y][s];

  if (r > 0)
    p += prob(r-1, g, b, y, s), n++;
  if (g > 0)
    p += prob(r, g-1, b, y, s), n++;
  if (b > 0)
    p += prob(r, g, b-1, y, s), n++;
  if (y > 0)
    p += prob(r, g, b, y-1, s), n++;

  p += prob(r, g, b, y, s-1);

  if (r == most_fruits) p += prob(r-1, g, b, y, s);
  else if (g == most_fruits) p += prob(r, g-1, b, y, s);
  else if (b == most_fruits) p += prob(r, g, b-1, y, s);
  else p += prob(r, g, b, y-1, s);

  return mem[r][g][b][y][s] = p / n;
}

int main()
{
  int r, g, b, y, s;
  for (r=0; r<5625; mem[0][0][0][0][r++] = -1);
  for (s=1; s<9; mem[0][0][0][0][s++] = 1);
  for (r=0; r<625; mem[0][0][0][r++][0] = 0);
  scanf("%d %d %d %d %d", &r, &g, &b, &y, &s);
  printf("%.10f\n", prob(r, g, b, y, s));
}
