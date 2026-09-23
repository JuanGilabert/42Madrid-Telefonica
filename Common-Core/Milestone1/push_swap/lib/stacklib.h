/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stacklib.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliao-tr <aliao-tr@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/09 18:45:33 by jgilaber          #+#    #+#             */
/*   Updated: 2026/08/20 17:58:51 by aliao-tr         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef STACKLIB_H
# define STACKLIB_H

# include <stddef.h>
# include "strategy.h"

typedef struct s_stack_node
{
	int					data;
	size_t				index;
	struct s_stack_node	*prev;
	struct s_stack_node	*next;
}	t_stack_node;

typedef struct s_stack
{
	t_stack_node	*top;
	int				size;
	double			disorder;
	t_strategy_type	strategy_used;
}	t_stack;

t_stack			*ft_new_stack(int strategy);
t_stack_node	*ft_new_stack_node(int data, int index);
t_stack_node	*ft_stack_last(t_stack *stack);
void			ft_stack_push(t_stack **stack, t_stack_node *new_stack_node);
void			ft_stack_clear(t_stack **stack);
int				ft_fill_stack(t_stack **stack, int *nmbrs, size_t nmbrs_size);
int				ft_check_stack_order(t_stack *stack);
size_t			ft_get_min_stack_node_index(t_stack **stack);
int				ft_get_min_stack_node_pos(t_stack **stack,
					size_t min_stack_node_index);
size_t			ft_get_max_stack_node_pos(t_stack *stack);

#endif