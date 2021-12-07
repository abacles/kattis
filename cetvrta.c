#include <stdio.h>

int main()
{
  int a,b,c,d,e,f,g,h;
  scanf("%d%d%d%d%d%d",&a,&b,&c,&d,&e,&f);
  if(a == c) g = e;
  else if(a == e) g = c;
  else g = a;
  if(b == d) h = f;
  else if(b == f) h = d;
  else h = b;
  printf("%d %d\n",g,h);
}
