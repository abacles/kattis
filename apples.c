#include <stdio.h>

int main()
{
  int r,c,i,j,a,qw,qr,q[50000];
  char board[50000][11],temp;
  scanf("%d %d",&r,&c);
  for(i=0;i<r;i++) scanf("%s",board[i]);
  for(j=0;j<c;j++)
    {
      qw = qr = 0;
      for(i=r-1;i>=0;i--)
	{
	  if(board[i][j] == 'a' && qw != qr)
	    {
	      a = q[qr++];
	      temp = board[a][j],board[a][j] = board[i][j],board[i][j] = temp;
	    }
	  if(board[i][j] == '.')
	    q[qw++] = i;
	  else if(board[i][j] == '#')
	    qr = qw;
	}
    }
  for(i=0;i<r;i++) printf("%s\n",board[i]);
}
