/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_parser_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliao-tr <aliao-tr@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/16 18:49:24 by aliao-tr          #+#    #+#             */
/*   Updated: 2026/07/21 20:24:32 by aliao-tr         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/// @brief does free
/// @param str characters from split
/// @return Nothing
/// @authors jgilaber & aliao-tr
void	ft_free_split(char **str)
{
	int	i;

	i = 0;
	if (!str)
		return ;
	while (str[i])
	{
		free(str[i]);
		i++;
	}
	free(str);
}

/// @brief Do free of str and numbers
/// @param str characters from split
/// @param numbers array of numbers
/// @return Nothing
/// @see ft_free_split
/// @authors jgilaber & aliao-tr
void	ft_free_all(char **str, int *numbers)
{
	if (str)
		ft_free_split(str);
	if (numbers)
		free(numbers);
}

/// @brief checks if the number if valid
/// @param str number
/// @return 0 if number is not valid, 1 if number is valid
/// @see ft_save_number
/// @authors jgilaber & aliao-tr
static int	ft_check_valid_numbers(char *str)
{
	int	i;

	i = 0;
	if (str[i] == '+' || str[i] == '-')
		i++;
	if (str[i] == '\0')
		return (0);
	while (str[i])
	{
		if (!ft_isdigit(str[i]))
			return (0);
		i++;
	}
	return (1);
}

/// @brief saves the number into the numbers array
/// @param str 
/// @param numbers array of numbers
/// @param size size of numbers
/// @param splt_str 
/// @return Nothing
/// @see ft_check_valid_numbers & ft_free_all
/// @authors jgilaber & aliao-tr
void	ft_save_numbr(char *str, char **splt_str, int *nbrs, size_t *nbrs_size)
{
	long	nbr;

	if (!ft_check_valid_numbers(str))
	{
		ft_free_all(splt_str, nbrs);
		ft_exit_program("Error", 1);
	}
	nbr = ft_atoi(str);
	if (nbr < INT_MIN || nbr > INT_MAX)
	{
		ft_free_all(splt_str, nbrs);
		ft_exit_program("Error", 1);
	}
	nbrs[*nbrs_size] = (int)nbr;
	(*nbrs_size)++;
}

/// @brief checks if there is a duplicated numbers
/// @param numbers array of numbers
/// @param size size of numbers array
/// @return 0 if theres no duplicates and 1 if there is duplicates.
/// @see ft_parse_args
/// @authors jgilaber & aliao-tr
int	ft_check_duplicates_numbers(int *numbers, int size)
{
	int	i;
	int	j;

	i = 0;
	while (i < size)
	{
		j = i + 1;
		while (j < size)
		{
			if (numbers[i] == numbers[j])
				return (1);
			j++;
		}
		i++;
	}
	return (0);
}
