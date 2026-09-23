/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strategy_small.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliao-tr <aliao-tr@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/28 16:42:25 by aliao-tr          #+#    #+#             */
/*   Updated: 2026/08/20 13:36:44 by aliao-tr         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/// @brief Function that order the stack_a when the stack has 2 elements
/// @param ops_data Struct that contains the stacks and the operations count.
/// @return Nothing
/// @authors jgilaber & aliao-tr
static void	ft_do_sort_two(t_push_swap_ops_data *ops_data)
{
	if ((*ops_data->a)->disorder == 1)
		sa(ops_data->a, ops_data->operations_count, ops_data->show_op);
}

/// @brief Function that order the stack_a when the stack has 3 elements
/// @param ops_data Struct that contains the stacks and the operations count. 
/// @return Nothing
/// @authors jgilaber & aliao-tr
static void	ft_do_sort_three(t_push_swap_ops_data *ops_data)
{
	int	first;
	int	second;
	int	third;

	first = (*ops_data->a)->top->data;
	second = (*ops_data->a)->top->next->data;
	third = (*ops_data->a)->top->next->next->data;
	if (first < second && second < third)
		return ;
	else if (first > second && first < third)
		sa(ops_data->a, ops_data->operations_count, ops_data->show_op);
	else if (first > second && second > third)
	{
		sa(ops_data->a, ops_data->operations_count, ops_data->show_op);
		rra(ops_data->a, ops_data->operations_count, ops_data->show_op);
	}
	else if (first > second && first > third)
		ra(ops_data->a, ops_data->operations_count, ops_data->show_op);
	else if (first < second && first < third)
	{
		sa(ops_data->a, ops_data->operations_count, ops_data->show_op);
		ra(ops_data->a, ops_data->operations_count, ops_data->show_op);
	}
	else
		rra(ops_data->a, ops_data->operations_count, ops_data->show_op);
}

/// @brief Function that order the stack_a when the stack has 4 elements.
/// @param ops_data Struct that contains the stacks and the operations count.
/// @return Nothing
/// @see ft_do_sort_three
/// @authors jgilaber & aliao-tr
static void	ft_do_sort_four(t_push_swap_ops_data *ops_data)
{
	move_index_to_top(ops_data, 0);
	pb(ops_data);
	ft_do_sort_three(ops_data);
	pa(ops_data);
}

/// @brief Function that order the stack_a when the stack has 5 elements.
/// @param ops_data Struct that contains the stacks and the operations count. 
/// @return Nothing
/// @see move_index_to_top
/// @authors jgilaber & aliao-tr
static void	ft_do_sort_five(t_push_swap_ops_data *ops_data)
{
	move_index_to_top(ops_data, 0);
	pb(ops_data);
	move_index_to_top(ops_data, 1);
	pb(ops_data);
	ft_do_sort_three(ops_data);
	pa(ops_data);
	pa(ops_data);
}

/// @brief Dispatcher function that calls the correct small sorting function.
/// @param operations_data Struct that contains the stacks and operations count.
/// @return Nothing
/// @see ft_do_sort_two, ft_do_sort_three, ft_do_sort_four & ft_do_sort_five
/// @authors jgilaber & aliao-tr
void	ft_do_small_sort(t_push_swap_ops_data *operations_data)
{
	int	size;

	size = (*operations_data->a)->size;
	if (size == 2)
		ft_do_sort_two(operations_data);
	else if (size == 3)
		ft_do_sort_three(operations_data);
	else if (size == 4)
		ft_do_sort_four(operations_data);
	else if (size == 5)
		ft_do_sort_five(operations_data);
}
