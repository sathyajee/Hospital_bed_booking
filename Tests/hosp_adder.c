#include <stdio.h>
#include <conio.h>
#include<windows.h>
#include<stdlib.h>
#include<string.h>

int main()
{
	char pin[6];
	int bed;
	char hos[25];
	printf("Enter the name of the Hospital: ");
	scanf("%s",hos);
	printf("Enter the hospital's area pincode: ");
	scanf("%s",pin);
	printf("Enter the number of beds allocated to PES Government: ");
	scanf("%d",bed);
	FILE *fp;
	fp=fopen("Hospital_list.csv","a+");
	fprintf(fp,"%s,%s,%d\n",hos,pin,bed);
	fclose(fp);
	printf("\n=============================\n\t%s HOSPITAL HAS BEEN REGISTERED TO NATIONAL COVID PORTAL SUCCESSFULLY\n",hos);
	return 0;
}