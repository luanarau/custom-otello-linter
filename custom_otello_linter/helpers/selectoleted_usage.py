import ast


def imports_selectoleted(import_from_nodes: list[ast.ImportFrom]) -> bool:
    """
    Есть ли в файле `from …selectoleted import selectoleted` (модуль заканчивается на selectoleted).
    """
    for node in import_from_nodes:
        if not node.module or not node.module.endswith('selectoleted'):
            continue
        if any(alias.name == 'selectoleted' for alias in node.names):
            return True
    return False


def is_selectoleted_call(func: ast.AST, import_from_nodes: list[ast.ImportFrom]) -> bool:
    """
    Вызов `selectoleted(...)` в правой части присваивания, если функция импортирована из модуля selectolet.
    """
    if isinstance(func, ast.Name) and func.id == 'selectoleted':
        return imports_selectoleted(import_from_nodes)
    return False


def is_selectoleted_decorator(decorator: ast.AST, import_from_nodes: list[ast.ImportFrom]) -> bool:
    """
    Декоратор `@selectoleted` или `@selectoleted(...)` при импорте selectoleted из e2e selectolet.
    """
    if isinstance(decorator, ast.Name) and decorator.id == 'selectoleted':
        return imports_selectoleted(import_from_nodes)

    if isinstance(decorator, ast.Call):
        return is_selectoleted_call(decorator.func, import_from_nodes)

    return False
