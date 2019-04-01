from ...models import *
import random
from types import SimpleNamespace as SN
from .base import BaseGenerator


class EnglishGenerator(BaseGenerator):

    def gram_tasks(self, lesson):
        return [], []
