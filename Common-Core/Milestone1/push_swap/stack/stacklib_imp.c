/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stacklib_imp.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/09 18:45:33 by jgilaber          #+#    #+#             */
/*   Updated: 2026/07/13 21:11:07 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/// @brief Function that creates a new stack of type t_stack.
/// @param strategy The strategy used in push_swap
/// @return New stack with the new data
/// @authors jgilaber & aliao-tr
t_stack	*ft_new_stack(int strategy)
{
	t_stack			*new_stack;

	new_stack = malloc(sizeof(t_stack));
	if (!new_stack)
		return (NULL);
	new_stack->top = NULL;
	new_stack->size = 0;
	new_stack->disorder = 0;
	new_stack->strategy_used = strategy;
	return (new_stack);
}

/// @brief Function that creates a new node of type t_stack_node.
/// @param data The data of the new node.
/// @param index The index of the new node.
/// @return The new stack-node created. 
/// @authors jgilaber & aliao-tr
t_stack_node	*ft_new_stack_node(int data, int index)
{
	t_stack_node	*stack_node;

	stack_node = malloc(sizeof(t_stack_node));
	if (!stack_node)
		return (NULL);
	stack_node->data = data;
	stack_node->index = index;
	stack_node->prev = NULL;
	stack_node->next = NULL;
	return (stack_node);
}

/// @brief Function that returns the last node of a stack.
/// @param stack The stack to get the last node from.
/// @return The last node of the stack.
/// @authors jgilaber & aliao-tr
t_stack_node	*ft_stack_last(t_stack *stack)
{
	t_stack_node	*current;

	if (!stack || !stack->top)
		return (NULL);
	current = stack->top;
	while (current->next)
		current = current->next;
	return (current);
}

/// @brief Function that pushes a new stack-node to the top of a stack.
/// @param stack The stack to push to.
/// @param  new_stack_node The new node to push.
/// @return Nothing
/// @authors jgilaber & aliao-tr
void	ft_stack_push(t_stack **stack, t_stack_node *new_stack_node)
{
	t_stack_node	*tmp_stack_node;

	if (!(*stack)->top)
	{
		(*stack)->top = new_stack_node;
		return ;
	}
	tmp_stack_node = (*stack)->top;
	new_stack_node->next = tmp_stack_node;
	tmp_stack_node->prev = new_stack_node;
	(*stack)->top = new_stack_node;
}

/// @brief Function that removes all nodes from a stack.
/// @param stack The stack to remove the node from.
/// @return Nothing
/// @authors jgilaber & aliao-tr
void	ft_stack_clear(t_stack **stack)
{
	t_stack_node	*tmp_stack_node;

	if (!stack || !*stack || !(*stack)->top)
	{
		free(*stack);
		return ;
	}
	while ((*stack)->top)
	{
		tmp_stack_node = (*stack)->top->next;
		free((*stack)->top);
		(*stack)->top = tmp_stack_node;
	}
	free(*stack);
}
