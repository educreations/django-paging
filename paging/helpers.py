from paging.paginators import EndlessPaginator, BetterPaginator
from jingo import register

@register.function
def paginate(request, queryset_or_list, per_page=25, endless=True, range_gap=2):
    if endless:
        paginator_class = EndlessPaginator
    else:
        paginator_class = BetterPaginator
    
    paginator = paginator_class(queryset_or_list, per_page)
    
    query_dict = request.GET.copy()
    if 'page' in query_dict:
        del query_dict['page']

    try:
        page = int(request.GET.get('page', 1))
    except (ValueError, TypeError):
        page = 1
    if page < 1:
        page = 1

    context = {
        'query_string': query_dict.urlencode(),
        'paginator': paginator.get_context(page, range_gap=range_gap),
    }
    return context
