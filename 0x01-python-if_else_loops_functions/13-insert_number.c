#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t* ptr;
	listint_t* newnode = malloc(sizeof(listint_t));
	newnode->n = number;
	newnode->next = NULL;

	if(head == NULL || (*head)->n >= newnode->n)
	{
		newnode->next = *head;
		*head =newnode;
		return (newnode);
	}
	else
	{
		ptr = *head;
		while (ptr->next != NULL && ptr->next->n < newnode->n)
			ptr = ptr->next;
	}
	newnode->next = ptr->next;
	ptr->next = newnode;
	
	return (newnode);
}
