LIB_NAME		:= push_swap.a
LIB_NAME_EXE	:= push_swap
LIB_SRCS_DIRS	:= . bench core errors helpers parser stack strategy utils
LIB_SRCS_FILES	:= $(foreach dir,$(LIB_SRCS_DIRS),$(wildcard $(dir)/*.c))
LIB_OBJS_DIR	:= build
LIB_OBJS_FILES	:= $(addprefix $(LIB_OBJS_DIR)/,$(LIB_SRCS_FILES:.c=.o))
CC				:= cc
CFLAGS			:= -Wall -Wextra -Werror
CINCLUDES		:= -I ./lib
CMD_RM_FLAGS	:= rm -rf
CMD_AR_FLAGS	:= ar rcs


all: $(LIB_NAME_EXE)

$(LIB_NAME_EXE): ft_push_swap.c $(LIB_NAME)
	@$(CC) $(CFLAGS) $(CINCLUDES) ft_push_swap.c $(LIB_NAME) -o $(LIB_NAME_EXE)

$(LIB_OBJS_DIR)/%.o: %.c
	@mkdir -p $(dir $@)
	@echo "Compiling -> $< ..."
	@$(CC) $(CFLAGS) $(CINCLUDES) -c $< -o $@

$(LIB_NAME): $(LIB_OBJS_FILES)
	@echo "Executing command -> ar rcs $(LIB_NAME) $(LIB_OBJS_FILES)"
	@$(CMD_AR_FLAGS) $(LIB_NAME) $(LIB_OBJS_FILES)
	@echo ""


clean:
	@echo "Cleaning ..."
	@if [ -n "$$(find $(LIB_OBJS_DIR) -mindepth 1 -print -quit 2>/dev/null)" ]; then \
		echo "Removing -> $(CMD_RM_FLAGS) $(LIB_OBJS_DIR)/* ..."; \
		$(CMD_RM_FLAGS) $(LIB_OBJS_DIR)/*; \
	fi
	@echo ""

fclean: clean
	@echo "Full Cleaning ..."
	@echo "Removing -> $(CMD_RM_FLAGS) $(LIB_NAME) ..."
	@$(CMD_RM_FLAGS) $(LIB_NAME)
	@echo "Removing -> $(CMD_RM_FLAGS) $(LIB_NAME_EXE) ..."
	@$(CMD_RM_FLAGS) $(LIB_NAME_EXE)
	@echo ""

re: fclean all

.PHONY: all clean fclean re