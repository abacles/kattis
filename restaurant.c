#include <stdio.h>

int main()
{
  int n, m, left, right, i;
  char action[5];
  while(scanf("%d", &n), n != 0)
    {
      left = right = 0;
      for(i=0; i<n; i++)
	{
	  scanf("%s %d", action, &m);
	  if(action[0] == 'D')
	    {
	      printf("DROP 1 %d\n", m);
	      left += m;
	    }
	  else
	    {
	      if(m <= right)
		{
		  printf("TAKE 2 %d\n", m);
		  right -= m;
		}
	      else
		{
		  if(right > 0)
		    printf("TAKE 2 %d\n", right);
		  printf("MOVE 1->2 %d\n", left);
		  printf("TAKE 2 %d\n", m - right);
		  right = left + right - m;
		  left = 0;
		}
	    }
	}
      printf("\n");
    }
}
