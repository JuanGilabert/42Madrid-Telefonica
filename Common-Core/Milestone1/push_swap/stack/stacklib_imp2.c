/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stacklib_imp2.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/09 18:45:33 by jgilaber          #+#    #+#             */
/*   Updated: 2026/07/13 21:11:07 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/// @brief Function that calculates the index of the received value max_value.
/// It is used when creating the stack to assign the index of each node.
/// @param numbers array of int-numbers
/// @param max_value The value for which to calculate the index.
/// @return The index of the received value.
/// @authors jgilaber & aliao-tr
static int	ft_get_stack_node_index(int *nmbrs, size_t nmbrs_size, int max_val)
{
	size_t	numbers_index;
	size_t	stack_node_min_count_index;

	numbers_index = 0;
	stack_node_min_count_index = 0;
	while (numbers_index < nmbrs_size)
	{
		if (nmbrs[numbers_index] < max_val)
			stack_node_min_count_index++;
		numbers_index++;
	}
	return (stack_node_min_count_index);
}

/// @brief Function that fills the provided stack with nodes
/// created from the given array of numbers.
/// @param stack Pointer to the first stack.
/// @param nmbrs Array of numbers to fill the stack with.
/// @param nmbrs_size Size of the numbers array.
/// @return Returns 1 on success, 0 on failure (e.g., mem-alloc-fail).
/// @see ft_calc_stack_node_index & ft_new_stack_node
/// @authors jgilaber & aliao-tr
int	ft_fill_stack(t_stack **stack, int *nmbrs, size_t nmbrs_size)
{
	int				index;
	size_t			stack_size;
	t_stack_node	*temp_stack;

	stack_size = nmbrs_size;
	while (stack_size > 0)
	{
		index = ft_get_stack_node_index(
				nmbrs, nmbrs_size, nmbrs[stack_size - 1]);
		temp_stack = ft_new_stack_node(nmbrs[stack_size - 1], index);
		if (!temp_stack)
			return (0);
		ft_stack_push(stack, temp_stack);
		stack_size--;
	}
	(*stack)->size = nmbrs_size;
	return (1);
}

/// @brief Finds the lowest number on the stack
/// @param stack The stack to get the lowest number from.
/// @return The lowest number on the stack
/// @authors jgilaber & aliao-tr
size_t	ft_get_min_stack_node_index(t_stack **stack)
{
	size_t			min_stack_node_index;
	t_stack_node	*temp_stack;

	if (!stack || !*stack || !(*stack)->top)
		return (-1);
	temp_stack = (*stack)->top;
	min_stack_node_index = temp_stack->index;
	while (temp_stack)
	{
		if (temp_stack->index < min_stack_node_index)
			min_stack_node_index = temp_stack->index;
		temp_stack = temp_stack->next;
	}
	return (min_stack_node_index);
}

/// @brief Finds the position on the stack of the lowest number
/// @param stack The stack to get the minimum node position from.
/// @param min_stack_node_index Lowest index on the stack
/// @return Position of the min_stack_node_index number on the stack
/// @authors jgilaber & aliao-tr
int	ft_get_min_stack_node_pos(t_stack **stack, size_t min_stack_node_index)
{
	t_stack_node	*temp_stack;
	int				pos;

	if (!stack || !(*stack)->top)
		return (-1);
	temp_stack = (*stack)->top;
	pos = 0;
	while (temp_stack)
	{
		if (temp_stack->index == min_stack_node_index)
			return (pos);
		pos++;
		temp_stack = temp_stack->next;
	}
	return (-1);
}

/// @brief Function that returns the position of the maximum node in a stack.
/// @param stack The stack to get the maximum node position from.
/// @return The position of the maximum node on the stack.
/// @authors jgilaber & aliao-tr
size_t	ft_get_max_stack_node_pos(t_stack *stack)
{
	size_t			pos;
	size_t			max;
	size_t			max_pos;
	t_stack_node	*tmp;

	tmp = stack->top;
	pos = 0;
	max = tmp->index;
	max_pos = 0;
	while (tmp)
	{
		if (tmp->index > max)
		{
			max = tmp->index;
			max_pos = pos;
		}
		tmp = tmp->next;
		pos++;
	}
	return (max_pos);
}
