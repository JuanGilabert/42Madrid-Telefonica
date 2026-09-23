/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_parser_flags.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliao-tr <aliao-tr@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/16 18:49:24 by aliao-tr          #+#    #+#             */
/*   Updated: 2026/07/21 20:24:32 by aliao-tr         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/// @brief check which type of flag is
/// @param str string of the argument
/// @return number of the strategy, -1 if it's not a known strategy
/// @see ft_check_nbr_or_flag
/// @authors jgilaber & aliao-tr
static int	ft_check_strategy_flag_type(char *str)
{
	if (ft_strncmp(str, "--simple", 9) == 0)
		return (STRAT_SIMPLE);
	if (ft_strncmp(str, "--medium", 9) == 0)
		return (STRAT_MEDIUM);
	if (ft_strncmp(str, "--complex", 10) == 0)
		return (STRAT_COMPLEX);
	if (ft_strncmp(str, "--adaptive", 11) == 0)
		return (STRAT_ADAPTIVE);
	if (ft_strncmp(str, "--bench", 8) == 0)
		return (BENCH);
	return (-1);
}

/// @brief redirects if argument is a flag or a number
/// @param str string from split
/// @param flags array of flags
/// @param numbers array of numbers
/// @param size size of numbers array
/// @return Nothing
/// @see ft_check_strategy_flag_type & ft_save_number
/// @authors jgilaber & aliao-tr
void	ft_check_nbr_or_flag(char **str, int *flags, int *nmbrs, size_t *size)
{
	int	i;
	int	type;

	i = 0;
	while (str[i])
	{
		type = ft_check_strategy_flag_type(str[i]);
		if (type != -1)
			flags[type]++;
		else
			ft_save_numbr(str[i], str, nmbrs, size);
		i++;
	}
}

/// @brief checks which flag is > 0
/// @param flags array of flags
/// @return 1 if there is zero or one flag, otherwise 0
/// @see ft_parse_args
/// @authors jgilaber & aliao-tr
int	ft_check_strategy_flags(int *flags)
{
	int	i;
	int	count;

	i = 0;
	count = 0;
	while (i < 4)
	{
		if (flags[i] > 0)
			count++;
		i++;
	}
	return (count > 1);
}

/// @brief returns the correspondent flag
/// @param flags array of flags
/// @return number of the strategy
/// @see ft_push_swap
/// @authors jgilaber & aliao-tr
int	ft_get_strategy_flag(int *flags)
{
	if (flags[STRAT_SIMPLE])
		return (STRAT_SIMPLE);
	if (flags[STRAT_MEDIUM])
		return (STRAT_MEDIUM);
	if (flags[STRAT_COMPLEX])
		return (STRAT_COMPLEX);
	if (flags[STRAT_ADAPTIVE])
		return (STRAT_ADAPTIVE);
	return (STRAT_ADAPTIVE);
}
