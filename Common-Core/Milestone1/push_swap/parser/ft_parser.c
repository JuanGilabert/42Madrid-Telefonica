/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_parser.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliao-tr <aliao-tr@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/16 18:49:24 by aliao-tr          #+#    #+#             */
/*   Updated: 2026/07/21 20:24:32 by aliao-tr         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/// @brief counts how many numbers there are
/// @param argc numbers of arguments
/// @param argv value of arguments
/// @return how many numbers there are, -1 on error.
/// @see main(ft_push_swap.c) & free_ft_split
/// @authors jgilaber & aliao-tr
int	ft_count_numbers(int argc, char **argv)
{
	char	**str;
	int		i;
	int		j;
	int		count;

	i = 1;
	count = 0;
	while (i < argc)
	{
		str = ft_split(argv[i], ' ');
		if (!str)
			return (-1);
		j = 0;
		while (str[j])
		{
			if (str[j][0] != '-' || str[j][1] != '-')
				count++;
			j++;
		}
		ft_free_split(str);
		i++;
	}
	return (count);
}

/// @brief checks argument and splits the argument
/// @param argc number of arguments
/// @param argv value of arguments
/// @param flags array for flags
/// @param numbers array of int-numbers
/// @return Returns 1 on success, 0 on failure (e.g., mem-alloc-fail).
/// @see main(ft_push_swap.c), ft_check_nbr_or_flag, ft_free_split,
/// ft_check_strategy_flags & ft_check_duplicates_numbers
/// @authors jgilaber & aliao-tr
int	ft_parse_args(int argc, char **argv, int *flags, int *numbers)
{
	char	**str;
	int		i;
	size_t	numbers_size;
	int		has_duplicated_numbers;
	int		has_duplicated_strategy_flags;

	i = 1;
	numbers_size = 0;
	while (i < argc)
	{
		str = ft_split(argv[i], ' ');
		if (!str)
			return (0);
		ft_check_nbr_or_flag(str, flags, numbers, &numbers_size);
		ft_free_split(str);
		i++;
	}
	has_duplicated_strategy_flags = ft_check_strategy_flags(flags);
	has_duplicated_numbers = ft_check_duplicates_numbers(numbers, numbers_size);
	if (has_duplicated_strategy_flags || has_duplicated_numbers)
		return (0);
	return (1);
}
