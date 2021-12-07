#include <stdio.h>
#include <string.h>

long long b2d(char s[], int base)
{
  long long n = 0, pv = 1;
  int i;
  for(i=strlen(s)-1; i>=0; i--)
  {
    n += (s[i]-'0') * pv;
    pv *= base;
  }
  return n;
}

void d2b(long long n, int base, char s[])
{
  char reversed[10] = "";
  int i = 0, j;
  while(n > 0)
  {
    reversed[++i] = '0' + n % base;
    n /= base;
  }
  if(i == 0)
    reversed[++i] = '0';
  for(j=0; i>=0; i--, j++)
    s[j] = reversed[i];
}

long long mod(char p[], char m[], int base, char r[])
{
  long long bot = b2d(m, base), top = 0;
  int i;
  for(i=0; p[i]; i++)
  {
    top = base * top + (p[i] - '0');
    top = top % bot;
  }
  return top;
}

int main()
{
  int base;
  char p[1001], m[10], rem[10];
  while(scanf("%d", &base), base)
  {
    scanf("%s %s", p, m);
    d2b(mod(p, m, base, rem), base, rem);
    printf("%s\n", rem);
  }
}
