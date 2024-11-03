//**********  BASIC FUNCTIONS PROBLEMS IN C LANGUAGE **************

#include<math.h>
#include<stdio.h>

int power(int n,int p){
int result=1,i;
for(i=0;i<p;i++)
    result*=n;
return result;
}

/*
// 1)max(a,b,c) find he maximum number
#include<stdio.h>
int max(int,int,int);
void main(){
int a,b,c;
printf("enter three number to max in them : ");
scanf("%d%d%d",&a,&b,&c);
printf("maximum value : %d",max(a,b,c));
}
*/
int max(int a,int b,int c){
int max;
if(a>b && a>c)
    max=a;
else if(b>c)
    max=b;
else
    max=c;
return max;
}


/*
// 2)findfact(n) find the factorial
#include<stdio.h>
int findfact(int);
void main(){
int n;
printf("enter a number to find factorial : ");
scanf("%d",&n);
printf("factorial of %d : %d",n,findfact(n));
}
*/
int findfact(int n){
int fact;
if(n==0)
    return 1;
fact=n*findfact(n-1);
return fact;
}

/*
// 3)isfactor(n,x) find wheater x is a factor of n
#include<stdio.h>
int isfactor(int,int);
void main(){
int n,x,check;
printf("enter a number : ");
scanf("%d",&n);
printf("\nenter a factor : ");
scanf("%d",&x);
if(isfactor(n,x))
    printf("%d is the factor of %d ",x,n);
else
    printf("%d is not the factor of %d ",x,n);
}
*/
int isfactor(int n,int x){
if(n%x==0)
    return 1;
else
    return 0;
}


/*
// 4)findsum(n) find the number of digits
#include<stdio.h>
int find_digits(int);

void main(){
int n;
printf("enter a number : ");
scanf("%d",&n);
printf("\nthe number of digits in %d is %d",n,find_digits(n));
}
*/
int find_digits(int n){
int sum;
if(n==0)
    return 0;
n/=10;
sum=1+find_digits(n);
return sum;
}

/*
// 5)find_sum(n) find the sum of digits
#include<stdio.h>
int find_sum(int);
void main(){
int n;
printf("enter a number : ");
scanf("%d",&n);
printf("\nsum of digit is % d is %d",n,find_sum(n));
}
*/
int find_sum(int n){
int sum,r;
if(n==0)
    return 0;
r=n%10;
n/=10;
sum=r+find_sum(n);
return sum;
}


/*
// 6)reverse_number(n) reverse a number

#include<stdio.h>
int reverse_number(int);
void main(){
int n;
printf("enter a number : ");
scanf("%d",&n);
printf("\nreverse of % d is %d",n,reverse_number(n));
}
*/
//without recursion*************************
int reverse_number(int n){
int reverse=0,t,rev,k;
t=find_digits(n);
while(n!=0){
    t--;
    rev=n%10;
    reverse+=rev*power(10,t);
    n/=10;
}
return reverse;

}

// 7)is_palindrome(n) check the number is palindrome or not

int is_palindrome(int n){
    int reverse=reverse_number(n);
    if(reverse==n)
        return 1;
    else
        return 0;
}
/*
void main(){
int n;
printf("enter a number : ");
scanf("%d",&n);
if(is_palindrome(n))
    printf("%d is in palindrome",n);
else
    printf("%d is not in palindrome",n);
}

*/

// 8)is_prime(n) check a number is prime or not
#include<stdio.h>

int is_prime(int n){
int i;
for(i=2;i<=n/2;i++){
    if(n%i==0)
        return 0;
}
return 1;
}

/*
void main(){
int n;
printf("enter a number : ");
scanf("%d",&n);
if(is_prime(n))
    printf("%d is in prime",n);
else
    printf("%d is not in prime",n);
}

*/


//9)is_perfect(n) check a number is perfect or not

int is_perfect(int n){
    int i,sum=0;
    for(i=1;i<=n/2;i++){
        if(n%i==0)
            sum+=i;
    }
    if(sum==n)
        return 1;
    else
        return 0;
}

/*
void main(){
int n;
printf("enter a number : ");
scanf("%d",&n);
if(is_perfect(n))
    printf("%d is perfect",n);
else
    printf("%d is not perfect",n);
}
*/

// 10)generate_prime_numbers(n)

void generate_prime_numbers(int n){
int i;
for(i=2;i<=n;i++){
    if(is_prime(i))
        printf("%d ",i);
    }
}

/*
void main(){
int n;
printf("enter a number : ");
scanf("%d",&n);
generate_prime_numbers(n);
}
*/

// 11)is_amstrong(n)
int is_amstrong_support(int n,int k){
int i,r;
int sum;
if(n==0)
    return 0;
r=n%10;
n/=10;
sum=power(r,k)+is_amstrong_support(n,k);
//printf("sum : %d",sum);
return sum;
}
int is_amstrong(int n){
if(n==0){return 1;}
int k=find_digits(n);
int t=is_amstrong_support(n,k);
if(t==n){return 1;}
else{return 0;}

}
/*
void main(){
int n;
printf("enter a number : ");
scanf("%d",&n);
if(is_amstrong(n)){printf("\n%d is an amstrong number",n);}
else{printf("\n%d is not an amstrong number",n);}
}
*/

//12)view_all_prime(x,y) print all prime within the range

void view_all_prime(int x,int y){
int i;
for(i=x;i<=y;i++)
    if(is_prime(i))
        printf("%d ",i);
}

/*
void main(){
int x,y;
printf("enter the range : ");
scanf("%d%d",&x,&y);
view_all_prime(x,y);
}
*/

// 13)view_all_perfect(x,y)

void view_all_amstrong(int x,int y){
int i;
for(i=x;i<=y;i++)
    if(is_amstrong(i))
        printf(" %d ",i);
}
/*
void main(){
int x,y;
printf("enter the range : ");
scanf("%d%d",&x,&y);
view_all_amstrong(x,y);
}
*/

//  13)view_all_perfect(x,y)

void view_all_perfect(int x,int y){
int i;
for(i=x;i<=y;i++)
    if(is_perfect(i))
        printf("%d ",i);
}
/*
void main(){
int x,y;
printf("enter the range : ");
scanf("%d%d",&x,&y);
view_all_perfect(x,y);
}
*/

// 14)generate_fibonacci(n)

/*
int fabonacci(int n){
if(n==0){return 0;}
else if(n==1){return 1;}
else{
    int k=fabonacci(n-1)+fabonacci(n-2);
    return k;
}
}

void generate_fabonacci(int n){
//printf("0");
for(int i=0;i<=n;i++)
    printf("%d ",fabonacci(i));
}

void main(){
int n;
printf("enter a number : ");
scanf("%d",&n);
generate_fabonacci(n);
}
*/


int fabonacci(int n){
if(n==0){return 0;}
else if(n==1){return 1;}
else{
    int k=fabonacci(n-1)+fabonacci(n-2);
    return k;
}
}

void generate_fabonacci(int n){
//printf("0");
int temp;
int a=0,b=1;
printf("%d %d ",a,b);
for(int i=2;i<=n;i++){
    printf("%d ",a+b);
    temp=b;
    b=a+b;
    a=temp;
}}
/*
void main(){
int n;
printf("enter a number : ");
scanf("%d",&n);
generate_fabonacci(n);
}

*/

//15)function for swapping by call by address

void swap(int* a,int* b){
int temp;
temp=*a;
*a=*b;
*b=temp;
}
/*
void main(){
int x,y;
printf("enter two number : ");
scanf("%d%d",&x,&y);
swap(&x,&y);
printf("%d %d",x,y);
}
*/

// 16) addition,multiplication and etc... using call by address

int* arithmetic(int x,int y,int *add,int *mul,int *sub,int *div){
*add=x+y;
*mul=x*y;
*sub=x-y;
*div=x/y;
}

/*
void main(){
int x,y,add,sub,mul,div;
printf("enter two number : ");
scanf("%d%d",&x,&y);
arithmetic(x,y,&add,&mul,&sub,&div);
printf("add: %d\nsub : %d\nmul : %d\ndiv : %d",add,sub,mul,div);
}
*/

// 17)GCD using recursion

int gcd(int x,int y){
int k;
if(y==0){return 1;}
k=x%y;
if(k==0)
    return y;
gcd(y,k);
}

/*
void main(){
int x,y,add,sub,mul,div;
printf("enter two number : ");
scanf("%d%d",&x,&y);
printf("gcd : %d",gcd(x,y));
}
*/

// 18)find_fact(n)  //recursion
int find_fact(int n){
int fact;
if(n==0){return 1;}
fact=n*find_fact(n-1);
return fact;
}
/*
void main(){
int n;
printf("enter a number : ");
scanf("%d",&n);
printf("factorial of %d is %d",n,find_fact(n));
}
*/

// 19)print the fibonacci series using recursion

void print_fibo(int n,int a,int b){
if(n==0){return;}
printf("%d ",a);
print_fibo(n-1,b,a+b);

}
/*
void main(){
int n;
printf("enter a number : ");
scanf("%d",&n);
print_fibo(n,0,1);
}
*/

// 20)sum of digits using recursion

int recursive_sum_digits(int n){
int sum,r;
if(n==0){return 0;}
r=n%10;
n/=10;
sum=r+recursive_sum_digits(n);
return sum;
}
/*
void main(){
int n;
printf("enter a number : ");
scanf("%d",&n);
printf("sum : %d",recursive_sum_digits(n));
}
*/

// 21)print_pattern(int p,int row)
/*
pattern 1;
*
**
***
****
pattern 2;
1
22
333
4444
pattern 3;
1
12
123
1234
pattern 4;
1
23
456
78910
*/
void print_pattern(int p,int n){
int i,j,k=1;
switch(p){
case 1:
    for(i=0;i<n;i++){
        for(j=0;j<=i;j++){printf("* ");}
    printf("\n");}break;
case 2:
    for(i=0;i<n;i++){
        for(j=0;j<=i;j++){printf("%d ",i+1);}
        printf("\n");}break;
case 3:
    for(i=0;i<n;i++){
        for(j=0;j<=i;j++){printf("%d ",j+1);}
        printf("\n");}break;
case 4:
    for(i=0;i<n;i++){
        for(j=0;j<=i;j++){printf("%d ",k++);}
        printf("\n");}break;
default:
    printf("\nenter correct input");}}

/*
void main(){
int n,p;
printf("enter a number and pattern : ");
scanf("%d%d",&n,&p);
print_pattern(p,n);
}
*/

//22)print_reverse_pattern(int p,int n)
/*
pattern 1;
   *
  **
 ***
****
pattern 2;
   1
  22
 333
4444

pattern 3;
   1
  21
 321
4321

pattern 4;
   1
  23
 456
78910
*/

void print_reverse_pattern(int n,int p){
int i,j,k=1,x;
switch(p){
case 1:
    for(i=0;i<n;i++){
        for(x=0;x<n-i;x++){printf(" ");}
        for(j=0;j<=i;j++){printf("*");}
        printf("\n");}break;
case 2:
    for(i=0;i<n;i++){
        for(x=0;x<n-i;x++){printf(" ");}
        for(j=0;j<=i;j++){printf("%d",i+1);}
        printf("\n");}break;
case 3:
    for(i=0;i<n;i++){
        for(x=0;x<n-i;x++){printf(" ");}
        for(j=i;j>=0;j--){printf("%d",j+1);}
        printf("\n");}break;
case 4:
    for(i=0;i<n;i++){
        for(x=0;x<n-i;x++){printf(" ");}
        for(j=0;j<=i;j++){printf("%d",k++);}
        printf("\n");}break;
default :
    printf("please enter valid choice");}}
/*
void main(){
int n,p;
printf("enter a number and pattern : ");
scanf("%d%d",&n,&p);
print_reverse_pattern(n,p);
}
*/
// 23)print_something_pattern(int n,int p)
/*
pattern 1;
   *
  * *
 * * *
* * * *
pattern 2;
   1
  2 2
 3 3 3
4 4 4 4
pattern 3;
   1
  1 2
 1 2 3
1 2 3 4
pattern 4;
   1
  2 3
 4 5 6
7 8 9 10
*/

void print_something_pattern(int n,int p){
int i,j,k=1,x;
switch(p){
case 1:
    for(i=0;i<n;i++){
        for(x=0;x<n-i;x++){printf(" ");}
    for(j=0;j<=i;j++)
        printf("* ");
    printf("\n");
    }break;
case 2:
    for(i=0;i<n;i++){
        for(x=0;x<n-i;x++){printf(" ");}
    for(j=0;j<=i;j++)
        printf("%d ",i+1);
    printf("\n");
    }break;
case 3:
    for(i=0;i<n;i++){
        for(x=0;x<n-i;x++){printf(" ");}
    for(j=i;j>=0;j--)
        printf("%d ",j+1);
    printf("\n");
    }break;
case 4:
    for(i=0;i<n;i++){
        for(x=0;x<n-i;x++){printf(" ");}
    for(j=0;j<=i;j++)
        printf("%d ",k++);
    printf("\n");
    }break;
default :
    printf("please enter valid choice");
}}
/*
void main(){
int n,p;
printf("enter a number and pattern : ");
scanf("%d%d",&n,&p);
print_something_pattern(n,p);
}
*/

// 24) print_what(int p,int n)
/*
pattern 1;
   *
  ***
 *****
*******

*/

void print_what(int p,int n){
int i,j,k=1,x;
switch(p){
case 1:
    for(i=0;i<n;i++){
        for(x=0;x<n-i;x++){printf(" ");}
        for(j=0;j<=2*i;j++){printf("*");}
    printf("\n");}break;
case 2:
    for(i=0;i<n;i++){
        for(x=0;x<n-i;x++){printf(" ");}
        for(j=0;j<=2*i;j++){printf("%d",i+1);}
        printf("\n");}break;
case 3:
    for(i=0;i<n;i++){
        for(x=0;x<n-i;x++){printf(" ");}
        for(j=0;j<=2*i;j++){printf("%d",j+1);}
        printf("\n");}break;
case 4:
    for(i=0;i<n;i++){
        for(x=0;x<n-i;x++){printf(" ");}
        for(j=0;j<=2*i;j++){printf("%d",k++);}
        printf("\n");}break;
default:
    printf("\nenter correct input");}}
/*
void main(){
int n,p;
printf("enter a number and pattern : ");
scanf("%d%d",&n,&p);
print_what(p,n);
}
*/
