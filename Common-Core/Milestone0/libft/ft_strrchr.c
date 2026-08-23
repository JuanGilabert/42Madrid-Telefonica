/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/01 21:36:30 by jgilaber          #+#    #+#             */
/*   Updated: 2026/06/22 18:32:26 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	int		str_len;
	char	*str;
	char	c_chr;

	str = (char *)s;
	c_chr = (char) c;
	str_len = ft_strlen(s);
	while (str_len >= 0)
	{
		if (str[str_len] == c_chr)
			return (&str[str_len]);
		str_len--;
	}
	return (NULL);
}
