/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/29 02:24:52 by jgilaber          #+#    #+#             */
/*   Updated: 2026/06/19 22:49:32 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	unsigned char	*ptr_dest;
	unsigned char	*ptr_src;

	ptr_dest = (unsigned char *)dest;
	ptr_src = (unsigned char *)src;
	if (!ptr_dest || !ptr_src)
		return (NULL);
	if (ptr_src < ptr_dest)
	{
		while (n-- > 0)
			ptr_dest[n] = ptr_src[n];
	}
	else
		ft_memcpy(dest, src, n);
	return (dest);
}
