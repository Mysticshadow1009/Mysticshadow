#include<stdio.h>

int* get_array(int arr[],int n){
printf("\nenter the array : \n");
for(int i=0;i<n;i++)
scanf("%d",&arr[i]);
return *arr;}

// 1)sum of n numbers

int sum_numbers(int arr[],int n){
int i,sum=0;
for(i=0;i<n;i++)
sum+=arr[i];
return sum;
}

/*
void main(){
int n;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n],i;
printf("\nenter the array : \n");
for(i=0;i<n;i++)
scanf("%d",&arr[i]);
printf("\nsum of elements in the array : %d ",sum_numbers(arr,n));
}
*/

//2) print array

void print_array(int arr[],int n){
int i;
printf("\n");
for(i=0;i<n;i++)
printf("%d ",arr[i]);
return;
}
/*
void main(){
int n;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n],i;
printf("\nenter the array : \n");
for(i=0;i<n;i++)
scanf("%d",&arr[i]);
print_array(arr,n);
}
*/

//3)reverse printing the array

void print_reverse(int arr[],int n){
int i;
printf("\n");
for(i=n-1;i>=0;i--)
printf("%d ",arr[i]);
return;
}

/*
void main(){
int n;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n],i;
printf("\nenter the array : \n");
for(i=0;i<n;i++)
scanf("%d",&arr[i]);
print_reverse(arr,n);
}
*/

//4)reverse the content of the array

int* reverse(int arr[],int n){ //use int* return pointer variable
int i,t=n,temp;
for(i=0;i<n/2;i++){
temp=arr[i];
arr[i]=arr[t-1];
arr[t-1]=temp;
t--;
}
return arr;
}

/*
void main(){
int n;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n],i;
printf("\nenter the array : \n");
for(i=0;i<n;i++)
scanf("%d",&arr[i]);
reverse(arr,n);
print_array(arr,n);
}

*/

//5)copy a array to another

int* copy_array(int arr[],int a[],int n){
int i;
for(i=0;i<n;i++)
a[i]=arr[i];
return a;
}

/*
void main(){
int n;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n],i,arr1[n];
printf("\nenter the array : \n");
for(i=0;i<n;i++)
scanf("%d",&arr[i]);
copy_array(arr,arr1,n);
print_array(arr1,n);
}
*/

//6)copy a reverse of array

int* copy_reverse(int arr[],int a[],int n){
copy_array(arr,a,n);
reverse(a,n);
return a;
}

/*
void main(){
int n;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n],i,arr1[n];
printf("\nenter the array : \n");
for(i=0;i<n;i++)
scanf("%d",&arr[i]);
copy_reverse(arr,arr1,n);
print_array(arr1,n);
}
*/

//7)search a element in array

int search_element(int arr[],int n,int low,int high,int search){
int mid=(high+low)/2;
if(low>high)
return 0;
if(arr[mid]==search)
return mid;
else if(arr[mid]>search)
high=mid-1;
else
low=mid+1;
search_element(arr,n,low,high,search);
}

/*
void main(){
int n,search,high,low;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n];
printf("\nenter the array : \n");
get_array(arr,n);
sort_ascend(arr,n);
printf("\nenter a search element : ");
scanf("%d",&search);
printf("\nenter range : ");
scanf("%d%d",&low,&high);
int t=search_element(arr,n,low,high,search);
if(t){printf("found");}
else
printf("not found");
}
*/

// 8)count number of occurences of a given number

int count_occurences(int search,int arr[],int n){
int i,check=0;
for(i=0;i<n;i++)
    if(arr[i]==search){check++;}
return check;
}
/*
void main(){
int n,search,high,low;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n];
get_array(arr,n);
sort_ascend(arr,n);
printf("\nenter a search element : ");
scanf("%d",&search);
int t=count_occurences(search,arr,n);
if(t==0){printf("nothing found");}
else{printf("found : %d times",t);}
}
*/

// 9) find minimum number in an array

int minimum(int arr[],int n){
int i,min=arr[0];
for(i=1;i<n;i++){if(arr[i]<min){min=arr[i];}}
return min;}
/*
void main(){
int n;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n];
get_array(arr,n);
printf("minimum : %d",minimum(arr,n));
}
*/

// 10) find minimum number in an array

int maximum(int arr[],int n){
int i,max=arr[0];
for(i=1;i<n;i++){if(arr[i]>max){max=arr[i];}}
return max;}
/*
void main(){
int n;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n];
get_array(arr,n);
printf("maximum : %d",maximum(arr,n));
}
*/

//11)sorting in ascending order

int* sort_ascend(int a[],int n){
int i,j,temp;
for(j=0;j<n-1;j++)
for(i=0;i<n-1;i++){
if(a[i]>a[i+1]){
temp=a[i];
a[i]=a[i+1];
a[i+1]=temp;
}}
return *a;
}
/*
void main(){
int n;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n];
get_array(arr,n);
sort_ascend(arr,n);
print_array(arr,n);
}*/

// 12)sort in decreasing order

int* sort_decend(int a[],int n){
int i,j,temp;
for(j=0;j<n-1;j++)
for(i=0;i<n-1;i++){
if(a[i]<a[i+1]){
temp=a[i];
a[i]=a[i+1];
a[i+1]=temp;
}}
return *a;}
/*
void main(){
int n;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n];
get_array(arr,n);
sort_decend(arr,n);
print_array(arr,n);
}
*/

// 13)insert an element in an particular index

int* insert_element(int arr[],int n,int index,int element){
arr[index]=element;
for(int i=index+1;i<n;i++){arr[i]=arr[i+1];}
return *arr;}
/*
void main(){
int n,ele,ind;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n];
get_array(arr,n);
printf("enter element and its index : ");
scanf("%d%d",&ele,&ind);
insert_element(arr,n,ind,ele);
print_array(arr,n);
}
*/

// 14)delete an element using index
int* delete_element_index(int arr[],int n,int index){
for(int i=index;i<n-1;i++){arr[i]=arr[i+1];}
return *arr;}
/*
void main(){
int n,ind;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n];
get_array(arr,n);
printf("enter element's index : ");
scanf("%d",&ind);
delete_element_index(arr,n,ind);
print_array(arr,n-1);
}
*/

// 15)delete an element
int* delete_element(int arr[],int n,int element){
int i;
for(i=0;i<n;i++){if(arr[i]==element){break;}}
for(int j=i;j<n-1;j++){arr[j]=arr[j+1];}
return *arr;}

/*
void main(){
int n,ele;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n];
get_array(arr,n);
printf("enter element : ");
scanf("%d",&ele);
delete_element(arr,n,ele);
print_array(arr,n-1);
}
*/

// 16)left right split in array

/*WRONG
int* split(int arr[],int* left[],int* right[],int n,int x){
int k=0,l=0;
for(int i=0;i<n;i++){
if(arr[i]<x){
    *left[k++]=x;}
else if(arr[i]>x){
    *right[l++]=x;}
// WRONG
}}
void main(){
int n,x;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n],left[n],right[n];
get_array(arr,n);
printf("enter x : ");
scanf("%d",&x);
split(arr,&left,&right,n,x);
print_array(left,n);
print_array(right,n);
}
*/
//CORRECT
/*
void main(){
int n,x;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n];
get_array(arr,n);
printf("enter x : ");
scanf("%d",&x);
int i,count_left=0,count_right=0;
for(i=0;i<n;i++){
    if(arr[i]<x){count_left++;}
    else if(arr[i]>x){count_right++;}
}
int left[count_left],right[count_right],r=0,l=0;
for(i=0;i<n;i++){
    if(arr[i]<x){left[l++]=arr[i];}
    else if(arr[i]>x){right[r++]=arr[i];}
}
printf("\nleft : ");
print_array(left,count_left);
printf("\nright : ");
print_array(right,count_right);
}
*/

// 17)remove duplicates
/*
int* remove_duplicates(int arr[],int *n){
int k=*n;
printf("%d",k);
for(int i=0;i<k;i++){
    int check=count_occurences(arr[i],arr,k);
    printf("i : %d,%d ",i,check);
    while(check>1){
        printf("%d",k);
        for(int j=i;j<k-2;j++){arr[i]=arr[i+1];}
        k--;
        check=count_occurences(arr[i],arr,k);
    }
}
*n=k;
return *arr;
}
*/

int* remove_dup(int arr[],int *n){
//first sort array
int temp;
for(int j=0;j<*n-1;j++){
for(int i=0;i<*n-1;i++){
    if(arr[i]>arr[i+1]){
        temp=arr[i];
        arr[i]=arr[i+1];
        arr[i+1]=temp;
    }
}}

int j=0;
int i;
for(i=0;i<*n-1;i++){
    if(arr[i]!=arr[i+1]){
            arr[j++]=arr[i];
    }
}

arr[j++]=arr[i];
*n=j;
return *arr;
}
/*
void main(){
int n;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n];
get_array(arr,n);
remove_dup(arr,&n);
print_array(arr,n);
}
*/

// 18)C Program to replace all the occurrences of given element with another input value using function.

int* replace(int arr[],int n,int old_ele,int new_ele){
for(int i=0;i<n;i++){
    if(arr[i]==old_ele){arr[i]=new_ele;}
}
return *arr;
}

/*
void main(){
int n,old_ele,new_ele;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n];
get_array(arr,n);
printf("enter old element : ");
scanf("%d",&old_ele);
printf("enter new element : ");
scanf("%d",&new_ele);
replace(arr,n,old_ele,new_ele);
print_array(arr,n);
}
*/

// 19)C Program to insert an element into an array at the given position (index) using function.

int* insert(int arr[],int *n,int element,int index){
(*n)+=1;
printf("n : %d",*n);
int temp;
/*
for(int i=index;i<*n+1;i++){
       // printf("%d ",i);
    arr[i+1]=arr[i];
}*/

for(int i=*n-1;i>index;i--){
arr[i]=arr[i-1];
}

arr[index]=element;
return *arr;
}
/*
void main(){
int n,index,element;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n+1];
get_array(arr,n);
printf("enter element,index : ");
scanf("%d%d",&element,&index);
insert(arr,&n,element,index);
print_array(arr,n);
}
*/

// 21) C Program to merge the content of two input sorted array into another array so that the resultant
//array should be in order.

int* merge_array(int rel[],int arr1[],int arr2[],int n1,int n2,int n3){
int i;
for(i=0;i<n1;i++){rel[i]=arr1[i];}
for(int j=0;j<n2;j++){
    rel[i]=arr2[j];
    i++;
}
return *rel;
}
/*
void main(){
int n1,n2,n3;
printf("enter number of inputs in array 1: ");
scanf("%d",&n1);
int arr1[n1];
get_array(arr1,n1);
printf("enter number of inputs in array 2: ");
scanf("%d",&n2);
int arr2[n2];
get_array(arr2,n2);
int arr3[n1+n2];
merge_array(arr3,arr1,arr2,n1,n2,n1+n2);
print_array(arr3,n1+n2);
}
*/

// 20)C Program to delete all the occurrences of given element from the array using function.

int* destroy_element(int arr[],int *n,int element){
int index=0,i;
int k= *n;
for(i=0;i<k;i++){
    if(arr[i]!=element){
        arr[index++]=arr[i];
    }
}
*n=index;
return *arr;
}
/*
void main(){
int n,element;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n];
get_array(arr,n);
printf("enter element to delete : ");
scanf("%d",&element);
destroy_element(arr,&n,element);
print_array(arr,n);
}
*/

// 22)C Program to search an element from an array using recursive function.
//unwanted dumb question!!

int recursive_search(int arr[],int n,int search_element){
if(n<=0){
    return -1;
}
if(arr[n-1]==search_element){
    return n-1;
}
recursive_search(arr,n-1,search_element);
}
/*
void main(){
int n,search_element,check;
printf("enter number of inputs : ");
scanf("%d",&n);
int arr[n];
get_array(arr,n);
printf("enter element to seach : ");
scanf("%d",&search_element);
check=recursive_search(arr,n,search_element);
if(check==-1){printf("not found");}
else{printf("found at : %d",check);}
}
*/

// 23)C Program to perform addition of two matrices with dimension m x n.
#define MAX_ROWS 10
#define MAX_COLS 10
int** get_matrix(int arr[MAX_ROWS][MAX_COLS],int m,int n){
for(int i=0;i<m;i++)
    for(int j=0;j<n;j++){
        printf("\nenter [%d][%d] position of matrix : ",i,j);
        scanf("%d",&arr[i][j]);
    }
return arr;
}

void print_matrix(int arr[MAX_ROWS][MAX_COLS],int m,int n){
for(int i=0;i<m;i++){
    for(int j=0;j<n;j++){printf("%d ",arr[i][j]);}
    printf("\n");
}
}

int** addition_matrix(int rel[MAX_ROWS][MAX_COLS],int arr1[MAX_ROWS][MAX_COLS],int arr2[MAX_ROWS][MAX_COLS],int m,int n){
for(int i=0;i<m;i++)
    for(int j=0;j<n;j++){rel[i][j]=arr1[i][j]+arr2[i][j];}
return **rel;
}

/*
void main(){
int m,n;
printf("enter row and columns of matrix : ");
scanf("%d%d",&m,&n);
int arr1[m][n],arr2[m][n],add[m][n];
get_matrix(arr1,m,n);
get_matrix(arr2,m,n);
addition_matrix(add,arr1,arr2,m,n);
print_matrix(add,m,n);
}
*/

// 24)C Program to search an element from a matrix. If found, display the row index and column index.
void display_position(int arr[MAX_ROWS][MAX_COLS],int m,int n,int element){
int check=0;
for(int i=0;i<m;i++){
    for(int j=0;j<n;j++){
        if(arr[i][j]==element){
            check++;
            printf("row : %d , column : %d\n",i,j);
        }
    }
}
if(check==0){printf("not found");}
}
/*
void main(){
int m,n;
printf("enter row and columns of matrix : ");
scanf("%d%d",&m,&n);
int element,arr[m][n];
get_matrix(arr,m,n);
printf("enter element to search : ");
scanf("%d",&element);
display_position(arr,m,n,element);
}
*/

//C Program to find the sum of the elements of a matrix.
int sum_of_elements_matrix(int arr[MAX_ROWS][MAX_COLS],int m,int n){
int sum=0;
for(int i=0;i<m;i++)
    for(int j=0;j<n;j++){sum+=arr[i][j];}
return sum;
}
/*
void main(){
int m,n;
printf("enter row and columns of matrix : ");
scanf("%d%d",&m,&n);
int element,arr[m][n];
get_matrix(arr,m,n);
printf("sum : %d",sum_of_elements_matrix(arr,m,n));
}
*/
