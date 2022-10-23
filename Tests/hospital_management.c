#include<stdio.h>
#include<string.h>
struct Booking
{
    char name[20];
    int n,fee;
    char type[20];
}B[100];
typedef struct Booking book;
struct patient
{
    char name[20];
    char H_name[20];
    int BU_no;
    char SRN[15];
    long long int Ph_no;
}P;
void read();
void rewrite();
void display(int *p);
void Booking_patient(int *q);
//void cancel();
// void new();
int main()
{
    int a,i;
    char r;
    int d;
    i=0;
    printf("\t\t\t\t ONLINE BED_BOOKING FOR COVID PATIENTS \n\n");
    printf("Would you like to book for Hospital beds from our portal(Y/N):\n");
    scanf("%c",&r);
    if(r=='Y' or r=='y')
    {
        read();
        do
        {
            display(a);
            rewrite();
            Booking_patient(a);
            printf("select the options(0 or 1):\n");
            printf("0. for continue booking\t 1. for exit\n");
            scanf("%d",&d);
        } while (d);
    }
    printf("\t\t\tTHANK YOU FOR VISITING OUR WEBSITE");
    return 0;
}






void rewrite()
{
    int n;                                              //number of enteries.
    FILE *ptr;
    ptr=fopen("Hospital.csv","w+");
    fprintf(ptr,"Hospital_name,number_of_beds,type,fees\n");
    for(int i=0;i<1;i++)
    {
        fprintf(ptr,"%s,%d,%s,%d\n",B[i].name,B[i].n,B[i].type,B[i].fee);
    }
    fclose(ptr);
}




void display(int *p)
{
    printf("hospital_name, fee\n");
    for(int i=1;i<11;i++)
    {
        printf("%d. %s , %s",i,B[i].name,B[i].fee);
    }
    printf("Enter the hospital number that you want to book=(1-10):\n");
    scanf("%d",p);
    B[*p].n=(B[*p].n)-1;
}




// void new()
// {
//     // B[0].name='abcd';
//     // B[0].n=25;
//     // B[0].type='pri';
//     // B[0].fee=10000;
// }
// void cancel()
// {
//     int c;
//     FILE *ptr;
//     // ptr=fopen("Booked.csv","r");
//     char u[15];
//     printf()

// }




void read()
{
    char a[20],b[20],c[20];
    FILE *ptr;
    ptr=fopen("data1.csv","r");
    if(ptr==NULL)
    {
        printf("the file do not exist\n");
    }
    else
    {
        fscanf(ptr,"%[^,]s %[^,]s %[^\n]s\n",&a,&b,&c);
        for(int i=0;i<10;i++)
        {
            fscanf(ptr,"%[^,]s %[^,]d %[^\n]s",&B[i].name,&B[i].n,B[i].fee);
        }
    }
    fclose(ptr);
}




void Booking_patient(int *q)
{
    printf("name of the Patient:\n");
    scanf("%s",P.name);
    printf("Enter the BU_number:\n");
    scanf("%d",P.BU_no);
    printf("enter the contact number:\n");
    scanf("%lld",P.Ph_no);
    FILE *pt;
    pt=fopen("Patient_list.csv","a+");
    fprintf(pt,"%s , %d , %lld , %s",P.name,P.BU_no,P.Ph_no,B[*q].name);
    fclose(pt);
}