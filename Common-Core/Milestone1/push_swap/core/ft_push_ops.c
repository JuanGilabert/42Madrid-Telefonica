/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_push_ops.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliao-tr <aliao-tr@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/09 17:11:07 by jgilaber          #+#    #+#             */
/*   Updated: 2026/08/19 12:39:37 by aliao-tr         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/// @brief Function that take the first element of stack_b
/// and push it to the top of stack_a.
/// @param operations_data Struct that contains the stacks and operations count.
/// @return Nothing
/// @see ft_show_push_swap_op
/// @authors jgilaber & aliao-tr
void	pa(t_push_swap_ops_data *operations_data)
{
	t_stack_node	*tmp;

	if (!operations_data || !operations_data->b
		|| !*operations_data->b || !(*operations_data->b)->top)
		return ;
	tmp = (*operations_data->b)->top;
	(*operations_data->b)->top = tmp->next;
	if ((*operations_data->b)->top)
		(*operations_data->b)->top->prev = NULL;
	tmp->prev = NULL;
	tmp->next = (*operations_data->a)->top;
	if ((*operations_data->a)->top)
		(*operations_data->a)->top->prev = tmp;
	(*operations_data->a)->top = tmp;
	(*operations_data->a)->size++;
	(*operations_data->b)->size--;
	operations_data->operations_count[OP_PA]++;
	operations_data->operations_count[OP_TOTAL]++;
	ft_show_push_swap_op("pa", operations_data->show_op);
}

/// @brief Function that take the first element of stack_a
/// and push it to the top of stack_b.
/// @param operations_data Struct that contains the stacks and operations count.
/// @return Nothing
/// @see ft_show_push_swap_op
/// @authors jgilaber & aliao-tr
void	pb(t_push_swap_ops_data *operations_data)
{
	t_stack_node	*tmp;

	if (!operations_data || !operations_data->a
		|| !*operations_data->a || !(*operations_data->a)->top)
		return ;
	tmp = (*operations_data->a)->top;
	(*operations_data->a)->top = tmp->next;
	if ((*operations_data->a)->top)
		(*operations_data->a)->top->prev = NULL;
	tmp->next = (*operations_data->b)->top;
	tmp->prev = NULL;
	if ((*operations_data->b)->top)
		(*operations_data->b)->top->prev = tmp;
	(*operations_data->b)->top = tmp;
	(*operations_data->a)->size--;
	(*operations_data->b)->size++;
	operations_data->operations_count[OP_PB]++;
	operations_data->operations_count[OP_TOTAL]++;
	ft_show_push_swap_op("pb", operations_data->show_op);
}

/// @brief Function that show the recived operation in base show_op param
/// @param push_swap_operation The name of the push_swap operation
/// @param show_op Indicates if the operation should be printed.
/// @return Nothing
/// @see ft_putendl_fd
/// @authors jgilaber & aliao-tr
void	ft_show_push_swap_op(char *push_swap_operation, int show_op)
{
	if (show_op)
		ft_putendl_fd(push_swap_operation, STDOUT_FILENO);
}
