#include <stdio.h>

int main()
{
  int n, cards[100000], top = 0, nextcard, i;
  scanf("%d", &n);
  for (i=0; i<n; i++)
    {
      scanf("%d", &nextcard);
      if (top > 0 && (cards[top-1] + nextcard) % 2 == 0)
        top--;
      else
        cards[top++] = nextcard;
    }
  printf("%d\n", top);
}
