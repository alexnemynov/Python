def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1_000_000:
        return f'{round(size / 1024)} KB'
    elif 1_000_000 <= size < 1_000_000_000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'