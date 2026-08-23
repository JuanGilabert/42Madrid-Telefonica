/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/12 05:05:56 by jgilaber          #+#    #+#             */
/*   Updated: 2026/06/19 21:39:24 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dest, const char *src, size_t size)
{
	size_t	dest_len;
	size_t	src_len;
	size_t	src_index;

	dest_len = ft_strlen(dest);
	src_len = ft_strlen(src);
	src_index = 0;
	if (size <= dest_len)
		return (src_len + size);
	while (src[src_index] && src_index < size - dest_len - 1)
	{
		dest[dest_len + src_index] = src[src_index];
		src_index++;
	}
	dest[dest_len + src_index] = '\0';
	return (dest_len + src_len);
}
