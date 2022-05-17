import os


def consumer(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    wrapper.__name__ = func.__name__
    wrapper.__dict__ = func.__dict__
    wrapper.__doc__ = func.__doc__
    return wrapper


def new_image(pagesize):
    pass


def create_thumbnail(image, thumbsize):
    pass


def write_jpeg(image, filename):
    pass


@consumer
def thumbnail_pager(pagesize, thumbsize, destination):
    while True:
        page = new_image(pagesize)
        rows, columns = pagesize / thumbsize
        pending = False

        try:
            for row in range(rows):
                for col in range(columns):
                    thumb = create_thumbnail((yield), thumbsize)
                    page.write(thumb, col*thumbsize.x, row*thumbsize.y)
                    pending = True
        except GeneratorExit:
            if pending:
                destination.send(page)
            destination.close()
            return
        else:
            destination.send(page)


@consumer
def jpeg_writer(dirname):
    fileno = 1

    while True:
        filename = os.path.join(dirname, f'page{fileno:04d}')
        write_jpeg((yield), filename)
        fileno += 1


def write_thumbnails(pagesize, thumbsize, images, output_dir):
    pipeline = thumbnail_pager(
        pagesize, thumbsize, jpeg_writer(output_dir)
    )

    for image in images:
        pipeline.send(image)

    pipeline.close()


if __name__ == '__main__':
    pass