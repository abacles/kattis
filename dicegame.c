#include <stdio.h>

int main()
{
  int gdia,gdib,gdiia,gdiib;
  int edia,edib,ediia,ediib;
  float ga,ea;
  scanf("%d %d %d %d",&gdia,&gdib,&gdiia,&gdiib);
  scanf("%d %d %d %d",&edia,&edib,&ediia,&ediib);
  ga=1.0*(gdia+gdib)/2+1.0*(gdiia+gdiib)/2;
  ea=1.0*(edia+edib)/2+1.0*(ediia+ediib)/2;
  if(ea>ga)
    printf("Emma\n");
  else if(ga>ea)
    printf("Gunnar\n");
  else
    printf("Tie\n");
}
