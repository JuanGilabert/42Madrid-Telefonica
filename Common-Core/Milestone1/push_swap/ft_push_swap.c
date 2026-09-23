/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_push_swap.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliao-tr <aliao-tr@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/09 17:18:13 by jgilaber          #+#    #+#             */
/*   Updated: 2026/08/17 17:38:51 by aliao-tr         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/// @brief Frees the memory allocated for the push_swap algorithm.
/// @param stack_a Pointer to the first stack.
/// @param stack_b Pointer to the second stack.
/// @param operations_count Pointer to an array
/// that will hold the count of operations performed.
/// @return Nothing
/// @see ft_stack_clear
/// @authors jgilaber & aliao-tr
static void	ft_free_push_swap(
	t_stack **stack_a, t_stack **stack_b, int *ops_count)
{
	ft_stack_clear(stack_a);
	ft_stack_clear(stack_b);
	free(ops_count);
}

/// @brief Executes the push_swap algorithm
/// on the provided stacks and counts operations.
/// @param stack_a Pointer to the first stack.
/// @param stack_b Pointer to the second stack.
/// @param operations_count Pointer to an array
/// that will hold the count of operations performed.
/// @return Returns 1 on success, 0 on failure (e.g., mem-alloc-fail).
/// @see ft_do_disorder & ft_exec_strat_dispatch
/// @authors jgilaber & aliao-tr
static int	ft_do_push_swap(t_stack **stack_a, t_stack **stack_b, int *ops_cont)
{
	t_push_swap_ops_data	*operations_data;

	if (ft_check_stack_order(*stack_a))
		return (1);
	operations_data = malloc(sizeof(t_push_swap_ops_data));
	if (!operations_data)
		return (0);
	operations_data->a = stack_a;
	operations_data->b = stack_b;
	operations_data->show_op = SHOW_PUSH_SWAP_OPERATION;
	operations_data->operations_count = ops_cont;
	(*operations_data->a)->disorder = ft_get_disorder(stack_a);
	ft_exec_strat_dispatch(operations_data);
	free(operations_data);
	return (1);
}

/// @brief Creates and initializes the stacks, fills them with numbers,
/// executes the push_swap algorithm(ft_do_push_swap), and handles cleanup.
/// @param flags Array that indicates the strategy
/// @param numbers int-array with the numbers to sort.
/// @param number_size size of the int-array numbers.
/// @return Returns 1 on success, 0 on failure (e.g., mem-alloc-fail).
/// @see ft_fill_stack, ft_do_push_swap, ft_show_benchmark, ft_stack_clear
/// @authors jgilaber & aliao-tr
static void	ft_push_swap(int *flags, int *numbers, int numbers_size)
{
	t_stack		*stack_a;
	t_stack		*stack_b;
	int			*ops_count;
	int			stack_filled_failure;
	int			memory_allocation_failure;

	stack_b = ft_new_stack(-1);
	stack_a = ft_new_stack(ft_get_strategy_flag(flags));
	ops_count = ft_calloc(OP_TOTAL + 1, sizeof(int));
	memory_allocation_failure = !stack_a || !stack_b || !ops_count;
	if (memory_allocation_failure)
	{
		ft_free_push_swap(&stack_a, &stack_b, ops_count);
		return ;
	}
	stack_filled_failure = !ft_fill_stack(&stack_a, numbers, numbers_size);
	if (stack_filled_failure || !ft_do_push_swap(&stack_a, &stack_b, ops_count))
	{
		ft_free_push_swap(&stack_a, &stack_b, ops_count);
		return ;
	}
	if (flags[4] > 0)
		ft_show_benchmark(stack_a, ops_count);
	ft_free_push_swap(&stack_a, &stack_b, ops_count);
}

/// @brief Main function of the program.
/// @param argc Number of arguments.
/// @param argv Array of arguments.
/// @return Exit status of the program.
/// @see ft_exit_program, ft_count_numbers, ft_parse_args, ft_push_swap
/// @authors jgilaber & aliao-tr
int	main(int argc, char **argv)
{
	int		*flags;
	int		*numbers;
	int		numbers_count;

	if (argc < 2)
		return (0);
	numbers_count = ft_count_numbers(argc, argv);
	if (numbers_count == -1)
		ft_exit_program("Error", 1);
	flags = ft_calloc(5, sizeof(int));
	numbers = malloc(sizeof(int) * numbers_count);
	if (!flags || !numbers)
		return (free(flags), free(numbers), 1);
	if (!ft_parse_args(argc, argv, flags, numbers))
	{
		free(flags);
		free(numbers);
		ft_exit_program("Error", 1);
	}
	ft_push_swap(flags, numbers, numbers_count);
	free(numbers);
	free(flags);
	return (0);
}
