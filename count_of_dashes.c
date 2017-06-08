/* You are given a string, which contains entirely of decimal digits (0-9). Each digit is made of a certain number of dashes.
For instance 1 is made of 2 dashes, 8 is made of 7 dashes and so on. 
You have to write a function that takes this string message as an input and returns a corresponding value in terms of a number. 
This number is the count of dashes in the string message.
0 consists of 6 dashes, 1 consists of 2 dashes, 2 consists of 5 dashes, 3 consists of 5 dashes, 4 consists of 4 dashes, 
5 consists of 5 dashes, 6 consists of 6 dashes, 7 consists of 3 dashes, 8 consists of 7 dashes, 9 consists of 6 dashes. 

SAMPLE INPUT
12134

SAMPLE OUTPUT
18
*/
#include <stdio.h>
#include<string.h>
int main(){
    char a[100];
    int sum=0;
    scanf("%s",a);
    for(int i=0;i<strlen(a);i++){
        switch(a[i]){
            case 48:
                sum+=6;
                break;
            case 49:
                sum+=2;
                break;
            case 50:
                sum+=5;
                break;
            case 51:
                sum+=5;
                break;
            case 52:
                sum+=4;
                break;
            case 53:
                sum+=5;
                break;
            case 54:
                sum+=6;
                break;
            case 55:
                sum+=3;
                break;
            case 56:
                sum+=7;
                break;
            case 57:
                sum+=6;
                break;
        }
    }
    printf("%d",sum);
    return 0;
}