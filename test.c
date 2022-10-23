#include<stdio.h>
#include<windows.h>
typedef struct stud
{
	char name[20];
	char SRN[20];
	int subj[5];
	int sem;
	struct stud *link;
}STUDENT;

void swap(STUDENT *a,STUDENT*b)
{
    STUDENT temp;
    strcpy(temp.name,a->name);
    strcpy(temp.SRN,a->SRN);
    temp.sem=a->sem;
    for(int i=0;i<5;i++)
        temp.subj[i]=a->subj[i];
    
    strcpy(a->name,b->name);
    strcpy(a->SRN,b->SRN);
    a->sem=b->sem;
    for(int i=0;i<5;i++)
        a->subj[i]=b->subj[i];

    strcpy(b->name,temp.name);
    strcpy(b->SRN,temp.SRN);
    b->sem=temp.sem;
    for(int i=0;i<5;i++)
        b->subj[i]=temp.subj[i];
    
}

int main()
{
    STUDENT a={"Shashank","PES1UG20CS689",{10,20,30,40,50},3},b={"Viresh","PES1UG20CS701",{20,40,60,80,100},3};
    swap(&a,&b);
    printf("After swap\n");
    printf("a.name : %s\t\tb.name : %s\na.SRN : %s\t\tb.SRN : %s\n",a.name,b.name,a.SRN,b.SRN);
    
}