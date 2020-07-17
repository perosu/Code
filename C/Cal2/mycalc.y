%{
#include  <stdio.h>
#include  <stdlib.h>
#define YYDEBUG 1
%}
%union {
    int int_value;
    double double_value;
}
%token <double_value> DOUBLE_LITERAL
%token ADD SUB MUL DIV CR
%token A B
%type <double_value> expression term primary_expression FIRA FIRD FIRM FIRS
%%
line_list
    : line
    | line_list line
    ;
line
    : expression CR
    {
        printf(">>%lf\n",$1);
    }
expression
    : term
    | expression ADD term
    {
        $$ = $1 + $3;
    }
    | expression SUB term
    {
        $$ = $1 - $3;
    }
    ;
term
    : primary_expression
    | FIRA
    | FIRS
    | FIRM
    | FIRD
    | term MUL primary_expression
    {
        $$ = $1 * $3;
    }
    | term DIV primary_expression
    {
        $$ = $1 / $3;
    }
FIRA
    :A DOUBLE_LITERAL ADD DOUBLE_LITERAL B
    {
        $$ = $2 + $4;
    }
FIRS
    :A DOUBLE_LITERAL SUB DOUBLE_LITERAL B
    {
        $$ = $2 - $4;
    }
FIRM
    :A DOUBLE_LITERAL MUL DOUBLE_LITERAL B
    {
        $$ = $2 * $4;
    }
FIRD
    :A DOUBLE_LITERAL DIV DOUBLE_LITERAL B
    {
        $$ = $2 / $4;
    }
primary_expression
    : DOUBLE_LITERAL
    ;
%%
int
yyerror(char const *str)
{
    extern char *yytext;
    fprintf(stderr,"parser error near %s\n",yytext);
    return 0;
}
int main(void)
{
    extern int yyparse(void);
    extern FILE *yyin;

    yyin = stdin;
    if (yyparse()) {
        fprintf(stderr,"Error ! Error ! ERROR !\n");
        exit(1);
    }
}
