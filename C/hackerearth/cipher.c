/*Indian army is going to do a surprise attack on one of its enemies country. The President of India, the Supreme Commander of the Indian Army will be sending an alert message to all its commanding centers. As enemy would be monitoring the message, Indian army is going to encrypt(cipher) the message using basic encryption technique. A decoding key 'K' (number) would be sent secretly.

You are assigned to develop a cipher program to encrypt the message. Your cipher must rotate every character in the message by a fixed number making it unreadable by enemies.

Given a single line of string 'S' containing alpha, numeric and symbols, followed by a number '0<=N<=1000'. Encrypt and print the resulting string.

Note: The cipher only encrypts Alpha and Numeric. (A-Z, a-z, and 0-9) . All Symbols, such as - , ; %, remain unencrypted.

Sample Input:
All-convoYs-9-be:Alert1.
4
Sample Output:
Epp-gsrzsCw-3-fi:Epivx5.
*/

#include<stdio.h>

int main()
{
    char msg[100000],emsg[100000];
    int k,i=0,d,temp;
    
    scanf("%s",msg);
    scanf("%d",&k);
    while(msg[i]!='\0')
    {
        if(msg[i]>=48 && msg[i]<=57)
        {
            if(k>10){
                temp=k%10;
            }
            else
                temp = k;
            if(msg[i]+temp>57)
            {
               d=57-msg[i];
               emsg[i]=48+(temp-d-1);
            }
            
            else
              emsg[i]=msg[i]+temp;
        }
        
        else if (msg[i]>=65 && msg[i]<=90)
        {
            if(k>26){
                temp=k%26;
            }
            else
                temp = k;
            if (msg[i]+temp>90)
            {
               d=90-msg[i];
               emsg[i]=65+(temp-d-1);
            }
           
            else
              emsg[i]=msg[i]+temp;
        }
        
        else if (msg[i]>=97 && msg[i]<=122)
        { 
            if(k>26){
                temp=k%26;
            }
            else
                temp = k;
           if(msg[i]+temp>122)
           {
               d=122-msg[i];
               emsg[i]=97+(temp-d-1);
           }
        
           else
              emsg[i]=msg[i]+temp;
        }
        
        else
           emsg[i]=msg[i];
        
        i++;
    }
    
    printf("%s",emsg);
}