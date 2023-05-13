#include <stdlib.h>
#include <stdio.h>	
typedef struct Node
{
    int data;
    struct Node* next;
}Node;

Node* insert(Node *head,int data)
{
    //Complete this function
    Node * nod=
     nod=(Node *)malloc(sizeof(Node));
     nod->data=data;
     if(head==NULL) {head =nod; return head;}
     Node *p;
     p=head;
     while(p->next!=NULL)
         p=p->next;
     p->next=nod;
     return head;
}

void display(Node *head)
{
	Node *start=head;
	while(start)
	{
		printf("%d ",start->data);
		start=start->next;
	}
}
int main()
{
	int T,data;
    scanf("%d",&T);
    Node *head=NULL;	
    while(T-->0){
        scanf("%d",&data);
        head=insert(head,data);
    }
  display(head);
		
}

