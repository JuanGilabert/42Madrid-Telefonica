/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strategy_utils.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/16 18:49:24 by jgilaber          #+#    #+#             */
/*   Updated: 2026/07/21 20:24:32 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/// @brief Function that checks if there is a chunk
/// between start and end in medium strategy
/// @param stack The stack to check the chunk-range in.
/// @param start The chunk-range start value.
/// @param end The chunk-range end value.
/// @return An Int indicating if there is a chunk between start and end
/// @see ft_do_medium_strategy_operations
/// @authors jgilaber & aliao-tr
static int	ft_check_chunk_range(
	t_stack *stack, size_t start, size_t end)
{
	t_stack_node	*tmp;

	tmp = stack->top;
	while (tmp)
	{
		if (tmp->index >= start && tmp->index <= end)
			return (1);
		tmp = tmp->next;
	}
	return (0);
}

/// @brief Function that do medium strategy operations
/// @param ops_data Struct that contains the stacks and the operations count.
/// @param chunk_size The chunk size
/// @return Nothing
/// @see ft_do_medium_strategy
/// @authors jgilaber & aliao-tr
void	ft_do_medium_strategy_operations(
	t_push_swap_ops_data *op_data, int chunk_size)
{
	size_t	range_start;
	size_t	range_end;
	size_t	total_size;

	total_size = (*op_data->a)->size;
	range_start = 0;
	while (range_start < total_size)
	{
		range_end = range_start + chunk_size - 1;
		if (range_end >= total_size)
			range_end = total_size - 1;
		while (ft_check_chunk_range(*op_data->a, range_start, range_end))
		{
			if ((*op_data->a)->top->index >= range_start
				&& (*op_data->a)->top->index <= range_end)
			{
				pb(op_data);
				if ((*op_data->b)->top->index < range_start + chunk_size / 2)
					rb(op_data->b, op_data->operations_count, op_data->show_op);
			}
			else
				ra(op_data->a, op_data->operations_count, op_data->show_op);
		}
		range_start += chunk_size;
	}
}

/// @brief Function that reconstructs stack_a from stack_b in medium strategy.
/// @param ops_data Struct that contains the stacks and the operations count.
/// @return Nothing
/// @see ft_get_max_stack_node_pos
/// @authors jgilaber & aliao-tr
void	ft_do_medium_strategy_reconstruction(
	t_push_swap_ops_data *ops_data)
{
	size_t	moves;
	int		max_pos;

	while ((*ops_data->b)->top)
	{
		max_pos = ft_get_max_stack_node_pos(*ops_data->b);
		if (max_pos <= (*ops_data->b)->size / 2)
		{
			moves = max_pos;
			while (moves--)
				rb(ops_data->b, ops_data->operations_count, ops_data->show_op);
		}
		else
		{
			moves = (*ops_data->b)->size - max_pos;
			while (moves--)
				rrb(ops_data->b, ops_data->operations_count, ops_data->show_op);
		}
		pa(ops_data);
	}
}
