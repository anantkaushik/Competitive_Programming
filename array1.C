/*Given an array of positive integers,the task is that we find a
subset of size greater than one with maximum product*/
#include<conio.h>
#include<stdio.h>
void main(){
	int i,n,j,temp;
	int a[] = {1,5,7,2,0};
	clrscr();
	n=sizeof(a)/sizeof(a[0]);
	for(i=0;i<n;i++){
		for(j=0;j<n-i-1;j++){
			if(a[j] > a[j+1]){
				temp = a[j];
				a[j] = a[j+1];
				a[j+1] = temp;
			}
		}
	}
	printf("\nThe subset containing %d and %d produces maximum geometric mean.\n",a[n-2],a[n-1]);
	getch();
}