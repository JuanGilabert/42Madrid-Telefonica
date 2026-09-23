/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_benchmark.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliao-tr <aliao-tr@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/11 22:43:25 by jgilaber          #+#    #+#             */
/*   Updated: 2026/08/24 14:09:15 by aliao-tr         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/// @brief Function that show the information of the disorder.
/// The operation +0.5f is the correct way to round to two decimal places
/// when converting a float to whole hundredths.
/// @param stack The stack to show the disorder from
/// @return Nothing
/// @authors jgilabert & aliao-tr
static void	ft_show_disorder(t_stack *stack)
{
	long	value;
	long	ent;
	long	dec;

	value = (long)(stack->disorder * 10000.0f + 0.5f);
	ent = value / 100;
	dec = value % 100;
	ft_putstr_fd("[bench] disorder: ", STDERR_FILENO);
	if (ent < 10)
		ft_putchar_fd('0', STDERR_FILENO);
	ft_putnbr_fd(ent, STDERR_FILENO);
	ft_putchar_fd('.', STDERR_FILENO);
	if (dec < 10)
		ft_putchar_fd('0', STDERR_FILENO);
	ft_putnbr_fd(dec, STDERR_FILENO);
	ft_putendl_fd("%", STDERR_FILENO);
}

/// @brief Function that shows the message of the used strategy.
/// @param stack The stack to show the strategy.
/// @return Nothing
/// @authors jgilabert & aliao-tr
static void	ft_show_strategy(t_stack *stack)
{
	int	strategy_used;

	strategy_used = stack->strategy_used;
	ft_putstr_fd("[bench] strategy: ", STDERR_FILENO);
	if (strategy_used == STRAT_SIMPLE)
		ft_putendl_fd(STRAT_SIMPLE_BENCH_MSG, STDERR_FILENO);
	else if (strategy_used == STRAT_MEDIUM)
		ft_putendl_fd(STRAT_MEDIUM_BENCH_MSG, STDERR_FILENO);
	else if (strategy_used == STRAT_COMPLEX)
		ft_putendl_fd(STRAT_COMPLEX_BENCH_MSG, STDERR_FILENO);
	else if (stack->disorder < 0.2)
		ft_putendl_fd(STRAT_ADAPTIVE_SIMPLE_BENCH_MSG, STDERR_FILENO);
	else if (stack->disorder >= 0.5)
		ft_putendl_fd(STRAT_ADAPTIVE_COMPLEX_BENCH_MSG, STDERR_FILENO);
	else
		ft_putendl_fd(STRAT_ADAPTIVE_MEDIUM_BENCH_MSG, STDERR_FILENO);
}

/// @brief Function that show the total operation of each type.
/// @param ops_count Int-Array that contains
/// the count of all type of operations.
/// @return Nothing
/// @authors jgilaber & aliao-tr
static void	ft_show_total_operations_count(int *ops_count)
{
	ft_printf("[bench] total_ops: %d\n", ops_count[OP_TOTAL]);
	ft_printf("[bench] sa: %d", ops_count[OP_SA]);
	ft_printf("  sb: %d  ss: %d", ops_count[OP_SB], ops_count[OP_SS]);
	ft_printf("  pa: %d  pb: %d\n", ops_count[OP_PA], ops_count[OP_PB]);
	ft_printf("[bench] ra: %d  rb: %d", ops_count[OP_RA], ops_count[OP_RB]);
	ft_printf("  rr: %d  rra: %d", ops_count[OP_RR], ops_count[OP_RRA]);
	ft_printf("  rrb: %d  rrr: %d\n", ops_count[OP_RRB], ops_count[OP_RRR]);
}

/// @brief Function that shows on stderr the benchmark.
/// @param stack The stack to show the benchmark
/// @param ops_count Int-Array that contains
/// the count of all type of operations.
/// @return Nothing
/// @authors jgilabert & aliao-tr
void	ft_show_benchmark(t_stack *stack, int *ops_count)
{
	ft_show_disorder(stack);
	ft_show_strategy(stack);
	ft_show_total_operations_count(ops_count);
}

/// @brief check if there is bench as flag
/// @param argc number of arguments
/// @param argv value of argument
/// @return if there is bench or not
int	ft_check_benchmark(int argc, char **argv)
{
	int	i;

	i = 0;
	while (i < argc)
	{
		if (ft_strncmp(argv[i], "--bench", 8) == 0)
			return (1);
		i++;
	}
	return (0);
}
