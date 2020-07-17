#include<stdio.h>
int main()
{
  int b,s,g,input,output,tof,max,num1,num2,buffer = 1000,buffer1;
  printf("This program used to black hole number.\nInput a number:");
  scanf("%d",&input);
  printf("\n");
  tof = 1;
  while(tof)
  {
    b = input/100;
    s = input%100/10;
    g = input%10;
    if(b >= s)
    {
      max = b;//b>s
      if(max >= g)//g?s
      {
        if(g >= s)
        {
          num1 = b*100 + g*10 + s;
          num2 = s*100 + g*10 + b;
          buffer1 = num1 - num2;
          printf("%d\n",buffer1);
        }
        else
        {
          num1 = b*100 + s*10 + g;
          num2 = g*100 + s*10 + b;
          buffer1 = num1 - num2;
          printf("%d\n",buffer1);
        }
      }
      else//g>b>s
      {
        max = g;
        num1 = g*100 + b*10 + s;
        num2 = s*100 + b*10 + g;
        buffer1 = num1 - num2;
        printf("%d\n",buffer1);
      }
    }
    else
    {
      max = s;
      if(max >= g)//s>g
      {
        if(max >= b)//g?b
        {
          if(g>b)
          {
            num1 = s*100 + g*10 + b;
            num2 = b*100 + g*10 + s;
            buffer1 = num1 - num2;
            printf("%d\n",buffer1);
          }
          else
          {
            num1 = s*100 + b*10 + g;
            num2 = g*100 + b*10 + s;
            buffer1 = num1 - num2;
            printf("%d\n",buffer1);
          }
        }
      }
      else//g>s>b
      {
        max = g;
        num1 = g*100 + s*10 + b;
        num2 = b*100 + s*10 + g;
        buffer1 = num1 - num2;
        printf("%d\n",buffer1);
      }
    }
    if(buffer == buffer1)
    {
      printf("\nThe black hole number is %d,this number use %d times",buffer,tof-1);
      tof = 0;
    }
    else
    {
      tof = tof + 1;
      buffer = buffer1;
      input = buffer1;
    }
  }
  return 0;
}
