/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 20:29:30 by jgilaber          #+#    #+#             */
/*   Updated: 2026/06/19 21:23:35 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void*))
{
	t_list	*lst_tmp_node;

	if (!lst || !del)
		return ;
	while (*lst != NULL)
	{
		lst_tmp_node = *lst;
		*lst = (*lst)->next;
		ft_lstdelone(lst_tmp_node, del);
	}
}
