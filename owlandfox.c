#include <stdio.h>

int main()
{
    int cases,num,i,place;
    scanf("%d",&cases);
    for(i=0;i<cases;i++)
    {
        scanf("%d",&num);
        for(place=10;num%place==0;place*=10) {}
        num -= place/10;
        printf("%d\n",num);
    }
    return 0;
}
