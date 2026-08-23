/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/18 23:32:12 by jgilaber          #+#    #+#             */
/*   Updated: 2026/06/19 22:47:24 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

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
