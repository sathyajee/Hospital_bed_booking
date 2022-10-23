#include<stdio.h>
#include<windows.h>
#include<stdlib.h>
#include<float.h>
#include<string.h>


struct data
{
    char name[60],SRN[60],SRN_x[50],mailid[50],result[20];
    long long int mobile_no;
    int test;
}add,upd;


int main()
{
    system("cls");
    printf("\t\t\t\t COVID CARE PORTAL \n\n");
    printf("\t\t1.Enter data for COVID Testing\n\t\t2.Enter the RTPCR Result\n\t\t3.Search for Hospitals\n\t\t4.Hospital Management\n");
    int choice,n=1;
    printf("\n\tEnter your choice: ");
    scanf("%d",&choice);
    if(choice==1)
    {
        int c=1;
        FILE *ptr;
        ptr=fopen("record.csv","a+");
        fprintf(ptr,"NAME,PHONE NO.,SRN,E-MAIL,TESTING,RESULT\n");
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
            printf("\n\nWant to enter another Entry: ");
            scanf("%d",&c);
        }
        fclose(ptr);
    }

    /*if(choice==2)
    {
        int c2=1;
        system("cls");
        printf("ENTER '+' for positive and '-' for negative result\n");
        FILE *old, *new;
        old=fopen("record.csv","r");
        new=fopen("new.csv","w");
        /*printf("Enter the SRN(last 5 characters) for which the RESULT to be entered\n");
        upd.SRN="PES1UG20";
        scanf("%s",&upd.SRN_x);
        strcat(upd.SRN,upd.SRN_x);
        while(fscanf(old,"%s,%lld,%s,%s",&add.name,&add.mobile_no,&add.SRN,&add.mailid))
        {
            printf("NAME : %s\nSRN : %s\n",add.name,add.SRN);
            printf("Enter the RESULT : ");
            scanf("%s",&upd.result);
            if(upd.result=="+")
                upd.result[20]="positive";
            if(upd.result=="-")
                upd.result[20]="negative";
            fprintf(new,"%s,%lld,%s,%s,%d,%s\n",add.name,add.mobile_no,add.SRN,add.mailid,1,upd.result);
            printf("------------------RESULT UPDATED----------------------------\n");
        }
        fclose(old);
        fclose(new);
        remove("record.csv");
        rename("new.csv","record.csv");
    }*/
    return 0;
}