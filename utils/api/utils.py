import os , random


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


# برای آپلود عکس و درست کردن آدرسش
# def upload_image_path(instance, filename):
#     new_id = random.randint(1, 999999)
#     name, ext = get_filename_ext(filename)
#     final_name = f"{new_id}-{instance.title}{ext}"
#     return f"gallery/{final_name}"

def upload_image_path(instance, filename):
    return f'public_html/images/image_{instance.id}.{filename.split(".")[-1]}'