#include<stdio.h>
int main()
{
  char in = 'a';
  int buffer = 0;
  FILE *fp = NULL;
  fp = fopen("/home/archgu/computerfuck.bf","w+");
  while(in != '\n')
  {
    scanf("%c",&in);
    buffer = (int)in;
    while(buffer)
    {
      fprintf(fp,"+");
      buffer = buffer - 1;
    }
    fprintf(fp,".>");
  }
  fclose(fp);
}
