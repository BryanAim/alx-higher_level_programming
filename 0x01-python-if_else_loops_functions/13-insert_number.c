#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a new node in position greater than and less than
 * @head: pointer to head of list
 * @number: number to insert
 * Return: number of nodes
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *NewNode;
	listint_t *current;
	listint_t *aux;
	int check = 0;

	current = *head;
	aux = (*head)->next;
	NewNode = malloc(sizeof(listint_t));
	if (!NewNode)
		return (NULL);

	NewNode->n = number;

	if (*head == NULL)
		*head = NewNode;
	else
	{
		while (aux->next != NULL)
		{
			if (NewNode->n >= current->n && NewNode->n <= aux->n)
			{
				current->next = NewNode;
				NewNode->next = aux;
				check = 1;
				break;
			}
			current = current->next;
			aux = aux->next;
		}
		if (check == 0)
		{
			NewNode->next = aux->next;
			aux->next = NewNode;
		}
	}
	return (NewNode);
}
