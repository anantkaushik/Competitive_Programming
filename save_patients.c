/* A new deadly virus has infected large population of a planet. A brilliant scientist has discovered a new strain of virus which can cure this disease. 
Vaccine produced from this virus has various strength depending on midichlorians count. A person is cured only if midichlorians count in vaccine batch is 
more than midichlorians count of person. A doctor receives a new set of report which contains midichlorians count of each infected patient, Practo stores 
all vaccine doctor has and their midichlorians count. You need to determine if doctor can save all patients with the vaccines he has. The number of vaccines 
and patients are equal.

Input Format
First line contains the number of vaccines - N.Second line contains N integers, which are strength of vaccines. 
Third line contains N integers, which are midichlorians count of patients.

Output Format
Print a single line containing ′Yes′ or ′No′.

SAMPLE INPUT
5
123 146 454 542 456
100 328 248 689 200

SAMPLE OUTPUT
No
*/
#include <stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int v[n],p[n],i,j;
    for(i=0;i<n;i++)
        scanf("%d",&v[i]);
    for(i=0;i<n;i++)
        scanf("%d",&p[i]);
    int swap;
    for(i=0;i<n-1;i++){
        for(j=0;j<n-i-1;j++){
            if(v[j]>v[j+1]){
                swap=v[j];
                v[j]=v[j+1];
                v[j+1]=swap;
            }
            if(p[j]>p[j+1]){
                swap=p[j];
                p[j]=p[j+1];
                p[j+1]=swap;
            }
        }
    }
    for(i=0;i<n;i++){
        if(v[i]<p[i]){
            printf("No");
            break;
        }
        else if(i==n-1)
            printf("Yes");
    }
    return 0;
}