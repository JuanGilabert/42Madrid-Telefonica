/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_push_swap_utils.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/10 20:09:00 by aliao-tr          #+#    #+#             */
/*   Updated: 2026/07/31 16:24:35 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/// @brief Function that displays an error message and exits the program.
/// @param exit_message The error message to be displayed.
/// @param exit_code The exit code to be returned.
/// @return Nothing
/// @see ft_putendl_fd
/// @authors jgilaber & aliao-tr
void	ft_exit_program(char *exit_message, int exit_code)
{
	ft_putendl_fd(exit_message, STDERR_FILENO);
	exit(exit_code);
}

/// @brief Function that compute the disorder of the recived stack.
/// @param stack The stack to compute the disorder from.
/// @return double The disorder computed
/// @authors jgilaber & aliao-tr
double	ft_get_disorder(t_stack **stack)
{
	double			mistakes;
	int				total_pairs;
	t_stack_node	*tmp_stack_node;
	t_stack_node	*tmp2_stack_node;

	mistakes = 0;
	total_pairs = 0;
	tmp_stack_node = (*stack)->top;
	if (!stack || !*stack || (*stack)->size < 2)
		return (0.0);
	while (tmp_stack_node->next)
	{
		tmp2_stack_node = tmp_stack_node->next;
		while (tmp2_stack_node)
		{
			if (tmp_stack_node->data > tmp2_stack_node->data)
				mistakes += 1;
			total_pairs += 1;
			tmp2_stack_node = tmp2_stack_node->next;
		}
		tmp_stack_node = tmp_stack_node->next;
	}
	return (mistakes / total_pairs);
}

/// @brief Checks if the recived stack is sorted.
/// An empty stack is considered sorted.
/// @param stack Pointer to the stack to check.
/// @return 1 if the stack is sorted, 0 otherwise.
/// @authors jgilaber & aliao-tr
int	ft_check_stack_order(t_stack *stack)
{
	t_stack_node	*current;

	if (!stack || !stack->top)
		return (1);
	current = stack->top;
	while (current->next)
	{
		if (current->data > current->next->data)
			return (0);
		current = current->next;
	}
	return (1);
}
