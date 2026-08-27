/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/25 18:50:05 by jgilaber          #+#    #+#             */
/*   Updated: 2026/08/25 18:50:05 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

/// @brief Function that updates the stash
/// @param stash The gnl_stash
/// @return The line to return to the user/console(MEJORAR ESTE COMENTARIO)
/// @author jgilaber
static char	*ft_update_stash(char **stash)
{
	char	*readed_content;
	char	*stash_copy;
	int		i;

	i = 0;
	stash_copy = ft_strdup(*stash);
	if (!stash_copy)
		return (NULL);
	while (stash_copy[i] != '\0' && stash_copy[i] != '\n')
		i++;
	if (stash_copy[i] != '\0' && stash_copy[i] == '\n')
		i++;
	readed_content = ft_substr(stash_copy, 0, i);
	if (!readed_content)
		return (free(stash_copy), NULL);
	free(*stash);
	*stash = ft_substr(stash_copy, i, ft_strlen(stash_copy));
	free(stash_copy);
	if (!*stash)
		return (free(readed_content), NULL);
	if (readed_content[0] == '\0')
		return (free(readed_content), NULL);
	return (readed_content);
}

/// @brief Function that reads the file and updates the stack
/// with the rest of the line after the delimiter
/// @param fd The file descriptor of the file
/// @param stash The stash tu update with the rest of the line
/// @return The readed line
/// @author jgilaber
static char	*ft_read_line(int fd, char **stash)
{
	char	*readed_content;
	char	*temp_stash;
	int		bytes_read;

	readed_content = malloc(sizeof(char) * (BUFFER_SIZE + 1));
	if (!readed_content)
		return (free(readed_content), NULL);
	bytes_read = 1;
	while (bytes_read > 0)
	{
		bytes_read = read(fd, readed_content, BUFFER_SIZE);
		if (bytes_read < 0)
			return (free(readed_content), NULL);
		readed_content[bytes_read] = '\0';
		temp_stash = *stash;
		*stash = ft_strjoin(temp_stash, readed_content);
		free(temp_stash);
		if (!*stash)
			return (free(readed_content), NULL);
		if (ft_strchr(*stash, LINE_DELIM) || bytes_read == 0)
			return (free(readed_content), ft_update_stash(stash));
	}
	free(readed_content);
	return (NULL);
}

/// @brief Funtion that returns the next line of a file
/// @param fd The file descriptor of the file to read
/// @return The next line of the file
/// @author jgilaber
char	*get_next_line(int fd)
{
	static char	*stash;
	char		*readed_line;

	if (fd < 0 || fd > 1024 || BUFFER_SIZE < 1)
		return (NULL);
	if (!stash)
	{
		stash = ft_strdup("");
		if (!stash)
			return (NULL);
	}
	if (ft_strchr(stash, LINE_DELIM))
	{
		readed_line = ft_update_stash(&stash);
		if (!readed_line)
			return (free(stash), stash = NULL, NULL);
		return (readed_line);
	}
	readed_line = ft_read_line(fd, &stash);
	if (!readed_line)
		return (free(stash), stash = NULL, NULL);
	return (readed_line);
}
