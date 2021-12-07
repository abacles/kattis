#include <stdio.h>
#include <stdlib.h>

struct stick
{
  int *bot, nbot, nbotcap, ntop;
} *tower;

void stack(int t, int b)
{
  if(tower[t].nbot == tower[t].nbotcap)
    tower[t].bot = realloc(tower[t].bot, sizeof(int)*(tower[t].nbotcap *= 2));
  tower[t].bot[(tower[t].nbot)++] = b;
  tower[b].ntop++;
}

void topsort(int n)
{
  int *order = malloc(sizeof(int)*n), *top = malloc(sizeof(int)*n), nt = 0, v, i, j;
  for(i=0;i<n;i++)
    {
      if(!tower[i].ntop)
	top[nt++] = i;
    }
  for(i=0;i<n;i++)
    {
      if(!nt)
        {
	  printf("IMPOSSIBLE\n"); free(order); free(top);
	  return;
        }
      v = order[i] = top[--nt];
      for(j=0;j<tower[v].nbot;j++)
        {
	  tower[tower[v].bot[j]].ntop--;
	  if(!tower[tower[v].bot[j]].ntop)
	    top[nt++] = tower[v].bot[j];
        }
    }
  for(i=0;i<n;i++)
    printf("%d\n", order[i]+1);
  free(order); free(top);
}

int main()
{
  int nsticks, nstack, u, v, i;
  scanf("%d %d", &nsticks, &nstack);
  tower = malloc(sizeof(struct stick) * nsticks);
  for(i=0;i<nsticks;i++)
    {
      tower[i].bot = malloc(sizeof(int));
      tower[i].nbot = tower[i].ntop = 0;
      tower[i].nbotcap = 1;
    }
  for(i=0;i<nstack;i++)
    {
      scanf("%d %d", &u, &v);
      stack(u-1, v-1);
    }
  topsort(nsticks);
  for(i=0;i<nsticks;i++)
    free(tower[i].bot);
  free(tower);
}
