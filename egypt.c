#include <stdio.h>

void swap(int *x, int *y)
{
  int temp = *x;
  *x = *y;
  *y = temp;
}

int main()
{
  int a, b, c;
  while (1)
    {
      scanf("%d %d %d", &a, &b, &c);
      if (!a && !b && !c) break;
      if (a > b && a > c)
        swap(&a, &c);
      else if (b > a && b > c)
        swap(&b, &c);
      printf("%s\n", a*a + b*b == c*c ? "right":"wrong");
    }
}
