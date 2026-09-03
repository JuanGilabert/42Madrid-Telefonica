/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strategy_small_utils.c                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/29 12:33:52 by aliao-tr          #+#    #+#             */
/*   Updated: 2026/08/21 16:41:47 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/// @brief Function that search the position of a index.
/// @param ops_data Struct that contains the stacks
/// and the operations count.
/// @param index The index to search the position from
/// @return The position of the given index or -1 otherwise
/// @authors jgilaber & aliao-tr
static int	get_index_pos(t_push_swap_ops_data *ops_data, size_t index)
{
	int				pos;
	t_stack_node	*node;

	node = (*ops_data->a)->top;
	pos = 0;
	while (node)
	{
		if (node->index == index)
			return (pos);
		node = node->next;
		pos++;
	}
	return (-1);
}

/// @brief Function that moves the given index to the top of the stack.
/// @param ops_data Struct that contains the stacks
/// and the operations count.
/// @param index The index to move to the top of the stack
/// @return Nothing
/// @authors jgilaber & aliao-tr
void	move_index_to_top(t_push_swap_ops_data *ops_data, size_t index)
{
	while ((*ops_data->a)->top->index != index)
	{
		if (get_index_pos(ops_data, index)
			<= (*ops_data->a)->size / 2)
			ra(ops_data->a, ops_data->operations_count, ops_data->show_op);
		else
			rra(ops_data->a, ops_data->operations_count, ops_data->show_op);
	}
}
