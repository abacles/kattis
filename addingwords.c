#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define OCEAN 10007

struct ht
{
  char key[31];
  int v;
  struct ht *n;
};

void setup(struct ht table[])
{
  int i;
  for(i=0; i<OCEAN; i++)
    {
      table[i]->v = 1001;
      table[i]->n = NULL;
    }
}

void destroy(struct ht table[])
{
  int i;
  struct ht *a, *b;
  for(i=0; i<OCEAN; i++)
    {
      for(a=table[i]->n; a; a=b)
	{
	  b = a->n;
	  free(a);
	}
    }
}

int hash(char *s)
{
  int h = *s;
  while(*(++s) != '\0')
    h = (h*31 + *s) % OCEAN;
  return h;
}

void add(struct ht table[], char *s, int val)
{
  int h = hash(s);
  struct ht *a;
  for(a=table[h]; a->n; a=a->n) // here
    {
      if(a->v != 1001 && strcmp(a->key, s) == 0)
	{
	  a->v = val;
	  return;
	}
    }
}

int main()
{
  char cmd[5], args[600], buffer[600], *var, *next, op;
  int val, tmp, unk;
  struct ht table[OCEAN];
  setup(table);
  while(scanf("%s", cmd) != EOF)
    {
      if(cmd[1] == 'e')
	{
	  scanf("%s %d", args, &val);
	}
      else if(cmd[1] == 'a')
	{
	  fgets(args, 600, stdin);
	  next = strcpy(buffer, args+1);
	  var = strsep(&next, " ");
	  val = get(htable, var);
	  unk = val > 1000;
	  while(!unk && (op = next[0]) != '=')
	    {
	      next = &next[2];
	      var = strsep(&next, " ");
	      tmp = get(htable, var);
	      unk = tmp > 1000;
	      val = (op == '+' ? val+tmp : val-tmp);
	    }
	}
      else
	{
	  destroy(table);
	  setup(table);
	}
    }
  destroy(table);
}
