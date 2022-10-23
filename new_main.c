#include<stdio.h>
#include<windows.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>

struct data
{
    char name[60],mobile_no[12],SRN[20],SRN_x[50],mailid[50],result[20];
    int test;
}add,upd;

void entry_record(void);
void result_upd(void);
void mailing(void);
void hosp_allocate(void);
void hosp_add(void);
void discharge(void);
void final_touch(void);

int main()
{
    int ex;
    do
    {
        system("cls");
        printf("\t\t\tNATIONAL COVID CARE PORTAL\n\t\t\t=========================== \n\n");
        printf("\t\t1.Enter data for COVID Testing\n\t\t2.Enter the RTPCR Result\n\t\t3.Send mail to the tested people\n\t\t4.Allocate Hospitals\n\t\t5.Register Hospital to this Portal\n\t\t6.Update number of patients discharged");
        int choice,n=1;
        printf("\n\n\nEnter your choice : ");
        scanf("%d",&choice);
        if(choice==1)
        {
            entry_record();
            printf("\a");
            printf("\n=========================================================\n\tPress '1' to go back to MAIN menu and '0' to exit the program\n");
            scanf("%d",&ex);
        }
        if(choice==2)
        {
            result_upd();
            printf("\a");
            printf("\n=========================================================\n\tPress '1' to go back to MAIN menu and '0' to exit the program\n");
            scanf("%d",&ex);
        }
        if(choice==3)
        {
            mailing();
            printf("\a");
            printf("\n=========================================================\n\tPress '1' to go back to MAIN menu and '0' to exit the program\n");
            scanf("%d",&ex);
        }
        if(choice==4)
        {
            hosp_allocate();
            printf("\a");
            printf("\n\n=========================================================\n\tPress '1' to go back to MAIN menu and '0' to exit the program\n");
            scanf("%d",&ex);
        }
        if(choice==5)
        {
            hosp_add();
            printf("\a");
            printf("\n=========================================================\n\tPress '1' to go back to MAIN menu and '0' to exit the program\n");
            scanf("%d",&ex);
        }
        if(choice==6)
        {
            discharge();
            printf("\a");
            printf("\n=========================================================\n\tPress '1' to go back to MAIN menu and '0' to exit the program\n");
            scanf("%d",&ex);
        }
        if(choice==0)
        {
            system("cls");
            final_touch();
            exit(0);
        }

    } while(ex);
    system("cls");
    final_touch();
    return 0;   
}

void entry_record(void)
{
    int c1=1;
    system("cls");
    printf("\n\t\tDETAILS OF THE PATIENT UNDERGOING SWAB TEST\n\t\t===========================================\n");
    FILE *ptr;
    ptr=fopen("record.csv","a+");
    while(c1)
    {
        printf("\nEnter the name: ");
        scanf("%s",&add.name);
        printf("Enter the SRN: ");
        scanf("%s",&add.SRN);
        printf("Enter the E-Mail ID: ");
        scanf("%s",&add.mailid);
        printf("Enter the phone number: ");
        scanf("%s",&add.mobile_no);
        fprintf(ptr,"%s,%s,%s,%s,%s\n",add.name,add.mobile_no,add.SRN,add.mailid,"NA");
        printf("\n\nPress '1' to make another entry and '0' to quit entry : ");
        scanf("%d",&c1);
        printf("-------------------------------------------------------------\n");
    }
    fclose(ptr);
}

void result_upd(void)
{
    int lnum,count=0;
    char line[500],result[5];
    system("cls");
    printf("\n\t\t\tUPDATES ON SWAB TEST RESULT\n\t\t\t=============================\n");
    printf("*The Name and the SRN of the people are displayed on the screen.\n");
    printf("*In the Result row, Enter '+' for POSITIVE result and '-' for NEGATIVE result\n");
    FILE *ld, *nld, *csvf1, *csvf2;
    ld=fopen("last_data.txt","r");
    fscanf(ld,"%d",&lnum);
    fclose(ld);
    csvf1=fopen("record.csv","r");
    csvf2=fopen("new_record.csv","w");
    for(int i=0;i<lnum;i++)
    {
        fgets(line,500,csvf1);
        fprintf(csvf2,"%s",line);
        ++count;
    }
    while(fgets(line,500,csvf1))
    {
        char *name=strtok(line,",");
        char *mobile=strtok(NULL,",");
        char *srn=strtok(NULL,",");
        char *mailid=strtok(NULL,",");
        printf("\nNAME : %s\nSRN : %s\nResult : ",name,srn);
        scanf("%s",result);
        if(!strcmp(result,"+"))
            fprintf(csvf2,"%s,%s,%s,%s,%s,%s\n",name,mobile,srn,mailid,"positive","0");
        if(!strcmp(result,"-"))
            fprintf(csvf2,"%s,%s,%s,%s,%s,%s\n",name,mobile,srn,mailid,"negative","0");
        ++count;
    }

    if(count==lnum)
        printf("\n\n\t\tTHERE ARE NO NEW SWAB TEST ENTRIES AVAILABLE\n");
    fclose(csvf1);
    fclose(csvf2);

    remove("record.csv");
	rename("new_record.csv","record.csv");

    nld=fopen("newlast_data.txt","w");
    fprintf(nld,"%d",count);
    fclose(nld);

    remove("last_data.txt");
	rename("newlast_data.txt","last_data.txt");

}

void mailing(void)
{
    system("cls");
    printf("\nBASED ON THE RESULTS, PEOPLE GET THE MAIL OF THIER COVID-19 SWAB TEST.\n");
    printf("PEOPLE WITH POSITIVE RESULTS GET A FORM ATTACHED WITH THEIR SWAB TEST REPORT THROUGH THIS MAIL.\n");
    system("C://Users//admin//Desktop//CS_LAB//mini_project-2//smtp_res_mail.py");
}

void hosp_add(void)
{
    system("cls");
    int c5;
    char hospital[50],pin[7],beds[4];
    printf("\n\t\tHOSPITAL REGISTRATION TO COVID PORTAL\n\t\t====================================\n");
    printf("Steps to register a hospital to COVID portal :\n\n");
    printf("1.Go to the smtp_hosp_mail.py file to create a server in the name of the hospital\n");
    printf("2.In the smtp_hosp_mail.py file the format is given.\n");
    printf("3.Enter the hospital details in the format and remove the comments on that format.\n");
    printf("4.Once the details are entered correctly, save the file and exit.\n");
    printf("\n\n Once it is done, Press 1 to continue.....");
    scanf("%d",&c5);
    if(c5)
    {
        FILE *hp;
        hp=fopen("Hospital_list.csv","a");
        printf("\nEnter the Registered Hospital name : ");
        scanf("%s",hospital);
        printf("Enter the pincode of the hospital : ");
        scanf("%s",pin);
        printf("Enter the number of BEDS given under Govt. Quota : ");
        scanf("%s",beds);
        fprintf(hp,"%s,%s,%s\n",hospital,pin,beds);
        fclose(hp);
    }
    printf("\n\n%s HOSPITAL REGISTERED TO COVID PORTAL SUCCESSFULLY\n",hospital);
}

void hosp_allocate(void)
{
    system("cls");
    printf("\nBASED ON THE AREA PINCODE OF THE INFECTED PERSON, HOSPITAL IS ALLOCATED\n");
    printf("ANY OF THE INFECTED PERSON NOT GETTING THE BED WILL RECEIVE A MAIL CONTAINING A FORM TO FILL FOR HOSPITAL ALLOTMENT.\n");
    printf("WE REGRET FOR THE INCONVENIENCE CAUSED\n");
    system("C://Users//admin//Desktop//CS_LAB//mini_project-2//smtp_hosp_mail.py");
}

void discharge(void)
{
    system("cls");
    printf("\n\t\tRECORD OF OUT PATIENT NUMBER\n\t\t=============================\n");
    char buff[500];
    FILE *ptr1, *ptr2;
    ptr1=fopen("Hospital_list.csv","r");
    ptr2=fopen("uwhosp.csv","w");
    while(fgets(buff,500,ptr1))
    {
        int n,x;
        char *hosp=strtok(buff,",");
        char *pin=strtok(NULL,",");
        char *avl_bed=strtok(NULL,"\n");
        sscanf(avl_bed,"%d",&x);
        printf("\nPresently there are %s beds available in %s(%s) Hospital\n",avl_bed,hosp,pin);
        printf("Enter the number of patients discharged : ");
        scanf("%d",&n);
        printf("----------------------------------------------------------\n");
        fprintf(ptr2,"%s,%s,%d",hosp,pin,(x+n));
    }
    fclose(ptr1);
    fclose(ptr2);

    remove("Hospital_list.csv");
    rename("uwhosp.csv","Hospital_list.csv");
}

void final_touch(void)
{
    FILE *xrp=fopen("final.txt","r");
	char ch;
	while((ch=fgetc(xrp))!=EOF)
	{
		printf("%c",ch);
		Sleep(50);
	}
    printf("\a");
}