#include <stdio.h>

void next(char *str,int len)
{
  int i;
  for(i=len-1;i>=0;i--)
  {
    if(str[i] == '0')
    {
      str[i] = '1';
      return;
    }
    str[i] = '0';
  }
}

int dec(char *str,int len)
{
  int d = 0, dig = 1, i;
  for(i=len-1;i>=0;i--,dig*=2)
    d += (str[i]-'0') * dig;
  return d;
}

int main()
{
  int nth, count[30] = {0,1}, found, clen, hlen, i;
  char binstr[100] = {0};
  scanf("%d",&nth);
  for(found=1,clen=1;found<nth;)
  {
    if(clen%2 == 0)
      count[clen+1] = count[clen] * 2;
    else
      count[clen+1] = count[clen];
    found += count[++clen];
  }
  binstr[0] = '1';
  hlen = !(clen%2) ? clen/2 : clen/2 + 1;
  for(i=1;i<hlen;i++) binstr[i] = '0';
  for(i=1;i<nth-(found-count[clen]);i++)
    next(binstr,hlen);
  for(i=0;i<hlen;i++)
    binstr[clen-1-i] = binstr[i];
  binstr[clen] = 0;
  printf("%d\n",dec(binstr,clen));
}
