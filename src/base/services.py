import os

from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """ Построение пути к файлу, format: (media)/avatar/user_id/photo.jpg
    """
    return f'avatar/user_{instance.id}/{file}'


def get_path_upload_cover_album(instance, file):
    """ Построение пути к файлу, format: (media)/album/user_id/photo.jpg
    """
    return f'album/user_{instance.user.id}/{file}'


def get_path_upload_cover_playlist(instance, file):
    """ Построение пути к файлу, format: (media)/playlist/user_id/photo.jpg
    """
    return f'playlist/user_{instance.user.id}/{file}'


def get_path_upload_track(instance, file):
    """ Построение пути к файлу, format: (media)/track/user_id/audio.pm3
    """
    return f'track/user_{instance.user.id}/{file}'


def get_path_upload_cover_track(instance, file):
    """ Построение пути к файлу, format: (media)/track/cover/user_id/photo.jpg
    """
    return f'track/cover/user_{instance.user.id}/{file}'


def validate_size_image(file_obj):
    """ Проверка размера файла
    """
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла {megabyte_limit}MB")


def delete_old_file(path_file):
    """ Удаление старого файла
    """
    if os.path.exists(path_file):
        os.remove(path_file)
