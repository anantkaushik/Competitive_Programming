/*Write a program that prints the numbers in the given range. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz". Print a new line after each string or number.
Input Format First line will be the number of testcases, T. Next line will have T integers, denoted by N
Output Format For each testcase, print the number from 1 to N. But follow the rules given in the problem statement.*/
//Practice question from hackerearth. 

#include <stdio.h>
void main(){
    int cases,n,i;
    scanf("%d",&cases);
    while(cases!=0){
        scanf("%d",&n);
         for(i=1;i<=n;i++){
            if(i%3==0 && i%5==0)
                printf("\nFizzBuzz");            
            else if(i%3==0 & i%5!=0)
                printf("\nFizz");
            else if(i%5==0 && i%3!=0)
                printf("\nBuzz");
            else
                printf("\n%d",i);
         }
         cases--;
    }
}
