from django import template
from django.utils.safestring import mark_safe

from menu.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    path = request.path
    menu_items = MenuItem.objects.filter(parent=None, name=menu_name)
    menu_root = menu_items.first()

    current_page = MenuItem.objects.filter(url__endswith=path).first()

    parents = []
    if current_page and (current_page.root == menu_root or menu_root == current_page):
        parents.append(current_page)
        while parent := current_page.parent:
            parents.append(parent)
            current_page = parent

    dropdown_class = f'dropdown-menu{" show" if parents else ""}'

    html = f"""
        <div class='btn-group mx-3 my-1'>
            <a class="btn btn-outline-dark btn-sm pt-2" type="button" href="{menu_root.url}">
                {menu_root.name}
            </a>
            <button class='btn btn-outline-dark dropdown-toggle dropdown-toggle-split' type='button'
                id='dropdownMenuButton' data-mdb-toggle='dropdown' aria-expanded='false'>
                <span class="visually-hidden">Toggle Dropdown</span>
            </button>
            <ul class='{dropdown_class}' aria-labelledby='dropdownMenuButton'>
                {_draw_menu_items(menu_root.children.all(), path, parents)}
            </ul>
        </div>
    """
    return mark_safe(html)


def _draw_menu_items(menu_items, path, parents, parent=None):
    active_parent = parent in parents
    submenu_class = f"{parent} dropdown-menu dropdown-submenu{' show' if active_parent else ''}" if parent else ""

    items_html = ''.join([
        f"""
        <li class='{item.name}'>
            <a class='dropdown-item {"active" if item.url.endswith(path) else ""}' href='{item.url}'>
                {item.name}
            </a>
            {_draw_menu_items(item.children.all(),
                              path,
                              parents,
                              parent=item) if item.children.exists() else ''}
        </li>
        """
        for item in menu_items
    ])

    html = f"""
        <ul class='{submenu_class}'>
            {items_html}
        </ul>
    """ if submenu_class else items_html
    return html
