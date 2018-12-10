/* You are on a game show "Who Wants to Be a Millionaire".The host presents you "N" number of closed doors.There is huge prize behind one door while 
there are sumo wrestlers behind rest of the doors.Initially you are asked to choose a door.After that the host opens (N-2) doors,revealing sumo wrestlers.
The host is omniscient and always reveals sumo wrestlers when he opens the doors. The host then says to you.""Do you want to pick the door you have 
initially chosen or you want to chose the other closed door?".So it's your decision either stick with your original unopened door or switch to the other 
unopened door.You are good at maths so you will first calculate the probability of winning the prize by switching from the original selection.
INPUT:
the first line contain number of testcases "T". "T" testcases follows then.Each testcase contains the number of doors "N".
OUTPUT:
for each testcase output the probability of winning the prize by switching from the original selection.output upto 6 places of decimal.

SAMPLE INPUT
1
3
SAMPLE OUTPUT
0.666667
*/
#include <stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    while(t>0){
        double n,p;
        scanf("%lf",&n);
        p=(n-1)/n;
        printf("%.6lf\n",p);
        t--;
    }
    return 0;
}