#include<stdio.h>

void main()
{
	int arr[100];
	int n,i,left,right,mid,search,c=0;
	printf("Enter the no of elements in array");
	scanf("%d",&n);
	printf("Enter the elements in the array in sorted order:");
	for( i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
		
	}
	printf("enter the element to be searched");
	scanf("%d",&search);
	
	left=0;
	right=n-1;
	while(left<=right)
	{
		mid=(int)(left+right)/2;
		if(search==arr[mid])
		{
			printf("Element found at position %d",(mid+1));
			c=1;
			break;
		}
		else if(arr[mid]<search)
		   left=mid+1;
		else if(arr[mid]>search)
		    right=mid-1;
			   
	}
	if(c==0)
	{
		printf("element not found");
	}
}
