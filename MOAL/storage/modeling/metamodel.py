u"""https://en.wikipedia.org/wiki/Metadata_modeling.

# Formalized metamodel components:

Generalization
    e.g. "Car" -> "Honda" -> "Accord" -> "DX" -> "1995 Honda Accord DX"
    STANDARD CONCEPT: a concept that contains no further (sub) concepts.
        A standard concept is visualized with a rectangle.
    COMPLEX CONCEPT: a concept that consists of a collection of (sub) concepts.
        Complex concepts are divided into:
        OPEN CONCEPT: a complex concept whose (sub) concepts are expanded.
            An open concept is visualized with two white rectangles above
            each other. (Correction: An open concept is visualized with
            2 white rectangles, 1 overlaid over the other, offset to the right,
            with 3 corners of the rectangle beneath visible. )
        CLOSED CONCEPT: a complex concept whose (sub) concepts are not
            expanded since it is not relevant in the specific context. A closed
            concept is visualized by a white rectangle above a black rectangle.
Association
    some type of association between concepts.
        can have binary, n-ary assoc's.
    e.g. "Honda" <-is a type of-> "Car"
    e.g. "concept a" <-is associated with-> "concept b"
    e.g. "Class" <-describes-> "Object oriented programming construct"
Multiplicity
    number of assoc's a concept can have with another concept
    e.g. "concept a" has 1 assoc. X, 2 assoc. Y with "concept b"
    e.g. "exactly ONE X describes ONE Y"
Aggregation
    special association type.
    Aggregation represents the relation between a concept (as a whole)
        containing other concepts (as parts).
    It can also be described as a 'has-a' relationship.
    e.g. "Car" has-a "engine"
Properties
    Concepts can have arbitrary list of properties
    e.g. "Dog: {color, age, breed, demeanor}"


## Notes

As far as I can tell, a metadata model can be equivalent to an ontology,
particularly one represented like a graph.

There is also strong crossover between these and taxonomies,
but in the broadest sense, you can think of it as a set of data describing
relationships between concepts and the structure of concepts themselves
(via properties).

You could represent this in Python, or other languages
as either a pure data structure (dictionary/hash is probably required to
handle all the possible encoded relationships), or as a set of classes,
following OOP.
"""

meta_concept = {
    'generalization': None,
    'association': None,
    'multiplicity': None,
    'aggregration': None,
    'properties': None
}

concept = {
    'generalization': ['cat'],
    # Associations are 3-tuples with the
    # concept_from, association, and concept_to
    'associations': [
        ('cat', 'is a', 'feline'),
        ('cat', 'is a ', 'vertebrate'),
        ('cat', 'is a', 'carnivore'),
        ('fur', 'is a ', 'feature'),
        ('eyes', 'are a', 'feature'),
        ('color', 'represents', 'visual feature'),
        ('species', 'represents', 'animal classification'),
    ],
    'multiplicity': [
        ('hasEyes', 2),
        ('hasLegs', 4),
    ],
    'aggregation': [
        ('has', 'eyes'),
        ('has', 'fur'),
        ('has', 'claws'),
    ],
    'properties': {
        'fur': None,
        'large_eyes': None,
        'name': None,
        'age': None,
        'lives': None
    },
}

concrete_concept = {
    'generalization': ['tabby'],
    'Associations': [
        ('striped', 'represents', 'fur pattern'),
        ('gray black', 'represents', 'fur color'),
        ('chill', 'describes', 'demeanor'),
    ],
    'aggregation': [],  # Left empty since they are effectively the same here.
    'properties': {
        'fur': 'striped, dots, lines, swirling patterns',
        'large_eyes': True,
        'name': 'Trevor',
        'age': 2,
        'lives': 9
    }
}
