#include <stdio.h>
#include <string.h>

int main()
{
  int a, b, x, y, i, ncarry, c;
  while (1)
    {
      scanf("%d %d", &a, &b);
      if (a == 0 && b == 0)
        break;
      ncarry = c = 0;
      while (a > 0 || b > 0)
        {
          x = a % 10;
          y = b % 10;
          if (x + y + c >= 10)
            {
              ncarry++;
              c = 1;
            }
          else
            c = 0;
          a /= 10;
          b /= 10;
        }
      if (!ncarry)
        printf("No carry operation.\n");
      else
        printf("%d carry %s.\n", ncarry, ncarry == 1 ? "operation":"operations");
    }
}
