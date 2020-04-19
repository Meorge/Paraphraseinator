from ppi import Paraphraseinator
import os
from dotenv import load_dotenv

j = """
In the long history of the world, only a few generations have been granted the role of defending freedom in its hour of maximum danger. I do not shrink from this responsibility — I welcome it. I do not believe that any of us would exchange places with any other people or any other generation. The energy, the faith, the devotion which we bring to this endeavour will light our country and all who serve it — and the glow from that fire can truly light the world.

And so, my fellow Americans: ask not what your country can do for you — ask what you can do for your country.
"""

load_dotenv()
KEY = os.getenv('THES_KEY')


p = Paraphraseinator(KEY)
print(p.paraphraseinate(j, 0.9))