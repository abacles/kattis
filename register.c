#include <stdio.h>

int ok(int r[8], int cap[8])
{
  int i;
  for(i=0;i<8;i++)
    {
      if(r[i] < cap[i] - 1)
	return 1;
    }
  return 0;
}

int main()
{
  int primes[8] = {2, 3, 5, 7, 11, 13, 17, 19};
  int registers[8], carry, i, j;
  for(i=0;i<8;i++)
    scanf("%d", &registers[i]);
  for(j=0;ok(registers, primes);j++)
    {
      registers[0] = (registers[0] + 1) % 2;
      for(carry=registers[0]==0,i=1;carry;i++)
	{
	  carry = registers[i]+1 == primes[i];
	  registers[i] = (registers[i] + 1) % primes[i];
	}
    }
  printf("%d\n", j);
}
