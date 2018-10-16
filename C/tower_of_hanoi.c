/*tower of hanoi problem using recursive algorithm 
@ishanisri
*/

#include<stdio.h>




void Hanoi(int n,char source, char dest, char aux){
	if(n==1){
		printf("move 1 from %c to %c\n",source,dest);
	}
	else{
		Hanoi(n-1,source,aux,dest);
		printf("move %d disk from %c to %c\n",n,source,dest);
		Hanoi(n-1,aux,dest,source);
	}
}
int main(){
	int n;
	printf("Enter the number of rings:");
	scanf("%d",&n);
	char source;
	char dest;
	char aux;
	printf("the steps in tower of Hanoi are: \n");
	Hanoi(n,'S','D','A');
	
	
	return 0;
}
