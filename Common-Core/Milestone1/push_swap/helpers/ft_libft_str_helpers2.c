/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_libft_str_helpers2.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 19:40:39 by jgilaber          #+#    #+#             */
/*   Updated: 2026/06/19 21:30:12 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

long	ft_atoi(const char *nptr)
{
	long	atoi_nbr;
	int		atoi_nbr_sign;

	atoi_nbr_sign = 1;
	while (*nptr == ' ' || (*nptr > 6 && *nptr < 14))
		nptr++;
	if (*nptr == '+' || *nptr == '-')
	{
		if (*nptr == '-')
			atoi_nbr_sign = -atoi_nbr_sign;
		nptr++;
	}
	atoi_nbr = 0;
	while (*nptr > 47 && *nptr < 58)
	{
		atoi_nbr = (atoi_nbr * 10) + (*nptr - '0');
		nptr++;
	}
	return (atoi_nbr_sign * atoi_nbr);
}

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

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*str;
	char	*substr;

	if (!s)
		return (NULL);
	if (start >= ft_strlen(s) || len == 0)
		return (ft_strdup(""));
	if (start + len > ft_strlen(s))
		len = ft_strlen(s) - start;
	substr = malloc(sizeof(char) * (len + 1));
	if (!substr)
		return (NULL);
	str = (char *)s;
	ft_strlcpy(substr, &str[start], len + 1);
	return (substr);
}
