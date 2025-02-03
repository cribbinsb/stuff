import piexif
import piexif.helper

def image_append_exif_comment(image_file, comment):
    """
    Append comment to the end of any existing exif 'usercomment'
    if already exists separate with ';'
    """
    user_comment=""
    try:
        exif_dict = piexif.load(image_file)
    except piexif._exceptions.InvalidImageDataError:
        print(f"image_append_exif_comment: Invalid image {image_file}")
        return False
    try:
        user_comment = piexif.helper.UserComment.load(exif_dict["Exif"][piexif.ExifIFD.UserComment])
    except KeyError:
        pass
    except ValueError:
        pass
    user_comment=user_comment+";"+comment
    exif_dict["Exif"][piexif.ExifIFD.UserComment] = piexif.helper.UserComment.dump(
        user_comment,
        encoding="unicode"
    )
    try:
        piexif.insert(
            piexif.dump(exif_dict),
            image_file
        )
    except Exception as e:
        print(f"image_append_exif_comment: piexif.insert failed file {image_file} exception {e}")
        return False
    return True

def image_get_exif_comment(image_file):
    """
    Get 'usercomment' string exif field from an image.
    Deal with exceptions
    """
    user_comment=""
    try:
        exif_dict = piexif.load(image_file)
    except piexif._exceptions.InvalidImageDataError:
        print(f"image_get_exif_comment: Invalid image {image_file}")
        return ""

    try:
        user_comment = piexif.helper.UserComment.load(exif_dict["Exif"][piexif.ExifIFD.UserComment])
    except KeyError:
        pass
    return user_comment