from .streams import Processor


class UpperCase(Processor):
    def converter(self, date):
        return date.upper()


if __name__ == '__main__':
    import sys
    obj = UpperCase(open('pizzashop.py'), sys.stdout)
    obj.process()
