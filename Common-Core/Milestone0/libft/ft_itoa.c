/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/01 21:33:51 by jgilaber          #+#    #+#             */
/*   Updated: 2026/06/22 18:48:58 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	ft_get_itoa_number_length(int n)
{
	size_t	nbr_digits;

	if (!n)
		return (1);
	nbr_digits = 0;
	while (n != 0)
	{
		n /= 10;
		nbr_digits++;
	}
	return (nbr_digits);
}

static void	ft_do_itoa_positive(long nbr, size_t nbr_len, char *itoa_nbr)
{
	while (nbr_len > 0)
	{
		itoa_nbr[--nbr_len] = (nbr % 10) + '0';
		nbr = nbr / 10;
	}
}

static void	ft_do_itoa_negative(long nbr, size_t nbr_len, char *itoa_nbr)
{
	itoa_nbr[0] = '-';
	while (nbr_len > 1)
	{
		itoa_nbr[--nbr_len] = (nbr % 10) + '0';
		nbr = nbr / 10;
	}
}

char	*ft_itoa(int n)
{
	long	nbr;
	size_t	nbr_len;
	char	*itoa_nbr;
	int		itoa_nbr_sign;

	nbr = n;
	nbr_len = ft_get_itoa_number_length(nbr);
	itoa_nbr_sign = 0;
	if (nbr < 0)
	{
		itoa_nbr_sign = 1;
		nbr = -nbr;
		nbr_len++;
	}
	itoa_nbr = ft_calloc(sizeof(char), nbr_len + 1);
	if (!itoa_nbr)
		return (NULL);
	if (itoa_nbr_sign)
		ft_do_itoa_negative(nbr, nbr_len, itoa_nbr);
	else
		ft_do_itoa_positive(nbr, nbr_len, itoa_nbr);
	return (itoa_nbr);
}
