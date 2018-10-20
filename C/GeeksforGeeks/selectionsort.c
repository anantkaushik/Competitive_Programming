#include<stdio.h>

int* sort(int arr[100])
{
	int min,i,j,n,arr[100],tmp;
	printf("Enter the no of elements of array");
	scanf("%d",&n);
	printf("enter the elements in the array :");
	for(i=0;i<n;i++)
	scanf("%d",&arr[i]);
	
	for(i=0;i<n;i++)
	{
		min=arr[i];
		
		
		for(j=i+1;j<n;j++)
		{
			if(min>arr[j])
			{ tmp=arr[j];
			  arr[j]=min;
			  min=tmp;
				
			}
		}
		
		
		tmp=arr[i];
		arr[i]=min;
		min=tmp;
		
	}
	
	
	return arr;
	
	
	
}
