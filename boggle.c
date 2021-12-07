#include <stdio.h>
#include <string.h>

int find(char *str, int k[16][26][8], int p[16][26], char v[16], int pos)
{
  int i;
  if(!str[0])
    return 1;
  v[pos] = 1;
  for(i=0; i<p[pos][str[0]-'A']; i++)
    {
      if(!v[k[pos][str[0]-'A'][i]] &&
	 find(&str[1], k, p, v, k[pos][str[0]-'A'][i]))
	{
	  v[pos] = 0;
	  return 1;
	}
    }
  v[pos] = 0;
  return 0;
}

int main()
{
  int w, b, kiwi[16][26][8], pear[16][26], top[26][16], tc[26] = {0}, totscore, nwords, score_table[6] = {1, 1, 2, 3, 5, 11}, i, j, k, l, tmp;
  char dictionary[300000][9], board[4][5], longest[9], visited[16];
  scanf("%d", &w);
  for(i=0; i<w; i++)
    scanf("%s", dictionary[i]);
  scanf("%d", &b);
  for(i=0; i<b; i++)
    {
      for(j=0; j<4; j++)
	scanf("%s", board[j]);
      memset(pear, 0, 16*26*sizeof(int));
      memset(visited, 0, 16);
      for(j=0; j<16; j++)
        {
	  for(k=-1; k<=1; k++)
            {
	      for(l=-1; l<=1; l++)
                {
		  if((k || l) && (0 <= (j/4)+k && (j/4)+k < 4 &&
				  0 <= (j%4)+l && (j%4)+l < 4))
                    {
		      tmp = board[j/4+k][j%4+l] - 'A';
		      kiwi[j][tmp][pear[j][tmp]++] = j + 4*k + l;
                    }
                }
            }
	  top[board[j/4][j%4]-'A'][tc[board[j/4][j%4]-'A']++] = j;
        }
      totscore = nwords = 0;
      longest[0] = '\0';
      for(j=0; j<w; j++)
        {
	  for(k=0; k<tc[dictionary[j][0]-'A']; k++)
            {
	      if(find(&dictionary[j][1], kiwi, pear, visited, top[dictionary[j][0]-'A'][k]))
                {
		  tmp = strlen(dictionary[j]);
		  totscore += score_table[tmp-3];
		  nwords++;
		  if(tmp > strlen(longest) || (tmp == strlen(longest) && strcmp(dictionary[j], longest) < 0))
		    strcpy(longest, dictionary[j]);
		  break;
                }
            }
        }
      getchar();
      printf("%d %s %d\n", totscore, longest, nwords);
    }
}
