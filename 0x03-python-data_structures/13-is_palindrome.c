#include "lists.h"
#include <stdio.h>
#include <stdlib.h> 
#include <stdbool.h> 

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: pointer to head of linked list
* empty list is considered a palindrome
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
    listint_t **left = head;
    listint_t **right = head;
   /* stop recursion when right becomes NULL */
   if (right == NULL) 
      return true; 
  
   /* If sub-list is not palindrome then no need to 
       check for current left and right, return false */
   bool isp = is_palindrome(head); 
   if (isp == false) 
      return false; 
  
   /* Check values at current left and right */
   bool isp1 = ((*right)->n == (*left)->n); 
  
   /* Move left to next node */
   *left = (*left)->next; 
  
   return isp1; 
} 

/**
* A wrapper over isPalindromeUtil()
* bool isPalindrome(listint_t *head)
* { 
*   is_palindrome(**head);
*   return (0);
* }
*/
  
/* Push a node to linked list. Note that this function 
  changes the head */
void push(listint_t **head_ref, char new_data) 
{ 
    /* allocate node */
    listint_t* new_node = (listint_t*) malloc(sizeof(listint_t)); 
  
    /* put in the data  */
    new_node->n  = new_data; 
  
    /* link the old list off the new node */
    new_node->next = (*head_ref);
  
    /* move the head to pochar to the new node */
    (*head_ref)    = new_node; 
} 
  
