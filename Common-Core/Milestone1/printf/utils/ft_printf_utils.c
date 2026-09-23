/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/24 19:09:34 by jgilaber          #+#    #+#             */
/*   Updated: 2026/07/07 18:38:46 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printhex(unsigned long nbr, char format)
{
	long			count;
	char			*base;
	unsigned int	base_len;

	base_len = 16;
	if (format == 'X')
		base = "0123456789ABCDEF";
	else
		base = "0123456789abcdef";
	count = 0;
	if (nbr >= base_len)
		count = ft_printhex((nbr / base_len), format);
	count += ft_printchar(base[nbr % base_len]);
	return (count);
}

int	ft_putnbr(long nbr)
{
	int	count;

	count = 0;
	if (nbr < 0)
	{
		count += ft_printchar('-');
		nbr = -nbr;
	}
	if (nbr >= 10)
	{
		count += ft_printnbr(nbr / 10);
	}
	count += ft_printchar((nbr % 10) + '0');
	return (count);
}

int	ft_printunsignednbr(unsigned int nbr)
{
	int	count;

	count = 0;
	if (nbr >= 10)
	{
		count += ft_printunsignednbr(nbr / 10);
	}
	count += ft_printchar((nbr % 10) + '0');
	return (count);
}

int	ft_printpointer(void *ptr)
{
	int	count;

	if (!ptr)
		return (ft_printstr_fd("(nil)", 1));
	count = ft_printstr_fd("0x", 1);
	count += ft_printhex((unsigned long)ptr, 'p');
	return (count);
}
