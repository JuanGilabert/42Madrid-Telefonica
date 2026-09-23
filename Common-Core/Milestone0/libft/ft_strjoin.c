/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/01 21:38:02 by jgilaber          #+#    #+#             */
/*   Updated: 2026/06/19 21:30:48 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*strjoin;
	size_t	strings_length;

	if (!s1 || !s2)
		return (NULL);
	strings_length = (ft_strlen(s1) + ft_strlen(s2)) + 1;
	strjoin = malloc(sizeof(char) * (strings_length));
	if (!strjoin)
		return (NULL);
	ft_strlcpy(strjoin, s1, strings_length);
	ft_strlcat(strjoin, s2, strings_length);
	return (strjoin);
}
