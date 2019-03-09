#include <stdio.h>
#include <cs50.h>
#include <math.h>

int change(int cents);
int main(void)
{
    // INPUT STAGE
    float input;
    do
    {
        printf("O hai! How much change is owed?\n");
        input = get_float();
    }
    while(input < 0);

    // THE OUTPUT
    printf("%d\n", change( (int)round(input*100) )   );
}

/*
@return : minimum number of change
@parameter : cents in integer form
*/
int change (int cents)
{
    // 25 // (whatever's remaining) 10   // (wvr rmg) 5 //(wvr rmg) 1
    return cents / 25 + (cents % 25) / 10 + ((cents % 25) % 10)/5 + ((cents%25)%10)%5;
}
