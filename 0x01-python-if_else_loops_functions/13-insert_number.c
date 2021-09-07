#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to a pointer to first node of the list
 * @number: number to add
 * Return: address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *temp = *head;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	while (temp->next != NULL)
	{
		if ((new_node->n >= temp->n) && (new_node->n <= temp->next->n))
		{
			new_node->next = temp->next;
			temp->next = new_node;
			return (new_node);
		}
			temp = temp->next;
	}
	return (new_node);
}
