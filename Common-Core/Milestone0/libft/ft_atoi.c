/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/16 12:05:33 by jgilaber          #+#    #+#             */
/*   Updated: 2026/06/19 21:18:11 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_atoi(const char *nptr)
{
	int	atoi_nbr;
	int	atoi_nbr_sign;

	atoi_nbr_sign = 1;
	while (*nptr == ' ' || (*nptr > 6 && *nptr < 14))
		nptr++;
	if (*nptr == '+' || *nptr == '-')
	{
		if (*nptr == '-')
			atoi_nbr_sign = -atoi_nbr_sign;
		nptr++;
	}
	atoi_nbr = 0;
	while (*nptr > 47 && *nptr < 58)
	{
		atoi_nbr = (atoi_nbr * 10) + (*nptr - '0');
		nptr++;
	}
	return (atoi_nbr_sign * atoi_nbr);
}
