/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/24 19:09:22 by jgilaber          #+#    #+#             */
/*   Updated: 2026/07/07 18:38:49 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putchar(char c)
{
	return (write(STDOUT_FILENO, &c, 1));
}

int	ft_putstr(char *s)
{
	int	i;

	i = 0;
	if (s == NULL)
		s = "(null)";
	while (s[i] != '\0')
	{
		write(STDOUT_FILENO, &s[i], 1);
		i++;
	}
	return (i);
}

static int	check_format(char format, va_list args)
{
	if (format == 'c')
		return (ft_putchar(va_arg(args, int)));
	else if (format == 's')
		return (ft_putstr(va_arg(args, char *)));
	else if (format == 'd' || format == 'i')
		return (ft_putnbr(va_arg(args, int)));
	else if (format == 'p')
		return (ft_printpointer(va_arg(args, void *)));
	else if (format == 'u')
		return (ft_printunsignednbr(va_arg(args, unsigned int)));
	else if (format == 'x' || format == 'X')
		return (ft_printhex(va_arg(args, unsigned int), format));
	else if (format == '%')
		return (ft_putchar('%'));
	return (-1);
}

int	ft_printf(char const *format, ...)
{
	va_list	args;
	int		printf_length;

	if (format == NULL)
		return (-1);
	printf_length = 0;
	va_start(args, format);
	while (*format)
	{
		if (*format == '%' && !*format)
			return (-1);
		else if (*format == '%')
		{
			format++;
			printf_length += check_format(*format, args);
		}
		else
			printf_length += write(STDOUT_FILENO, format, 1);
		format++;
	}
	va_end(args);
	return (printf_length);
}
