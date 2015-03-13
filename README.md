# molecular_weight
_A simple tool to calculate molecular weights as an exploration on using antlr4 grammars with python._

----------------------------

A simple [Antlr4](http://www.antlr.org/) [grammar](https://github.com/edaniszewski/molecular_weight/blob/master/antlr/grammar/molecularWeight.g4) is used with [python](https://theantlrguy.atlassian.net/wiki/display/ANTLR4/Python+Target) to create a simple tool which allows you to calculate the molecular weight of a molecule, given a string that represents that molecule. This project was a means for me to become familiar with how to use antlr4 with python, since I could not find many example resources. The project idea came from a [post](http://www.dalkescientific.com/writings/diary/archive/2007/10/30/antlr_mw.html) which used antlr3 to do essentially the same thing I have done (though with more detail and more completely). Hopefully this may be able to act as a resource for anyone else looking to use python with antlr4.

If you make any modifications to the `molecularWeight.g4` file, in order to generate the correct [python files](https://github.com/edaniszewski/molecular_weight/tree/master/antlr), you should `cd` into the directory containing the `molecularWeight.g4` file and, assuming antlr has already been installed on your machine as per the [instructions on the site](https://theantlrguy.atlassian.net/wiki/display/ANTLR4/Getting+Started+with+ANTLR+v4), run the command:

```
$ java -jar /usr/local/lib/antlr-4.5-complete.jar -Dlanguage=Python2 molecularWeight.g4 
```

This should generate the needed parser, lexer, and listener files in the same directory.

#### Class Descriptions

##### CSVReader ::
The `CSVReader` class is a simple loader written to read in a .csv file from /resources, which contains each element with the associated molecular weight, which I got from [wikipedia](http://en.wikipedia.org/wiki/List_of_elements). It reads the data into a dictionary where the key is the atom symbol, and the value is the atomic weight.

##### Listener ::
An implementation of the generated `molecularWeightListener`. The only overriden method is `enterElements()`, since I have chosen this point to be the point where I calculate the weight of the element. If more actions were desired, `exitElements()`, `enterMolecule()`, or `exitMolecule()` may also be overriden.

##### MolecularWeight ::
A simple method to parse a given molecule string and pass it through to the antlr parser then extract the calculated total weight. The important part here is found in the `_parse_molecule()` method, as it shows how to pass some input to the parser:

```python
input_stream = InputStream(molecule)
lexer = molecularWeightLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = molecularWeightParser(stream)
return parser.molecule()
```

Most examples I came across showed how to pass data in from a file or as a command line argument, but not from some variable or input parameter, so if anything else, this example may be useful in this front.

#### Usage
Being such a simple example, there is not much to say in terms of usage. To properly instantiate the `MolecularWeight` class, it must be passed a dictionary of key: atomic symbol, value: atomic weight. This can be done by reading in the provided .csv file and using the created dictionary (see /test/test.py)

```python
reader = CSVReader('/resources/element_weights.csv')
reader.read()
mw = MolecularWeight(reader.data)
```

To calculate a weight, simple call the `process()` method

```python
> mw.process("H2O")

18.015
```

#### Future Work
Exception handling needs to be incorporated, and this could probably be extended in many ways (from allowing different means of data import, to handling certain edge cases, to better validation of results, etc.). My experience level with antlr4 is still novice, so there may be a way to simplify the implemented python logic within the antlr grammar, or maybe not. If you have any thoughts, suggestions, or comments, feel free to share!
