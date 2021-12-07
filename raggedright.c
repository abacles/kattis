#include <stdio.h>

int main()
{
  int raggedness = 0, line_lengths[100] = {0}, maxlen = 0, i = 0, j;
  char ch;
  while ((ch = getchar()) != EOF)
    {
      if (ch == '\n')
        i++;
      else
        line_lengths[i]++;
    }
  for (j=0; j<i; j++)
    if (line_lengths[j] > maxlen)
      maxlen = line_lengths[j];
  for (j=0; j<i-1; j++)
    raggedness += (maxlen - line_lengths[j]) * (maxlen - line_lengths[j]);
  printf("%d\n", raggedness);
}
