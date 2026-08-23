/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/02 21:11:02 by jgilaber          #+#    #+#             */
/*   Updated: 2026/06/22 18:51:17 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	ft_get_init_word_index(
	const char *str, char c, size_t init_word_index
)
{
	while (str[init_word_index] && str[init_word_index] == c)
		init_word_index++;
	return (init_word_index);
}

static size_t	ft_get_final_word_index(
	const char *str, char c, size_t final_word_index
)
{
	while (str[final_word_index] && str[final_word_index] != c)
		final_word_index++;
	return (final_word_index);
}

static size_t	ft_get_word_count(const char *str, char c)
{
	size_t	str_index;
	size_t	word_count;

	str_index = 0;
	word_count = 0;
	while (str[str_index])
	{
		str_index = ft_get_init_word_index(str, c, str_index);
		if (str[str_index])
		{
			str_index = ft_get_final_word_index(str, c, str_index);
			word_count++;
		}
	}
	return (word_count);
}

static char	**ft_do_split(char const *s, char c, char **split)
{
	size_t	split_index;
	size_t	init_word_index;
	size_t	final_word_index;

	split_index = 0;
	init_word_index = 0;
	while (split_index < ft_get_word_count(s, c))
	{
		init_word_index = ft_get_init_word_index(s, c, init_word_index);
		final_word_index = ft_get_final_word_index(s, c, init_word_index);
		split[split_index] = ft_substr(
				s, init_word_index, final_word_index - init_word_index);
		if (!split[split_index])
		{
			while (split_index-- > 0)
				free(split[split_index]);
			free(split);
			return (NULL);
		}
		init_word_index = final_word_index + 1;
		split_index++;
	}
	return (split);
}

char	**ft_split(char const *s, char c)
{
	char	**split;

	if (!s)
		return (NULL);
	split = malloc(sizeof(char *) * (ft_get_word_count(s, c) + 1));
	if (!split)
		return (NULL);
	if (ft_get_word_count(s, c) == 0)
	{
		split[0] = NULL;
		return (split);
	}
	if (ft_do_split(s, c, split) != NULL)
	{
		split[ft_get_word_count(s, c)] = NULL;
		return (split);
	}
	return (NULL);
}
