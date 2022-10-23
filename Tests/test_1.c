#include<stdio.h>
#include<windows.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>

int main()
{
	FILE *xrp=fopen("final.txt","r");
	char ch;
	while((ch=fgetc(xrp))!=EOF)
	{
		printf("%c",ch);
		Sleep(50);
	}
}

