#include<stdio.h>
#include<conio.h>
void DFS(int v);
typedef enum boolean{false,true} bool;
int n,a[10][10];
bool visited[10];

	void main()
 {
int i,j,v;
printf("enter the size");
scanf("%d",&n);

printf("enter the matrix ");
for(i=1;i<=n;i++)
 {
for(j=1;j<=n;j++)
{
scanf("%d",&a[i][j]);
}
}

printf("\nthe adjacency matrix is\n");
for(i=1;i<=n;i++)
 {
for(j=1;j<=n;j++)
{
printf("%d",a[i][j]);
}
printf("\n");
}
printf("enter starting node");
scanf("%d",&v);
for(i=1;i<=n;i++)
visited[i]=false;
DFS(v);
getch();
	}


void DFS(int v)
 {
int i,stack[10],top=-1,pop;
top++;
stack[top]=v;

while(top>=0)
 {
pop=stack[top];
top--;

if(visited[pop]==false)
 {
printf("%d",pop);
visited[pop]=true;
}
else
continue;

for(i=n;i>=1;i--)
 {
if(a[pop][i]==1 && visited[i]==false)
{
top++;
stack[top]=i;
	}
}
 }
	}





