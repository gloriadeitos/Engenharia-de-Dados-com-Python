#### Glória Maria Deitos Gomes da Silva <br> 31.Outubro.2024

# Código do Pacote Image Processor

Este arquivo contém o código-fonte do pacote **Image Processor**, que oferece funcionalidades básicas para redimensionamento de imagens e aplicação de filtros.

## Estrutura do Pacote

A estrutura do pacote é a seguinte:

```
image_processor/
│
├── __init__.py
├── filters.py
└── resize.py
```

## Código

### `__init__.py`

Este arquivo inicializa o pacote e importa as funções principais.

```python
from .resize import resize_image
from .filters import apply_filter
```

### `resize.py`

Este módulo contém a função para redimensionamento de imagens.

```python
from PIL import Image

def resize_image(image_path, new_size):
    with Image.open(image_path) as img:
        resized_img = img.resize(new_size)
        return resized_img
```

### `filters.py`

Este módulo contém funções para aplicar filtros em imagens.

```python
from PIL import Image, ImageFilter

def apply_filter(image_path, filter_type):
    with Image.open(image_path) as img:
        if filter_type == 'sepia':
            sepia_img = img.convert('L').convert('RGB')
            return sepia_img
        elif filter_type == 'black_and_white':
            bw_img = img.convert('L')
            return bw_img
        elif filter_type == 'negative':
            negative_img = Image.eval(img, lambda x: 255 - x)
            return negative_img
        else:
            raise ValueError("Filtro não reconhecido.")
```

## Dependências

Certifique-se de ter a biblioteca `Pillow` instalada para manipulação de imagens. Você pode instalá-la usando:

```bash
pip install Pillow
```
