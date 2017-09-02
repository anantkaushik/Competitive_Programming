/*Given a sorted array with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.*/ 
#include<conio.h>
#include<stdio.h>
void main(){
	int n,num,a[100],i,first=-1,last=-1;
	clrscr();
	printf("\nEnter the length of the array: ");
	scanf("%d",&n);
	printf("\nEnter %d integers in a sorted manner: ",n);
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	printf("\nEnter the number: ");
	scanf("%d",&num);
	for(i=0;i<n;i++){
		if(num==a[i]){
			if(first == -1)
				first = i;
			last=i;
		}
	}
		if(first!=-1){
			printf("\nFirst Occurrence=%d",first);
			printf("\nLast Occurrence=%d",last);
		}
		else
			printf("%d is not present in the array.",num);
	getch();
}
