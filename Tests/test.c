#include <stdio.h>
#include <conio.h>
#include<windows.h>
#include<stdlib.h>
#include<string.h>

/*int main()
{
	char filename[] = "smtp.py";
	FILE* fp;

	Py_Initialize();

	fp = _Py_fopen(filename, "r");
	PyRun_SimpleFile(fp, filename);

	Py_Finalize();
	return 0;
}*/

/*void main()
{
	system("C:\Users\admin\Desktop\CS LAB\mini project\smtp.py");
}*/

/*int main()
{
	char filename[20],pin[6];
	printf("Input the name of the hospital with extension(.csv): ");
	scanf("%s",filename);
	printf("Enter the hospital's area pincode: ");
	scanf("%s",pin);
	FILE *fp;
	fp=fopen(filename,"w");
	fclose(fp);
	fp=fopen("Hospital_list.csv","a+");
	fprintf("%s,%s",filename,pin);
	fclose(fp);
	return 0;
}*/

/*int main()
{
	char line[500],result[3];
	FILE *fp,*new;
	fp=fopen("record.csv","r");
	new=fopen("new.csv","w");
	while(fgets(line,500,fp)!=NULL)
	{
		char *name=strtok(line,",");
		char *mobile=strtok(NULL,",");
		char *srn=strtok(NULL,",");
		char *mail=strtok(NULL,",");
		char *status=strtok(NULL,",");
		if(!strcmp(status,"1"))
		{	
			char *res=strtok(NULL,",");
			fprintf(new,"%s,%s,%s,%s,%s,%s\n",name,mobile,srn,mail,status,res);
		}
		if(!strcmp(status,"0"))
		{
			printf("Name : %s\nSRN : %s\n",name,srn);
			printf("Enter the RESULT : ");
			scanf("%s",result);
			if(!strcmp(result,"+"))
				fprintf(new,"%s,%s,%s,%s,%s,%s\n",name,mobile,srn,mail,"1","positive");
			if(!strcmp(result,"-"))
				fprintf(new,"%s,%s,%s,%s,%s,%s\n",name,mobile,srn,mail,"1","negative");
		}
	}
	fclose(fp);
	fclose(new);
	remove("record.csv");
    rename("new.csv","record.csv");
}*/

int main()
{
	system("C://Users//admin//Desktop//CS_LAB//mini_project//Tests//test.py");
}