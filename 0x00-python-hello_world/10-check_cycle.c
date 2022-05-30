#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: List head.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *now = list, *latter = list;

	while (now != NULL && latter != NULL && latter->next != NULL)
	{
		now = now->next;
		latter = latter->next->next;

		if (now == latter)
			return (1);
	}

	return (0);
}
