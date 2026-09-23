/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jgilaber <jgilaber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 21:41:54 by jgilaber          #+#    #+#             */
/*   Updated: 2026/06/19 21:23:05 by jgilaber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*mapped_lst;
	t_list	*tmp_lst_node;
	void	*tmp_lst_node_content;

	if (!lst || !f || !del)
		return (NULL);
	mapped_lst = NULL;
	while (lst != NULL)
	{
		tmp_lst_node_content = f(lst->content);
		tmp_lst_node = ft_lstnew(tmp_lst_node_content);
		if (!tmp_lst_node)
		{
			ft_lstclear(&mapped_lst, del);
			return (NULL);
		}
		ft_lstadd_back(&mapped_lst, tmp_lst_node);
		lst = lst->next;
	}
	return (mapped_lst);
}
