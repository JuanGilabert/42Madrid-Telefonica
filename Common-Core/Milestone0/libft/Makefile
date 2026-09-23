# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/19 21:00:07 by jgilaber          #+#    #+#              #
#    Updated: 2026/06/22 19:03:13 by jgilaber         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

LIB_NAME = libft.a
LIB_SRCS = \
	ft_isalpha.c \
	ft_isdigit.c \
	ft_isalnum.c \
	ft_isascii.c \
	ft_isprint.c \
	ft_toupper.c \
	ft_tolower.c \
	ft_strlen.c \
	ft_strlcpy.c \
	ft_strncmp.c \
	ft_strlcat.c \
	ft_strnstr.c \
	ft_atoi.c \
	ft_strdup.c \
	ft_strchr.c \
	ft_strrchr.c \
	ft_bzero.c \
	ft_memset.c \
	ft_memcpy.c \
	ft_memcmp.c \
	ft_memchr.c \
	ft_calloc.c \
	ft_memmove.c \
	ft_substr.c \
	ft_strjoin.c \
	ft_strtrim.c \
	ft_split.c \
	ft_itoa.c \
	ft_strmapi.c \
	ft_striteri.c \
	ft_putchar_fd.c \
	ft_putstr_fd.c \
	ft_putendl_fd.c \
	ft_putnbr_fd.c \
	ft_lstnew.c \
	ft_lstadd_front.c \
	ft_lstsize.c \
	ft_lstlast.c \
	ft_lstadd_back.c \
	ft_lstdelone.c \
	ft_lstclear.c \
	ft_lstiter.c \
	ft_lstmap.c
LIB_OBJS = $(LIB_SRCS:.c=.o)
CC = cc
CFLAGS = -Wall -Wextra -Werror
CMD_AR_RCS_FLAG = ar rcs
CMD_RM_F_FLAG = rm -f
%.o: %.c
	@echo "Compiling  -> $< ..." 
	@$(CC) $(CFLAGS) -c $< -o $@
all: $(LIB_NAME)

$(LIB_NAME): $(LIB_OBJS)
	@echo "Doing ar comand ..."
	@$(CMD_AR_RCS_FLAG) $(LIB_NAME) $(LIB_OBJS)

clean:
	@echo "Doing clean ..."
	@$(CMD_RM_F_FLAG) $(LIB_OBJS)

fclean: clean
	@echo "Doing fclean ..."
	@$(CMD_RM_F_FLAG) $(LIB_NAME)

re: fclean all

.PHONY: all clean fclean re