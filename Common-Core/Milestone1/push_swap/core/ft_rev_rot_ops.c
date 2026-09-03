/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_rot_ops.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliao-tr <aliao-tr@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/09 17:12:12 by jgilaber          #+#    #+#             */
/*   Updated: 2026/08/19 12:39:36 by aliao-tr         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/// @brief Function that rotate to the bottom of the stack
/// all the elements 1 position, so the last element becomes the first.
/// @param stack The stack to do reverse-rotate operation.
/// @return Nothing
/// @authors jgilaber & aliao-tr
static void	ft_do_reverse_rotate_op(t_stack **stack)
{
	t_stack_node	*first_stack_node_tmp;
	t_stack_node	*last_stack_node_tmp;

	if (!stack || !*stack || (*stack)->size < 2)
		return ;
	first_stack_node_tmp = (*stack)->top;
	last_stack_node_tmp = ft_stack_last(*stack);
	last_stack_node_tmp->prev->next = NULL;
	last_stack_node_tmp->prev = NULL;
	last_stack_node_tmp->next = first_stack_node_tmp;
	first_stack_node_tmp->prev = last_stack_node_tmp;
	(*stack)->top = last_stack_node_tmp;
}

/// @brief Function that rotate to the bottom of the stack_a
/// all the elements 1 position.
/// @param stack_a The stack to do rra operation from.
/// @param operations_count Int-Array that contains
/// the count of all type of operations.
/// @param show_op Indicates if the operation should be printed.
/// @return Nothing
/// @see ft_do_reverse_rotate_op & ft_show_push_swap_op
/// @authors jgilaber & aliao-tr
void	rra(t_stack **stack_a, int *operations_count, int show_op)
{
	ft_do_reverse_rotate_op(stack_a);
	operations_count[OP_RRA]++;
	operations_count[OP_TOTAL]++;
	ft_show_push_swap_op("rra", show_op);
}

/// @brief Function that rotate to the bottom of the stack_b
/// all the elements 1 position.
/// @param stack_b The stack to do rrb operation from.
/// @param operations_count Int-Array that contains
/// the count of all type of operations.
/// @param show_op Indicates if the operation should be printed.
/// @return Nothing
/// @see ft_do_reverse_rotate_op & ft_show_push_swap_op
/// @authors jgilaber & aliao-tr
void	rrb(t_stack **stack_b, int *operations_count, int show_op)
{
	ft_do_reverse_rotate_op(stack_b);
	operations_count[OP_RRB]++;
	operations_count[OP_TOTAL]++;
	ft_show_push_swap_op("rrb", show_op);
}

/// @brief Function that do rra & rrb operations.
/// @param operations_data Struct that contains the stacks and operations count.
/// @return Nothing
/// @see ft_show_push_swap_op
/// @authors jgilaber & aliao-tr
void	rrr(t_push_swap_ops_data *ops_data)
{
	rra(ops_data->a, ops_data->operations_count, HIDE_PUSH_SWAP_OPERATION);
	rrb(ops_data->b, ops_data->operations_count, HIDE_PUSH_SWAP_OPERATION);
	ops_data->operations_count[OP_RRR]++;
	ops_data->operations_count[OP_RRA]--;
	ops_data->operations_count[OP_RRB]--;
	ops_data->operations_count[OP_TOTAL]--;
	ft_show_push_swap_op("rrr", ops_data->show_op);
}
