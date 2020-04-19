# Paraphraseinator
We've all been there. You're sitting at your desk at eleven o'clock at night, trying to slam out the last five pages of your English report before the due date at midnight. You think to yourself, "Hey, why I don't just grab something off the internet?" So you find a web page online with *exactly* what you need! But oh no! If you copy and paste that right into your essay and submit it, your professor will accuse you of "plagarising" and drone on about how that that's "bad" and "unethical".

But worry no more! With my latest invention, the **Paraphraseinator**, you can let the computer paraphrase your content for you, making it impossible for your teacher to recognize your information consolidation efforts!

Take, as an example, the famous speech by U.S. President John F. Kennedy:

> In the long history of the world, only a few generations have been granted the role of defending freedom in its hour of maximum danger. I do not shrink from this responsibility — I welcome it. I do not believe that any of us would exchange places with any other people or any other generation. The energy, the faith, the devotion which we bring to this endeavour will light our country and all who serve it — and the glow from that fire can truly light the world.
> 
> And so, my fellow Americans: ask not what your country can do for you — ask what you can do for your country.

Run through the Paraphraseinator with an Originality value of 90%, we get this gem:

> In the lengthy story of the planet, unparalleled a scattering generations have been prima facie the function of justifying self-government in its hour of top danger. I do not fall from this do — I pretty it. I do not believe that every of us would commutation capacities with every other family or each distinguishable generation. The might, the belief, the commitment which we bring to this endeavour will illuminant our rural and all who slave (for) it — and the light from that ardor can indeed cockcrow the world.
> 
> And so, my swain Americans: demand not what your rural can do for you — quiz what you can do for your rustic.

## Requriements
### Python modules
This library uses *[Requests](https://requests.readthedocs.io/en/master/)* for making API requests. In addition, the example scripts use the [`dotenv` module](https://pypi.org/project/python-dotenv/) for storing the API key.

### API key
In order to use the Paraphraseinator, you'll need to get an API key for the [Collegiate Thesaurus API](https://dictionaryapi.com/products/api-collegiate-thesaurus) from the [Merriam-Webster Developer Center](https://dictionaryapi.com). It's quick, it's easy, and it's free.

For the example scripts, you'll need a `.env` file with the following format:
```
THES_KEY=my-api-key
```

**Note**: Merriam-Webster's APIs only allow 1000 calls per day for free. However, the Paraphraseinator saves the information on every word it calls, which means that it will gradually do fewer and fewer calls as more text is run through it. The word information is saved in `cache.json`.

## Command-line tool
I've included a command-line script to easily paraphraseinate text files.
```
python3 ppi_file.py textfile [output [originality]]
```

* `textfile` - Path to text file to paraphraseinate
* `output` - File to output the paraphraseinated text to. If not specified, or written as "None" (without quotation marks), the paraphraseinated text will instead be printed to the console.
* `originality` - A value between 0 and 1 that dictates the probability of any given word being paraphraseinated. Defaults to 0.5 if not specified.

## Example script
```python
from paraphraseinator import Paraphraseinator

# initialize the Paraphraseinator with the Merriam-Webster Collegiate Thesaurus API key
ppi = Paraphraseinator("my-api-key")

# Paraphrase a string with an originality level of 80%
paraphrased = ppi.paraphraseinate("Somebody once told me the world was gonna roll me", originality=0.8)

print(paraphrased)
```

## Bonus `thesaurus` module
To make construction of the Paraphraseinator easier, I created a simple `thesaurus` library to handle communication with Merriam-Webster's API. Check out `ppi.py` for example usage of it. Maybe one day I'll write out more extensive documentation.