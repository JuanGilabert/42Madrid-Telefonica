/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strategy.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliao-tr <aliao-tr@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/16 18:49:24 by jgilaber          #+#    #+#             */
/*   Updated: 2026/08/17 17:10:48 by aliao-tr         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/// @brief Simple sorting method with O(n2) complexity.
/// @param operations_data Struct that contains the stacks
/// and the operations count.
/// @return Nothing
/// @see ft_get_min_stack_node_index & ft_get_min_stack_node_pos
/// @authors jgilaber & aliao-tr
static void	ft_do_simple_strategy(t_push_swap_ops_data *ops_data)
{
	size_t	min;
	int		pos;

	while ((**ops_data->a).top)
	{
		min = ft_get_min_stack_node_index(ops_data->a);
		pos = ft_get_min_stack_node_pos(ops_data->a, min);
		if (pos <= ((*ops_data->a)->size / 2))
			while ((*ops_data->a)->top && (*ops_data->a)->top->index != min)
				ra(ops_data->a, ops_data->operations_count, ops_data->show_op);
		else
			while ((*ops_data->a)->top && (*ops_data->a)->top->index != min)
				rra(ops_data->a, ops_data->operations_count, ops_data->show_op);
		pb(ops_data);
	}
	while ((*ops_data->b)->top)
		pa(ops_data);
}

/// @brief Medium Strategy Sorting Method with O(n√n) complexity.
/// @param operations_data Struct that contains the stacks
/// and the operations count.
/// @return Nothing
/// @see ft_do_medium_strategy_operations & ft_do_medium_strategy_reconstruction
/// @authors jgilaber & aliao-tr
static void	ft_do_medium_strategy(t_push_swap_ops_data *operations_data)
{
	int	chunk_size;

	if ((*operations_data->a)->size <= 100)
		chunk_size = 15;
	else
		chunk_size = 30;
	ft_do_medium_strategy_operations(operations_data, chunk_size);
	ft_do_medium_strategy_reconstruction(operations_data);
}

/// @brief Complex Strategy Sorting Method with O(n log n) complexity.
/// @param operations_data Struct that contains the stacks
/// and the operations count.
/// @return Nothing
/// @authors jgilaber & aliao-tr
static void	ft_do_complex_strategy(t_push_swap_ops_data *ops_data)
{
	size_t	bit;
	size_t	max_bits;
	size_t	stack_size;
	size_t	processed_nodes_count;

	stack_size = (*ops_data->a)->size;
	max_bits = 0;
	while (((stack_size - 1) >> max_bits) != 0)
		max_bits++;
	bit = 0;
	while (bit < max_bits)
	{
		processed_nodes_count = 0;
		while (processed_nodes_count < stack_size)
		{
			if ((((*ops_data->a)->top->index >> bit) & 1) == 0)
				pb(ops_data);
			else
				ra(ops_data->a, ops_data->operations_count, ops_data->show_op);
			processed_nodes_count++;
		}
		while ((*ops_data->b)->top)
			pa(ops_data);
		bit++;
	}
}

/// @brief Adaptative Strategy Sorting Method with O(n * k) complexity.
/// @param operations_data Struct that contains the stacks
/// and the operations count.
/// @return Nothing
/// @note Is the default strategy if no other strategy is selected.
/// @authors jgilaber & aliao-tr
static void	ft_do_adaptative_strategy(t_push_swap_ops_data *operations_data)
{
	if ((*operations_data->a)->disorder >= 0.5)
		ft_do_complex_strategy(operations_data);
	else if ((*operations_data->a)->disorder < 0.2)
		ft_do_simple_strategy(operations_data);
	else
		ft_do_medium_strategy(operations_data);
}

/// @brief Function that dispatch the stratergy tu use.
/// @param operations_data Struct that contains the stacks
/// and the operations count.
/// @return Nothing
/// @pre operations_data != NULL
/// @see ft_do_small_sort, ft_do_simple_strategy,
/// ft_do_medium_strategy, ft_do_complex_strategy & ft_do_adaptative_strategy
/// @authors jgilaber & aliao-tr
void	ft_exec_strat_dispatch(t_push_swap_ops_data *operations_data)
{
	t_strategy_type	strategy;

	strategy = (*operations_data->a)->strategy_used;
	if ((*operations_data->a)->size < 6)
		ft_do_small_sort(operations_data);
	else if (strategy == STRAT_SIMPLE)
		ft_do_simple_strategy(operations_data);
	else if (strategy == STRAT_MEDIUM)
		ft_do_medium_strategy(operations_data);
	else if (strategy == STRAT_COMPLEX)
		ft_do_complex_strategy(operations_data);
	else if (strategy == STRAT_ADAPTIVE)
		ft_do_adaptative_strategy(operations_data);
}
