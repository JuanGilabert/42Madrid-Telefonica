/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/01 21:36:25 by jgilaber          #+#    #+#             */
/*   Updated: 2026/06/19 21:29:14 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	unsigned int	s1_init;
	unsigned int	s1_final;

	if (!s1 || !set)
		return (NULL);
	s1_init = 0;
	s1_final = ft_strlen(s1);
	while (ft_strchr(set, s1[s1_init]))
		s1_init++;
	while (s1_final > s1_init && ft_strchr(set, s1[s1_final - 1]))
		s1_final--;
	return (ft_substr(s1, s1_init, (s1_final - s1_init)));
}
