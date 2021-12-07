#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>

#define MIN(A, B) ((A)<(B) ? (A):(B))

struct list
{
  int num;
  struct list *next;
};

void list_insert(struct list *node, int new)
{
  struct list *new_node = malloc(sizeof(struct list));
  new_node->num = new;
  new_node->next = node->next;
  node->next = new_node;
}

void route_insert(int n, int tour[], int **dist)
{
  int i, j, k, l;
  char in_tour[1000] = {0};
  int dist2tour[1000], mindist = -1;
  struct list *head = malloc(sizeof(struct list)), *current, *best, *temp;

  if (n == 1)
    {
      tour[0] = 0;
      return;
    }

  /* initialize tour to the 2 closest cities */
  for (i=0; i<n; i++)
    for (j=i+1; j<n; j++)
      if (dist[i][j] < mindist || mindist == -1)
	{
	  mindist = dist[i][j];
	  k = i;
	  l = j;
	}
  in_tour[k] = in_tour[l] = 1;
  head->num = k;
  head->next = head;
  list_insert(head, l);

  /* compute the distance of each city to the tour */
  for (i=0; i<n; i++)
    dist2tour[i] = MIN(dist[i][k], dist[i][l]);

  /* build tour */
  for (i=2; i<n; i++)
    {
      mindist = -1;
      for (j=0; j<n; j++) // look for closest city
	if (!in_tour[j] && (dist2tour[j] < mindist || mindist == -1))
	  {
	    mindist = dist2tour[j];
	    k = j;
	  }
      in_tour[k] = 1;
      for (j=0; j<n; j++) // update distances to the tour with new city
	if (!in_tour[j] && dist[j][k] < dist2tour[j])
	  dist2tour[j] = dist[j][k];
      
      /* place the new city into the tour */
      current = head;
      mindist = -1;
      do // look for best location to insert
	{
	  if (dist[current->num][k] + dist[k][current->next->num] - dist[current->num][current->next->num] < mindist || mindist == -1)
	    {
	      mindist = dist[current->num][k] + dist[k][current->next->num] - dist[current->num][current->next->num];
	      best = current;
	    }
	  current = current->next;
	} while (current != head);
      list_insert(best, k); // insert
    }
  current = head;
  i = 0;
  do
    {
      tour[i++] = current->num;
      temp = current;
      current = current->next;
      free(temp);
    } while (current != head);
}

int main()
{
  int ncities, tour[1000], *pairdist[1000], i, j;
  double x[1000], y[1000];

  scanf("%d", &ncities);
  
  for (i=0; i<ncities; i++)
    scanf("%lf %lf", &x[i], &y[i]);

  for (i=0; i<ncities; i++)
    pairdist[i] = malloc(sizeof(int) * ncities);
  for (i=0; i<ncities; i++)
    for (j=i; j<ncities; j++)
      pairdist[i][j] = pairdist[j][i] = round(hypot(x[i]-x[j], y[i]-y[j]));
  
  route_insert(ncities, tour, pairdist);
  
  for (i=0; i<ncities; i++)
    printf("%d\n", tour[i]);

  for (i=0; i<ncities; free(pairdist[i++]));
}
