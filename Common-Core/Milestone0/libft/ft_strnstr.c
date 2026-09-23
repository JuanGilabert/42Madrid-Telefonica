/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/01 21:36:41 by jgilaber          #+#    #+#             */
/*   Updated: 2026/06/19 21:29:52 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t	big_indx;
	size_t	lit_indx;

	if (!little[0])
		return ((char *)big);
	big_indx = 0;
	while (big[big_indx] && big_indx < len)
	{
		lit_indx = 0;
		while (big[big_indx + lit_indx] == little[lit_indx]
			&& big_indx + lit_indx < len)
			lit_indx++;
		if (!little[lit_indx])
			return ((char *)(big + big_indx));
		big_indx++;
	}
	return (NULL);
}
