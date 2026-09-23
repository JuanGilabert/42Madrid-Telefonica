/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap_helpers.h                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/01 21:40:06 by jgilaber          #+#    #+#             */
/*   Updated: 2026/08/21 15:11:41 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_HELPERS_H
# define PUSH_SWAP_HELPERS_H

# include <stddef.h>

int		ft_isdigit(int c);
long	ft_atoi(const char *nptr);
size_t	ft_strlen(const char *s);
char	*ft_strdup(const char *s);
char	**ft_split(char const *s, char c);
char	*ft_strchr(const char *str, int c);
char	*ft_strjoin(char const *s1, char const *s2);
int		ft_strncmp(char *s1, char *s2, unsigned int n);
size_t	ft_strlcpy(char *dst, const char *src, size_t size);
size_t	ft_strlcat(char *dest, const char *src, size_t size);
char	*ft_substr(char const *s, unsigned int start, size_t len);
void	ft_bzero(void *s, size_t n);
void	*ft_memset(void *s, int c, size_t n);
void	*ft_calloc(size_t nmemb, size_t size);
void	*ft_memcpy(void *dest, const void *src, size_t n);
int		ft_memcmp(const void *s1, const void *s2, size_t n);
char	*ft_substr(char const *s, unsigned int start, size_t len);
void	ft_putchar_fd(char c, int fd);
void	ft_putstr_fd(char *s, int fd);
void	ft_putendl_fd(char *s, int fd);
void	ft_putnbr_fd(int n, int fd);
int		ft_printf(char const *format, ...);
int		ft_printchar(char c);
int		ft_printstr_fd(char *s);
int		ft_printnbr(long nbr);
int		ft_printunsignednbr(unsigned int nbr);
int		ft_printpointer(void *ptr);
int		ft_printhex(unsigned long nbr, char format);
char	*get_next_line(int fd);

#endif