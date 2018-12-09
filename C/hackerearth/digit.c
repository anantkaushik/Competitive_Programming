/* Given A Number N, Find The Number Of Digits In N.
Input Format: First Line Take Input Value Of N
Output Format: Number Of Digits In N

SAMPLE INPUT
12345678

SAMPLE OUTPUT
8
*/
#include <stdio.h>
int main(){
    int x,count=0;
    while((x=getchar())!=EOF){
        count++;
    }
    printf("%d",count);
    return 0;
}