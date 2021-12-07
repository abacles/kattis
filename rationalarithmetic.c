#include <stdio.h>
#include <stdlib.h>

struct frac
{
  long long int zi, mu;
};

long long int gcf(long long int a, long long int b)
{
  if(a > b) return gcf(b, a);
  if(!a) return b;
  return gcf(b % a, a);
}

struct frac smpl(struct frac orig)
{
  long long int temp;
  struct frac new;
  new.zi = orig.zi;
  new.mu = orig.mu;
  temp = gcf(llabs(new.zi), llabs(new.mu));
  new.zi = new.zi / temp;
  new.mu = new.mu / temp;
  if(new.mu < 0)
  {
    new.mu = -new.mu;
    new.zi = -new.zi;
  }
  return new;
}

struct frac add(struct frac a, struct frac b)
{
  struct frac sum;
  sum.mu = a.mu / gcf(a.mu, b.mu) * b.mu;
  sum.zi = (sum.mu / a.mu * a.zi) + (sum.mu / b.mu * b.zi);
  return smpl(sum);
}

struct frac sub(struct frac a, struct frac b)
{
  b.zi = -b.zi;
  return add(a, b);
}

struct frac mult(struct frac a, struct frac b)
{
  struct frac prod;
  prod.zi = a.zi * b.zi;
  prod.mu = a.mu * b.mu;
  return smpl(prod);
}

struct frac dvd(struct frac a, struct frac b)
{
  long long int temp = b.zi;
  b.zi = b.mu * (temp < 0 ? -1 : 1);
  b.mu = llabs(temp);
  return mult(a, b);
}

int main()
{
  int cases, i;
  char op, foo;
  struct frac a, b, c;
  for(scanf("%d", &cases),i=0;i<cases;i++)
  {
    scanf("%lld %lld %c %lld %lld%c", &a.zi, &a.mu, &op, &b.zi, &b.mu, &foo);
    a = smpl(a);
    b = smpl(b);
    if(op == '+')
      c = add(a, b);
    else if(op == '-')
      c = sub(a, b);
    else if(op == '*')
      c = mult(a, b);
    else
      c = dvd(a, b);
    printf("%lld / %lld\n", c.zi, c.mu);
  }
}
