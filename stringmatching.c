#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct ll
{
  int elem;
  struct ll *next;
};

int *prefix(char *p,int plen)
{
  int *bl = malloc(sizeof(int)*plen),border = 0,i;
  bl[0] = 0;
  for(i=1;i<plen;i++)
  {
    while(border > 0 && p[i] != p[border])
      border = bl[border-1];
    if(p[i] == p[border]) border++;
    else border = 0;
    bl[i] = border;
  }
  return bl;
}

struct ll *kmp(char *p,char *t)
{
  int plen = strlen(p),tlen = strlen(t),*blen,i;
  char *s = malloc(sizeof(char) * (plen + 1 + tlen + 1));
  struct ll *occ = NULL,*tail = occ;
  strcpy(s,p);
  s[plen] = '$';
  strcpy(s+plen+1,t);
  blen = prefix(s,plen+1+tlen);
  for(i=plen+1;i<plen+1+tlen;i++)
  {
    if(blen[i] == plen)
    {
      if(tail)
      {
        tail->next = malloc(sizeof(struct ll));
        tail = tail->next;
      }
      else occ = tail = malloc(sizeof(struct ll));
      tail->elem = i - 2*plen;
      tail->next = NULL;
    }
  }
  free(blen);
  return occ;
}

int main()
{
  char pattern[5000000],text[5000000];
  struct ll *matches;
  while(gets(pattern))
  {
    gets(text);
    matches = kmp(pattern,text);
    if(!matches) printf("\n");
    for(;matches;matches=matches->next)
      printf("%d%c",matches->elem,matches->next?' ':'\n');
  }
}

