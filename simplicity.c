#include <stdio.h>
#include <string.h>

int main()
{
  char str[101];
  int counts[26] = {0}, most_common = 0, second_common = 0, distinct = 0, i;
  scanf("%s", str);
  for (i=0; str[i]; i++)
    counts[str[i] - 'a']++;
  for (i=0; i<26; i++)
    {
      if (counts[i] > most_common)
        {
          second_common = most_common;
          most_common = counts[i];
        }
      else if (counts[i] > second_common)
        second_common = counts[i];
      if (counts[i] > 0)
        distinct++;
    }
  if (distinct > 2)
    printf("%d\n", (int)strlen(str) - most_common - second_common);
  else
    printf("0\n");
}
