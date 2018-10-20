#include<stdio.h>

void main()
{
	int min,i,j,tmp,arr[100],n;
	printf("Enter the no of elements in array");
	scanf("%d",&n);
	printf("Enter the elements in the array:");
	for( i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
		
	}
	
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
	
	printf("the sorted array is :");
	for(i=0;i<n;i++)
		printf("%d ",arr[i]);		
	
	
	
}
