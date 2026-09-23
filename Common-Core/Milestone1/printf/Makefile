NAME = libftprintf.a
PRINTF_LIB_DIR = utils/
PRINTF_LIB_SRCS = ft_printf.c
PRINTF_LIB_FILES = \
	ft_printf_utils.c
PRINTF_LIB_SRCS += $(addprefix $(PRINTF_LIB_DIR), $(PRINTF_LIB_FILES))
PRINTF_LIB_OBJS = $(PRINTF_LIB_SRCS:.c=.o)
CC = cc
CFLAGS = 
CINCLUDES = -I ./includes
CMD_AR_RCS_FLAG = ar rcs
CMD_RM_F_FLAG = rm -f

%.o: %.c
	@echo "Compiling -> $< ..."
	@$(CC) $(CFLAGS) $(CINCLUDES) -c $< -o $@

$(NAME): $(PRINTF_LIB_OBJS)
	@echo "Executing command -> ar rcs $(NAME) $(PRINTF_LIB_OBJS)"
	@$(CMD_AR_RCS_FLAG) $(NAME) $(PRINTF_LIB_OBJS)

all: $(NAME)

clean:
	@echo "Doing Clean ..."
	@$(CMD_RM_F_FLAG) $(PRINTF_LIB_OBJS)

fclean: clean
	@echo "Doing fclean ..."
	@$(CMD_RM_F_FLAG) $(NAME)

re: fclean all

.PHONY: all clean fclean re