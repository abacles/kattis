#include <stdio.h>
#include <stdlib.h>

struct ll
{
  char ch;
  struct ll *next, *prev;
};

struct ll *insert(struct ll *h, char ch)
{
  /* insert a new node after h */
  struct ll *new = malloc(sizeof (struct ll));
  new->ch = ch;
  new->prev = h;
  new->next = h->next;
  h->next = new;
  new->next->prev = new;
  return new;
}

struct ll *delete(struct ll *h)
{
  struct ll *tmp = h->prev;
  h->prev->next = h->next;
  h->next->prev = h->prev;
  free(h);
  return tmp;
}

int main()
{
  struct ll head, tail, *current = &head;
  char ch;
  head.next = &tail;
  tail.prev = &head;
  while ((ch = getchar()) != EOF && ch != '\n')
    {
      if (ch == 'L')
        current = current->prev;
      else if (ch == 'R')
        current = current->next;
      else if (ch == 'B')
        current = delete(current);
      else
        current = insert(current, ch);
    }
  for (current = head.next; current != &tail; current = current->next)
    putchar(current->ch);
  putchar('\n');
}
