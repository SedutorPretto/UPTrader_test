from django import template

from ..models import MenuItem

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.inclusion_tag(filename='menu.html', takes_context=True)
def draw_menu(context, menu_name: str = None):

    request = context['request']
    current_url = request.build_absolute_uri()

    items = MenuItem.objects.select_related('parent', 'menu').filter(menu__name=menu_name)

    def find_active_item(items, current_url):
        for item in items:
            if item.get_url() == current_url:
                return item
        return None

    active_item_obj = find_active_item(items, current_url)


    def build_start_tree(items):
        base_tree = []
        for item in items:
            if item.parent is None:
                base_tree.append({'item': item, 'children': []})
        return base_tree

    def root_sick(active_element):
        while active_element.parent:
            active_element = active_element.parent
        return active_element


    def build_tree_upwards(menu_items, active_item, root_elem):
        tree = []
        subtree = []
        current_item = active_item
        for item in menu_items:
            if item.parent == current_item:
                subtree.append({'item': item, 'children': []})

        while current_item != root_elem:
            for item in menu_items:
                if item.parent == current_item.parent and item == current_item:
                    tree.append({'item': item, 'children': subtree})
                elif item.parent == current_item.parent:
                    tree.append({'item': item, 'children': []})


            subtree = tree
            tree = []
            current_item = current_item.parent

        return subtree

    if active_item_obj:
        base_tree = build_start_tree(items)
        root_elem = root_sick(active_item_obj)
        tree = build_tree_upwards(items, active_item_obj, root_elem)
        for elem in base_tree:
            if elem['item'] == root_elem:
                elem['children'].extend(tree)


    else:
        base_tree = build_start_tree(items)

    return {
        'menu': base_tree,
        'active_item': active_item_obj,
        'request': request,
        'depth': 0
    }
