/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/28 20:48:10 by jgilaber          #+#    #+#             */
/*   Updated: 2026/06/19 22:53:49 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	unsigned char	*ptr_src;
	unsigned char	*ptr_dest;
	size_t			ptr_index;

	if (!dest || !src)
		return (dest);
	ptr_src = (unsigned char *)src;
	ptr_dest = (unsigned char *)dest;
	ptr_index = 0;
	while (ptr_index < n)
	{
		ptr_dest[ptr_index] = ptr_src[ptr_index];
		ptr_index++;
	}
	return (dest);
}
