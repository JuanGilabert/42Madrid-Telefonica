/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/01 19:55:14 by jgilaber          #+#    #+#             */
/*   Updated: 2026/06/19 21:31:51 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strchr(const char *str, int c)
{
	char	c_chr;
	char	*string_str;
	size_t	str_index;

	string_str = (char *)str;
	if (!c)
		return (string_str + ft_strlen(str));
	c_chr = (char) c;
	str_index = 0;
	while (string_str[str_index])
	{
		if (string_str[str_index] == c_chr)
			return (&string_str[str_index]);
		str_index++;
	}
	return (NULL);
}
