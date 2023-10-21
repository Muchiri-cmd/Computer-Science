#include <stdio.h>

int main(){
    //defining variables
   int shillings,dataBundles;

   //Prompt the user to enter amount in shillings
   printf("Enter the amount in shillings: ");
   scanf("%d",&shillings);

   //calculate number of bundles (1SH=5MB)
   dataBundles=shillings * 5;

   //Display bundles
   printf("You have purchased :%d\n",dataBundles);

   return 0;

}

