/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   strategy.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/06 19:30:56 by jgilaber          #+#    #+#             */
/*   Updated: 2026/07/13 21:27:27 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef STRATEGY_H
# define STRATEGY_H

typedef struct s_stack				t_stack;
typedef struct s_push_swap_ops_data	t_push_swap_ops_data;

# define STRAT_SIMPLE_BENCH_MSG    "Simple / O(n2)"
# define STRAT_MEDIUM_BENCH_MSG    "Medium / O(n√n)"
# define STRAT_COMPLEX_BENCH_MSG   "Complex / O(n log n)"
# define STRAT_ADAPTIVE_SIMPLE_BENCH_MSG "Adaptive / O(n2)"
# define STRAT_ADAPTIVE_MEDIUM_BENCH_MSG   "Adaptive / O(n√n)"
# define STRAT_ADAPTIVE_COMPLEX_BENCH_MSG   "Adaptive / O(n log n)"

typedef enum e_strategy_type
{
	STRAT_SIMPLE,
	STRAT_MEDIUM,
	STRAT_COMPLEX,
	STRAT_ADAPTIVE,
	BENCH
}	t_strategy_type;

void	ft_exec_strat_dispatch(t_push_swap_ops_data *operations_data);
void	ft_do_small_sort(t_push_swap_ops_data *operations_data);
void	ft_do_medium_strategy_operations(
			t_push_swap_ops_data *operations_data, int chunk_size);
void	ft_do_medium_strategy_reconstruction(
			t_push_swap_ops_data *operations_data);
void	move_index_to_top(t_push_swap_ops_data *operations_data, size_t index);

#endif