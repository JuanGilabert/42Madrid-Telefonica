/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rotate_ops.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliao-tr <aliao-tr@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/09 17:11:47 by jgilaber          #+#    #+#             */
/*   Updated: 2026/08/19 12:26:17 by aliao-tr         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/// @brief Function that rotate to the top of the stack
/// all the elements 1 position, so the first element becomes the last.
/// @param stack The stack to do rotate operation.
/// @return Nothing
/// @authors jgilaber & aliao-tr
static void	ft_do_rotate_op(t_stack **stack)
{
	t_stack_node	*first;
	t_stack_node	*last;

	if (!stack || !*stack || (*stack)->size < 2)
		return ;
	first = (*stack)->top;
	last = ft_stack_last(*stack);
	(*stack)->top = first->next;
	(*stack)->top->prev = NULL;
	last->next = first;
	first->prev = last;
	first->next = NULL;
}

/// @brief Function that rotate to the top of the stack_a
/// all the elements 1 position.
/// @param stack_a The stack to do ra operation from.
/// @param operations_count Int-Array that contains
/// the count of all type of operations.
/// @param show_op Indicates if the operation should be printed.
/// @return Nothing
/// @see ft_do_rotate_op & ft_show_push_swap_op
/// @authors jgilaber & aliao-tr
void	ra(t_stack **stack_a, int *operations_count, int show_op)
{
	ft_do_rotate_op(stack_a);
	operations_count[OP_RA]++;
	operations_count[OP_TOTAL]++;
	ft_show_push_swap_op("ra", show_op);
}

/// @brief Function that rotate to the top of the stack_b
/// all the elements 1 position.
/// @param stack_b The stack to do rb operation from.
/// @param operations_count Int-Array that contains
/// the count of all type of operations.
/// @param show_op Indicates if the operation should be printed.
/// @return Nothing
/// @see ft_do_rotate_op & ft_show_push_swap_op
/// @authors jgilaber & aliao-tr
void	rb(t_stack **stack_b, int *operations_count, int show_op)
{
	ft_do_rotate_op(stack_b);
	operations_count[OP_RB]++;
	operations_count[OP_TOTAL]++;
	ft_show_push_swap_op("rb", show_op);
}

/// @brief Function that do ra & rb operations.
/// @param operations_data Struct that contains the stacks and operations count.
/// @return Nothing
/// @see ft_show_push_swap_op
/// @authors jgilaber & aliao-tr
void	rr(t_push_swap_ops_data *ops_data)
{
	ra(ops_data->a, ops_data->operations_count, HIDE_PUSH_SWAP_OPERATION);
	rb(ops_data->b, ops_data->operations_count, HIDE_PUSH_SWAP_OPERATION);
	ops_data->operations_count[OP_RR]++;
	ops_data->operations_count[OP_RA]--;
	ops_data->operations_count[OP_RB]--;
	ops_data->operations_count[OP_TOTAL]--;
	ft_show_push_swap_op("rr", ops_data->show_op);
}
