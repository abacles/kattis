#include <stdio.h>
#include <string.h>

int main()
{
  int n, counts[26] = {0}, i;
  char prev[21], last, dict[100000][21], win = -1;
  scanf("%s", prev);
  scanf("%d", &n);
  for (i=0; i<n; i++)
    {
      scanf("%s", dict[i]);
      counts[dict[i][0] - 'a']++;
    }
  last = prev[strlen(prev)-1];
  if (!counts[last - 'a'])
    printf("?\n");
  else
    {
      for (i=0; i<n; i++)
        if (dict[i][0] == last)
          {
            if (win == -1)
              win = i;
            if (counts[dict[i][strlen(dict[i])-1] - 'a'] == 0 ||
                (dict[i][strlen(dict[i])-1] == last && counts[last - 'a'] == 1))
              {
                printf("%s!\n", dict[i]);
                return 0;
              }
          }
      printf("%s\n", dict[win]);
    }
}
