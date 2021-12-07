#include <stdio.h>

int max(int a, int b)
{
  return a > b ? a : b;
}
int curve(int i, int s)
{
  return (i < s) ? i+1 : (2*s-1)-i;
}

char status(char b[][1001], int s, int w)
{
  int i, j, dil, djl, dir, djr, ch, cv;
  for(i=0;i<s;i++)
    {
      for(j=ch=cv=0;j<s;j++)
	{
	  ch = (ch && b[i][j] == b[i][j-1]) ? ch + 1 : 1;
	  if(ch >= w && b[i][j] != '.')
	    return b[i][j];
	  cv = (cv && b[j][i] == b[j-1][i]) ? cv + 1 : 1;
	  if(cv >= w && b[j][i] != '.')
	    return b[j][i];
	}
    }
  for(i=0;i<2*s-1;i++)
    {
      dil = dir = max(s-i-1, 0);
      djl = max(i-s+1, 0);
      djr = (i < s) ? s - 1 : (2*s-1) - i - 1;
      for(j=ch=cv=0;j<curve(i,s);j++)
	{
	  ch = (ch && b[dil+j][djl+j] == b[dil+j-1][djl+j-1]) ? ch + 1 : 1;
	  if(ch >= w && b[dil+j][djl+j] != '.')
	    return b[dil+j][djl+j];
	  cv = (cv && b[dir+j][djr-j] == b[dir+j-1][djr-j+1]) ? cv + 1 : 1;
	  if(cv >= w && b[dir+j][djr-j] != '.')
	    return b[dir+j][djr-j];
	}
    }
  return '.';
}

int count(char b[][1001], int s, char which)
{
  int i, j, c = 0;
  for(i=0;i<s;i++)
    {
      for(j=0;j<s;j++)
	{
	  if(b[i][j] == which)
	    c++;
	}
    }
  return c;
}

int main()
{
  int size, wincd, xc, oc, cs, i, j;
  char board[1001][1001];
  scanf("%d %d", &size, &wincd);
  for(i=0;i<size;i++)
    scanf("%s", board[i]);
  xc = count(board, size, 'X'), oc = count(board, size, 'O');
  if(xc > oc+1 || xc < oc)
    printf("ERROR\n");
  else if((cs = status(board, size, wincd)) != '.')
    {
      if(cs == 'O' && xc > oc || cs == 'X' && xc == oc)
	{
	  printf("ERROR\n");
	  return 0;
	}
      for(i=0;i<size;i++)
	{
	  for(j=0;j<size;j++)
	    {
	      if(board[i][j] == cs)
		{
		  board[i][j] = '.';
		  if(status(board, size, wincd) == '.')
		    {
		      printf("%c WINS\n", cs);
		      return 0;
		    }
		  board[i][j] = cs;
		}
	    }
	}
      printf("ERROR\n");
    }
  else if(xc + oc < size * size)
    printf("IN PROGRESS\n");
  else
    printf("DRAW\n");
}
