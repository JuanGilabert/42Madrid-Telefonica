/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap_ops.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliao-tr <aliao-tr@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/09 17:11:23 by jgilaber          #+#    #+#             */
/*   Updated: 2026/08/19 12:24:56 by aliao-tr         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/// @brief Function that swap the first and the second element of stack.
/// @param stack The stack to do swap operation.
/// @return Nothing
/// @authors jgilaber & aliao-tr
static void	ft_do_swap_op(t_stack **stack)
{
	t_stack_node	*first;
	t_stack_node	*second;

	if (!stack || !*stack || (*stack)->size < 2)
		return ;
	first = (*stack)->top;
	second = first->next;
	first->next = second->next;
	if (second->next)
		second->next->prev = first;
	second->prev = NULL;
	second->next = first;
	first->prev = second;
	(*stack)->top = second;
}

/// @brief Function that swap the first and the second element of stack_a.
/// @param stack_a The stack to do sa operation from.
/// @param operations_count Int-Array that contains
/// the count of all type of operations.
/// @param show_op Indicates if the operation should be printed.
/// @return Nothing
/// @see ft_do_swap_op & ft_show_push_swap_op
/// @authors jgilaber & aliao-tr
void	sa(t_stack **stack_a, int *operations_count, int show_op)
{
	ft_do_swap_op(stack_a);
	operations_count[OP_SA]++;
	operations_count[OP_TOTAL]++;
	ft_show_push_swap_op("sa", show_op);
}

/// @brief Function that swap the first and the second element of stack_b.
/// @param stack_b The stack to do sb operation from.
/// @param operations_count Int-Array that contains
/// the count of all type of operations.
/// @param show_op Indicates if the operation should be printed.
/// @return Nothing
/// @see ft_do_swap_op & ft_show_push_swap_op
/// @authors jgilaber & aliao-tr
void	sb(t_stack **stack_b, int *operations_count, int show_op)
{
	ft_do_swap_op(stack_b);
	operations_count[OP_SB]++;
	operations_count[OP_TOTAL]++;
	ft_show_push_swap_op("sb", show_op);
}

/// @brief Function that do sa & sb operations
/// @param operations_data Struct that contains the stacks and operations count.
/// @return Nothing
/// @see ft_show_push_swap_op
/// @authors jgilaber & aliao-tr
void	ss(t_push_swap_ops_data *ops_data)
{
	sa(ops_data->a, ops_data->operations_count, HIDE_PUSH_SWAP_OPERATION);
	sb(ops_data->b, ops_data->operations_count, HIDE_PUSH_SWAP_OPERATION);
	ops_data->operations_count[OP_SS]++;
	ops_data->operations_count[OP_SA]--;
	ops_data->operations_count[OP_SB]--;
	ops_data->operations_count[OP_TOTAL]--;
	ft_show_push_swap_op("ss", ops_data->show_op);
}
