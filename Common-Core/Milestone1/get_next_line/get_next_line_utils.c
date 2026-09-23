/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/25 18:50:15 by jgilaber          #+#    #+#             */
/*   Updated: 2026/08/25 18:50:15 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

/// @brief Function that returns the length of a string
/// @param s The string to ¿measure?
/// @return The length of the string
size_t	ft_strlen(const char *s)
{
	int	str_index;

	str_index = 0;
	while (s[str_index])
		str_index++;
	return (str_index);
}

/// @brief Function that duplicates a string
/// @param s The string to duplicate
/// @return The duplicated string
char	*ft_strdup(char *s)
{
	size_t	str_len;
	int		i;
	char	*str;

	i = 0;
	str_len = ft_strlen(s);
	str = malloc((sizeof(char) * str_len + 1));
	if (!str)
		return (NULL);
	while (s[i] != '\0')
	{
		str[i] = s[i];
		i++;
	}
	str[i] = '\0';
	return (str);
}

/// @brief Function that locates a character in a string
/// @param str The string to search in
/// @param c The character to locate
/// @return The pointer to the first occurrence of the character in the string
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

/// @brief Function that concatenates two strings
/// @param s1 The first string
/// @param s2 The second string
/// @return The concatenated strings
char	*ft_strjoin(char *s1, char *s2)
{
	char	*str;
	size_t	i;
	size_t	j;

	if (!s1 || !s2)
		return (NULL);
	str = malloc (sizeof(char) * (ft_strlen(s1) + ft_strlen(s2) + 1));
	if (!str)
		return (NULL);
	i = 0;
	while (s1[i] != '\0')
	{
		str[i] = s1[i];
		i++;
	}
	j = 0;
	while (s2[j] != '\0')
	{
		str[i + j] = s2[j];
		j++;
	}
	str[i + j] = '\0';
	return (str);
}

/// @brief 
/// @param s 
/// @param start 
/// @param len 
/// @return 
char	*ft_substr(char *s, unsigned int start, size_t len)
{
	char	*str;
	size_t	slen;
	size_t	i;

	if (s == NULL)
		return (NULL);
	slen = ft_strlen(s);
	if (start >= slen)
		return (ft_strdup(""));
	if (len > slen - start)
		len = slen - start;
	str = malloc(sizeof(char) * len + 1);
	if (str == NULL)
		return (NULL);
	i = 0;
	while (s[start + i] != '\0' && i < len)
	{
		str[i] = s[start + i];
		i++;
	}
	str[i] = '\0';
	return (str);
}
