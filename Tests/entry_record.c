#include<stdio.h>
#include<windows.h>
#include<stdlib.h>
#include<float.h>
#include<string.h>

void entry_record(void)
{
    int c=1;
    system("cls");
    FILE *ptr;
    ptr=fopen("record.csv","a+");
    while(c)
    {
        system("cls");
        printf("\t\t\t======NEW ENTRY======\n");
        printf("\nEnter the name: ");
        scanf("%s",&add.name);
        printf("Enter the SRN: ");
        scanf("%s",&add.SRN);
        printf("Enter the E-Mail ID: ");
        scanf("%s",&add.mailid);
        printf("Enter the phone number: ");
        scanf("%lld",&add.mobile_no);
        fprintf(ptr,"%s,%lld,%s,%s,%d,%s\n",add.name,add.mobile_no,add.SRN,add.mailid,0,"NA");
        printf("\n\nPress '1' to make another entry and '0' to quit entry");
        scanf("%d",&c);
    }
    fclose(ptr);
}