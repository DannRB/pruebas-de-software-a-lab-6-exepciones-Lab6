
import pytest
from Exceptions import ExceptionsDemo, MyException


@pytest.mark.unit
def test_divide_zero():
    demo = ExceptionsDemo()
    with pytest.raises(ZeroDivisionError):
        demo.divide(10, 0)


@pytest.mark.unit
def test_divide_type_error():
    demo = ExceptionsDemo()
    with pytest.raises(TypeError):
        demo.divide('Tamaulipas', 5)


@pytest.mark.unit
@pytest.mark.unit
def test_index_type_error():
    demo = ExceptionsDemo()
    with pytest.raises((TypeError, IndexError)):
        demo.access_list([3, 5, 4], 1)
        demo.access_list([3, 5, 4], 7)
        demo.access_list([3, 5, 4], '5')


@pytest.mark.unit
def test_key_error():
    demo = ExceptionsDemo()
    with pytest.raises(KeyError):
        demo.access_dict(
            {'Manzana': 'Dulce', 'Limon': 'Agrio'},
            'Tomate'
        )


@pytest.mark.unit
def test_FileNotFound_error():
    demo = ExceptionsDemo()
    with pytest.raises(FileNotFoundError):
        demo.read_file('frutas.txt')


@pytest.mark.unit
def test_attribute_error():
    demo = ExceptionsDemo()
    demoFake = ExceptionsDemo()
    with pytest.raises(AttributeError):
        demo.access_attribute(demoFake)


@pytest.mark.wip
def test_my_exception():
    demo = ExceptionsDemo()
    with pytest.raises(MyException):
        demo.check_positive(-3)

