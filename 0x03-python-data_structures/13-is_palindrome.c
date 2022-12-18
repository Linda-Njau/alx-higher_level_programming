#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	int count = 0;
	int i = 0;
	int j = 0;
	listint_t *front;
	listint_t *back;

	listint_t *ptr = NULL;
	ptr = head;

	while (ptr != NULL)
	{
		count++;
		ptr = ptr->next;
	}
	front = head;
	back = head;

		for (j = 0; j < i; j++)
		{		
			front = front->next;
		}	
		for (j = 0; j < count - (i + 1); j++)
		{
			back = back->next;
		}	
		if (front->n != back->n)
		{
			return 0;
		}
		else
		{
			i++;
		}		
	}	
	return 1;
}
