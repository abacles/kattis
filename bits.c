#include <stdio.h>
#include <string.h>

int bits(int x)
{
  int b = 0;
  while (x > 0)
    {
      b += x%2;
      x >>= 1;
    }
  return b;
}

int main()
{
  int t, i, x, j, len, b, maxb;
  char s[20];
  scanf("%d", &t);
  getchar();
  for (i=0; i<t; i++)
    {
      scanf("%s", s);
      len = strlen(s);
      x = 0;
      maxb = 0;
      for (j=0; j<len; j++)
        {
          x = x*10 + s[j] - '0';
          b = bits(x);
          if (b > maxb)
            maxb = b;
        }
      printf("%d\n", maxb);
    }
}
