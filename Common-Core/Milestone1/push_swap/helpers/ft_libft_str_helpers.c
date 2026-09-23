/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_libft_str_helpers.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 19:40:39 by jgilaber          #+#    #+#             */
/*   Updated: 2026/06/19 21:30:12 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

size_t	ft_strlen(const char *s)
{
	int	str_index;

	str_index = 0;
	while (s[str_index])
		str_index++;
	return (str_index);
}

int	ft_strncmp(char *s1, char *s2, unsigned int n)
{
	size_t	i;

	if (!n)
		return (n);
	i = 0;
	while ((s1[i] && s2[i]) && s1[i] == s2[i] && i < n - 1)
		i++;
	return ((unsigned char)s1[i] - (unsigned char)s2[i]);
}

char	*ft_strdup(const char *s)
{
	char	*str_dup;

	if (!s)
		return (NULL);
	str_dup = (char *) ft_calloc(sizeof(char), (ft_strlen(s) + 1));
	if (!str_dup)
		return (NULL);
	ft_memcpy(str_dup, s, ft_strlen(s));
	return (str_dup);
}

size_t	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t	src_len;
	size_t	copy_len;

	src_len = ft_strlen(src);
	if (size == 0)
		return (src_len);
	copy_len = src_len;
	if (src_len >= size)
		copy_len = size - 1;
	ft_memcpy(dst, src, copy_len);
	dst[copy_len] = '\0';
	return (src_len);
}

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
