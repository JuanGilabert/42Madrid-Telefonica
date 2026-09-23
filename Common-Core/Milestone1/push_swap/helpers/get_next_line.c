/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aliao-tr <aliao-tr@student.42madrid.com>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/23 11:08:42 by aliao-tr          #+#    #+#             */
/*   Updated: 2026/06/30 16:06:34 by aliao-tr         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static char	*update_stash(char **stash)
{
	char	*content_read;
	char	*stash_cpy;
	int		i;

	i = 0;
	stash_cpy = ft_strdup(*stash);
	if (stash_cpy == NULL)
		return (NULL);
	while (stash_cpy[i] != '\0' && stash_cpy[i] != '\n')
		i++;
	if (stash_cpy[i] != '\0' && stash_cpy[i] == '\n')
		i++;
	content_read = ft_substr(stash_cpy, 0, i);
	if (content_read == NULL)
		return (free(stash_cpy), NULL);
	free(*stash);
	*stash = ft_substr(stash_cpy, i, ft_strlen(stash_cpy));
	free(stash_cpy);
	if (*stash == NULL)
		return (free(content_read), NULL);
	if (content_read[0] == '\0')
		return (free(content_read), NULL);
	return (content_read);
}

static char	*read_line(int fd, char **stash)
{
	char	*read_content;
	char	*temp;
	int		read_byte;

	read_content = malloc(sizeof(char) * (BUFFER_SIZE + 1));
	if (read_content == NULL)
		return (free(read_content), NULL);
	read_byte = 1;
	while (read_byte > 0)
	{
		read_byte = read(fd, read_content, BUFFER_SIZE);
		if (read_byte < 0)
			return (free(read_content), NULL);
		read_content[read_byte] = '\0';
		temp = *stash;
		*stash = ft_strjoin(temp, read_content);
		free(temp);
		if (*stash == NULL)
			return (free(read_content), NULL);
		if (ft_strchr(*stash, '\n') || read_byte == 0)
			return (free(read_content), update_stash(stash));
	}
	free(read_content);
	return (NULL);
}

char	*get_next_line(int fd)
{
	static char	*stash;
	char		*content;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	if (stash == NULL)
	{
		stash = ft_strdup("");
		if (stash == NULL)
			return (NULL);
	}
	if (ft_strchr(stash, '\n'))
	{
		content = update_stash(&stash);
		if (content == NULL)
			return (free(stash), stash = NULL, NULL);
		return (content);
	}
	content = read_line(fd, &stash);
	if (content == NULL)
		return (free(stash), stash = NULL, NULL);
	return (content);
}
