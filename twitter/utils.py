def check_id_or_screen_name(screen_name, user_id):
    if (screen_name, user_id) == (None, None):
        raise ValueError("Please set one of these attributes [screen_names, user_ids].")


def check_ids_or_screen_names(screen_names, user_ids):
    check_id_or_screen_name(screen_names, user_ids)
    if screen_names and type(screen_names) != list:
        screen_names = [screen_names]
    if user_ids and type(user_ids) != list:
        user_ids = [user_ids]
    if not screen_names:
        screen_names = []
    if not user_ids:
        user_ids = []
    return screen_names, user_ids
