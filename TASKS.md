# Introduction

####*...An autodidacts dream*

**This should be considered a living document. It will grow in size, becoming better organized as new details and fields of study are integrated**

_Note:_ *completed tasks are [linked](#)*. Tasks are generally structured to be individual and atomic, but many build off of each other and are imported as new modules. Each file is formatted to have classes/definitions and then examples below. Each task and child task/category is designed to be as true to the hierarchy of understanding as possible; duplicate labels are thus removed for child elements, so that relationships are derived by simply mentally "traversing the tree", to build out the specific name.

# Tasks

## Data structures / types

+ [Persistent](MOAL/data_structures/persistent.py)
  + [Partial](MOAL/data_structures/persistent.py)
      + [Fat node](MOAL/data_structures/persistent.py)
      + Path copying
      + Fat / path combination
  + [Full](MOAL/data_structures/persistent.py)
  + [Confluent](MOAL/data_structures/persistent.py)
+ Succinct
+ [Retroactive](MOAL/data_structures/retroactive.py)
  + [Partial](MOAL/data_structures/retroactive.py)
  + [Full](MOAL/data_structures/retroactive.py)
+ [Abstract data types](MOAL/data_structures/abstract/)
  + [Arrays](MOAL/data_structures/abstract/array_and_linked_lists.py)
  + [Container](MOAL/data_structures/abstract/container.py)
  + [Map / Associative array / Dictionary](MOAL/data_structures/abstract/map.py)
  + [Multi-map](MOAL/data_structures/abstract/map.py)
  + [List](MOAL/data_structures/abstract/list.py)
  + [Set](MOAL/data_structures/abstract/set.py)
    + [Static](MOAL/data_structures/abstract/set.py)
    + [Dynamic](MOAL/data_structures/abstract/set.py)
  + [Multi-set / Bag](MOAL/data_structures/abstract/set.py)
  + [Queue](MOAL/data_structures/abstract/queues.py)
    + [Using stdlib](MOAL/data_structures/abstract/queues_stdlib.py)
    + [Double-ended queue](MOAL/data_structures/abstract/queues.py)
    + [Priority queue](MOAL/data_structures/abstract/priority_queue.py)
  + [Stacks](MOAL/data_structures/abstract/stack.py)
    + [Stack frames](MOAL/data_structures/abstract/stack_frame.py)
  + [String](MOAL/data_structures/abstract/string_adt.py)
  + [Tree](MOAL/data_structures/abstract/tree.py)
  + [Stream](MOAL/data_structures/abstract/stream.py)
  + [Graph](MOAL/data_structures/graphs/graphs.py)
+ Linear
  + [Arrays](MOAL/data_structures/abstract/array_and_linked_lists.py)
    + [Linear octree](MOAL/data_structures/linear/array/linear_trees.py)
    + [Linear quadtree](MOAL/data_structures/linear/array/linear_trees.py)
    + [Overloaded arrays](MOAL/helpers/adts.py)
    + [Suffix arrays](MOAL/data_structures/linear/array/suffix_arrays.py)
      + Compressed suffix array
    + [Bi-directional map](MOAL/data_structures/abstract/map.py)
    + [Bit](MOAL/computer_organization/data_types.py)
    + [Bit field](MOAL/computer_organization/bit_field.py)
    + [Bit vector](MOAL/computer_organization/bit_field.py)
    + [Bit Array](MOAL/data_structures/linear/bitarray)
      + [Bitboard](MOAL/data_structures/linear/bitarray/bitboard.py)
      + [Bitmap](MOAL/data_structures/linear/bitarray/bitboard.py)
    + [Circular buffer](MOAL/data_structures/linear/array/circular_buffer.py)
    + [Control table](MOAL/data_structures/linear/array/control_table.py)
    + [Image](MOAL/data_structures/linear/array/image_array.py)
    + [Dynamic](MOAL/data_structures/abstract/array_and_linked_lists.py)
    + Gap buffer
    + [Hashed array tree](MOAL/data_structures/linear/array/hashed_array_tree.py)
    + [Lookup table](MOAL/maths/applied/optimization/memoization.py)
    + [Branch table](MOAL/automata_theory/counter_machine.py)
    + [Vector](MOAL/data_structures/abstract/array_and_linked_lists.py)
    + [Matrix](MOAL/data_structures/abstract/array_and_linked_lists.py)
    + [Parallel](MOAL/data_structures/abstract/array_and_linked_lists.py)
    + [Sorted](MOAL/data_structures/abstract/array_and_linked_lists.py)
    + [Sparse](MOAL/data_structures/linear/array/sparse.py)
    + [Sparse matrix](MOAL/data_structures/linear/array/sparse.py)
    + Iliffe vector
      * Jagged array
      * Triangular array
      * Triangular matrix
    + Dope vector
    + [Variable-length](MOAL/data_structures/abstract/array_and_linked_lists.py)
  + Lists
    + [Array list](MOAL/data_structures/abstract/array_and_linked_lists.py)
    + [Linked](MOAL/data_structures/abstract/array_and_linked_lists.py)
      + [Doubly linked](MOAL/data_structures/abstract/array_and_linked_lists.py)
      + [Association list](MOAL/data_structures/abstract/array_and_linked_lists.py)
    + Self-organizing
    + [Skip lists](MOAL/data_structures/linear/lists/skip_lists.py)
    + Unrolled linked
    + VList
    + Xor linked
    + Zipper
    + Doubly connected edge
    + Difference
    + [Free](MOAL/data_structures/linear/lists/free_list.py)
+ Hashes
  + Bloom filter
  + Count-Min sketch
  + Distributed hash table
  + Double Hashing
  + Dynamic perfect hash table
  + Hash array mapped trie (HAMT)
  + [Hash list](MOAL/data_structures/hashes/hash_list.py)
  + [Hash table](MOAL/data_structures/hashes/hashtable.py)
  + Hash trie
  + Koorde
  + Prefix hash tree
  + [Rolling hash](MOAL/data_structures/hashes/rolling_hash.py)
  + MinHash
  + Quotient filter
+ Trees
  + [Hash tree](MOAL/data_structures/trees/)
    + [Merkle tree](MOAL/data_structures/trees/merkle_tree.py)
    + [Tiger Tree Hash](MOAL/data_structures/trees/merkle_tree.py)
  + [Binary](MOAL/data_structures/trees/binary_trees.py)
    + AA
    + [AVL](MOAL/data_structures/trees/avl_trees.py)
    + [Binary search](MOAL/data_structures/trees/binary_search_trees.py)
      * Randomized binary search
      * Self-balancing binary search
    + [Binary](MOAL/data_structures/trees/binary_trees.py)
    + [Cartesian](MOAL/data_structures/trees/cartesian_trees.py)
    + [Order statistic](MOAL/data_structures/trees/order_statistic_bst.py)
    + Pagoda
    + Red-black
    + Rope
    + Scapegoat
    + [Splay](MOAL/data_structures/trees/splay_trees.py)
    + T-tree
    + Tango
    + Threaded binary
    + Top
    + [Treap](MOAL/data_structures/trees/cartesian_trees.py)
    + Weight-balanced
    + Binary data structure
    + Stern–Brocot (mathematical)
  + B
    + B
    + B+
    + B*
    + B sharp
    + Dancing
    + 2-3
    + 2-3-4
    + Queap
    + Fusion
    + Bx
    + AList
  + [Heaps](MOAL/data_structures/trees/heaps.py)
    + [Binary](MOAL/data_structures/trees/heaps.py)
    + Weak
    + Binomial
    + Fibonacci
      + AF
    + Leonardo
    + 2-3
    + Soft
    + Pairing
    + Leftist
    + Beap
    + Skew
    + Ternary
    + D-ary
    + Brodal queue
  + Fractal
  + Interval tree
  + Binary indexed tree
  + vEB tree
  + Red-black tree
  + [Trie](MOAL/data_structures/trees/trie.py)
    + Radix tree
    + [Suffix tree](MOAL/data_structures/trees/suffix_tree.py)
      + [Generalized](MOAL/data_structures/trees/suffix_tree.py)
      + Ukkonen's
      + McCreight's
    + FM-index
    + B-trie
    + Judy array
    + X-fast
    + Y-fast
    + Concurrent trie (Ctrie)
  + Space-partitioning
    + Segment
    + Interval
    + Range
    + Bin
    + Kd-tree
      * Implicit kd-tree
      * Min/max kd-tree
      * Adaptive k-d
    + [Quad](MOAL/data_structures/abstract/tree.py)
    + [Octree](MOAL/data_structures/abstract/tree.py)
    + Z-order
    + UB
    + R
      * R+
      * R*
      * Hilbert R
    + X
    + Metric
    + Cover
    + M
    + VP
    + BK
    + Bounding interval hierarchy
    + BSP
      + K-dimensional tree
    + Rapidly exploring random
  + Multiway
    + Ternary
    + K-ary
    + And–or
    + (a,b)
    + Link/cut
    + SPQR
    + Spaghetti stack
    + Disjoint-set / union-find / merge-find ADT
    + Fusion
    + Enfilade
    + Exponential
    + Fenwick
    + Van Emde Boas
    + Rose
  + Application specific
    + [Abstract syntax](MOAL/execution/compiler/abstract_syntax_tree.py)
    + Parse
    + Decision
    + Alternating decision
    + Minimax
    + Expectiminimax
    + Finger
    + Bounding volume hierarchy
    + Expression
    + Log-structured merge
    + AHO tree (for AHO algorithm)
+ [Graph](MOAL/data_structures/graphs/graphs.py)
  + [Adjacency list](MOAL/data_structures/graphs/adjacency_list.py)
  + [Adjacency matrix](MOAL/data_structures/graphs/adjacency_matrix.py)
  + [Incidence matrix](MOAL/data_structures/graphs/incidence_matrix.py)
  + [Graph-structured stack](MOAL/data_structures/graphs/graph_structured_stack.py)
  + [Scene](MOAL/data_structures/graphs/scene_graph.py)
  + [Binary decision diagram](MOAL/data_structures/graphs/binary_decision_diagram.py)
  + Zero-suppressed decision diagram
  + [Directed](MOAL/data_structures/graphs/graphs.py)
    + DAWG/DAFSA
      + Sparse
      + Compacted
    + [Acyclic](MOAL/data_structures/graphs/graphs.py)
      + [Propositional](MOAL/data_structures/graphs/binary_decision_diagram.py)
      + And-inverter
  + [Multigraph](MOAL/data_structures/graphs/multigraph.py)
  + [Hypergraph](MOAL/data_structures/graphs/hypergraph.py)
+ Other
  + [Heightmap](MOAL/data_structures/other/heightmap.py)
  + [Lightmap](MOAL/data_structures/other/lightmap.py)
  + Winged edge
  + Quad-edge
  + [Routing table](MOAL/data_structures/other/routing_table.py)
  + [Symbol table](MOAL/data_structures/other/symbol_table.py)

## Software Engineering / Software Development

+ Requirements analysis
+ Reification
+ Debugging
+ Development
  + Methodologies
    + Test driven (TDD)
      + [Creating test matrices](MOAL/helpers/tests/test_adts.py)
      + [Testing libraries](MOAL/helpers/tests/test_adts.py)
        + [Nose](MOAL/helpers/tests/test_adts.py)
    + Behavior driven (BDD)
    + Model driven (MDD)
      + Model transformation
    + Feature driven (FDD)
    + Domain driven (DDD)
+ Testing
  + Black box
    + [Decision table](MOAL/software_engineering/testing/black_box/decision_table.py)
    + [All-pairs/orthogonal array](MOAL/software_engineering/testing/black_box/allpairs.py)
    + [State transition analysis](MOAL/execution/virtual_machine/process_vm.py)
    + [Equivalence partitioning](MOAL/software_engineering/testing/black_box/equivalence_partitioning.py)
    + Boundary value analysis
    + Cause-effect graph
    + [Error guessing](MOAL/software_engineering/testing/black_box/error_guessing.py)
  + White box
    + API testing
    + [Code coverage](MOAL/test_files.py)
    + [Fault injection](MOAL/software_engineering/testing/black_box/fault_injection.py)
    + [Mutation testing](MOAL/helpers/tests/test_adts.py)
    + Static analysis
      + Shape analysis
      + Effect systems
      + Control-flow graph (CFG)
      + Model checking
        + TuLiP
      + Static program analysis
        + Pylint
      + Data-flow analysis
      + Hoare logic
        * Communicating sequential processes (CSP)
      + Type checking
      + Type inference
      + Symbolic simulation
      + Symbolic execution
      + Abstract interpretation
        + Sound
        + Unsound
  + Gray box
    + /TBD/
+ Deployment
  * Docker
+ Formal verification
  + Theorem provers
    + Automated
  + Verified computation
  + Process-calculus
+ Refactoring
  + Martin Fowler refactoring.com patterns
+ Problem solving
  * Design patterns
    - Unix Rules
      + Rule of modularity
      + Rule of Clarity
      + Rule of Composition
      + Rule of Separation
      + Rule of Simplicity
      + Rule of Parsimony
      + Rule of Transparency
      + Rule of Robustness
      + Rule of Representation
      + Rule of Least Surprise
      + Rule of Silence
      + Rule of Repair
      + Rule of Economy
      + Rule of Generation
      + Rule of Optimization
      + Rule of Diversity
      + Rule of Extensibility
    + SOLID
      * Single Responsibility
      * Open/Closed
      * Liskov Substitution
      * Interface segregation
      * Dependency Inversion
    + [GRASP](MOAL/software_engineering/problem_solving/design_patterns/grasp)
      * [Controller](MOAL/software_engineering/problem_solving/design_patterns/grasp/pattern_controller.py)
      * [Creator](MOAL/software_engineering/problem_solving/design_patterns/grasp/pattern_creator.py)
      * [Indirection](MOAL/software_engineering/problem_solving/design_patterns/grasp/pattern_indirection.py)
      * [Information Expert](MOAL/software_engineering/problem_solving/design_patterns/grasp/pattern_infohiding.py)
      * [High Cohesion](MOAL/software_engineering/problem_solving/design_patterns/grasp/pattern_cohesion.py)
        - [Coincidental (worst)](MOAL/software_engineering/problem_solving/design_patterns/grasp/pattern_cohesion.py)
        - [Logical](MOAL/software_engineering/problem_solving/design_patterns/grasp/pattern_cohesion.py)
        - [Temporal](MOAL/software_engineering/problem_solving/design_patterns/grasp/pattern_cohesion.py)
        - [Procedural](MOAL/software_engineering/problem_solving/design_patterns/grasp/pattern_cohesion.py)
        - [Communicational/informational](MOAL/software_engineering/problem_solving/design_patterns/grasp/pattern_cohesion.py)
        - [Sequential](MOAL/software_engineering/problem_solving/design_patterns/grasp/pattern_cohesion.py)
        - [Functional (best)](MOAL/software_engineering/problem_solving/design_patterns/grasp/pattern_cohesion.py)
      * [Low/loose Coupling](MOAL/software_engineering/problem_solving/design_patterns/grasp/pattern_cohesion.py)
      * [Polymorphism](MOAL/software_engineering/problem_solving/design_patterns/grasp/pattern_polymorphism.py)
      * [Protected Variations](MOAL/software_engineering/problem_solving/design_patterns/grasp/pattern_protected_variation.py)
      * [Pure Fabrication](MOAL/software_engineering/problem_solving/design_patterns/grasp/pattern_pure_fabrication.py)
  + Decomposition

## Mathematics

+ Quantity
  + Numbers
    + [Natural](MOAL/maths/numbers/basic.py)
      + [Transfinite](MOAL/maths/set_theory.py)
    + [Integers](MOAL/maths/numbers/basic.py)
    + [Rational](MOAL/maths/numbers/basic.py)
    + [Irrational](MOAL/maths/numbers/basic.py)
    + [Real](MOAL/maths/numbers/basic.py)
    + Imaginary
    + Complex
    + Quaternions
    + Octonions
    + [Cardinals](MOAL/maths/set_theory.py)
+ Structure
  + [Combinatorics](MOAL/maths/combinatorics/basic.py)
  + [Number theory](MOAL/maths/number_theory.py)
  + Group theory
  + [Category theory](MOAL/maths/category_theory/cat_basics.py)
    * Sympy
  + Graph theory
    + Spectral graph theory
    + Euler graph
    + Hamiltonian graph
  + Order theory
  + Representation theory
  + Algebra
+ Space
  + Geometry
  + Trigonometry
  + Differential geometry
  + Topology
  + Fractal geometry
  + Measure theory
+ Change
  + Calculus
  + Vector calculus
  + Differential equations
  + Dynamical systems
  + Chaos theory
  + Complex analysis
+ Applied
  + Computational
    + Geometry
    + Mathematical physics
    + Fluid dynamics
    + Numerical analysis
      + Asymptotic notation
        + [Big O](MOAL/maths/big_o.py)
          + [O(1)](MOAL/maths/big_o.py)
          + [O(logN)](MOAL/maths/big_o.py)
          + [O(n)](MOAL/maths/big_o.py)
          + [O(n logN)](MOAL/maths/big_o.py)
          + [O(n^2)](MOAL/maths/big_o.py)
          + [O(2^n)](MOAL/maths/big_o.py)
          + [O(n!)](MOAL/maths/big_o.py)
    + Optimization
      + [Memoization](MOAL/maths/applied/optimization/memoization.py)
      + Strength reduction
      + Caching
      + Linear programming
        + Augmented form
        + Duality
    + Probability theory
    + [Statistics](MOAL/maths/probability.py)
      + [Probability](MOAL/maths/probability.py)
    + [Cryptography](MOAL/maths/applied/computational/cryptography)
      + Zero-knowledge proofs
      + [Ciphers](MOAL/maths/applied/computational/cryptography/ciphers)
        + Historical
          + Substitution
            + [ROT13](MOAL/maths/applied/computational/cryptography/ciphers/historical/substitution/rot13.py)
          + [Transposition](MOAL/maths/applied/computational/cryptography/ciphers/historical/transposition)
            + [Rail fence](MOAL/maths/applied/computational/cryptography/ciphers/historical/transposition/railfence.py)
        + Modern
          + Key type
            + Symmetric
            + Asymmetric
          + Input type
            + Block
              * GOST
            + Stream
    + Modeling
      + Finance
      + Biology
      + Chemistry
      + Economics
+ Discrete
  + Game theory
  + Control theory
  + Decision theory
  + Utility theory
  + Social choice theory
  + Logic
    + [Set theory](MOAL/maths/set_theory.py)
      + Axiomatic
      + Combinatorial
      + Descriptive
      + Fuzzy
      + Inner model
      + Large cardinal
      + Determinacy
      + Forcing
      + Cardinal invariants
      + Set-theoretic topology
      + Three-valued (trivalent / trinary)
    + Model theory
      + Classical
      + Applied to groups and fields
      + Geometric
      + Finite
      + Infinite
    + Recursion theory / Computability theory
      + Lambda calculus
      + Kahn process networks
    + Proof theory
      + Hilbert system
    + First-order
    + Predicate
    + Computational
    + Modal
    + Algebraic

## Algorithms

+ Automata
    + Powerset construction
    + Todd-Coxeter
+ Artificial intelligence
    + Alpha-beta
    + Ant-algorithms
    + Cortical Learning Algorithm
    + Differential evolution
+ Computer vision
    + Epitome
    + Counting objects in an image
        + connected-component labeling
    + Deep Dense Face Detector
    + Evolution-Constructed Features
    + O'Carroll
    + Tracking-Learning Detection
    + Viola-Jones object detection framework
+ Cryptography
    + Private key (symmetric)
        + Advanced Encryption Standard / Rijndael
        + Blowfish
        + Data Encryption Standard (DES)
        + IDEA / IPES / PES
        + RC4 or ARC4
        + Tiny Encryption Algorithm
    + Public key (asymmetric)
        + DSA
        + ElGamal
        + RSA
        + Diffie-Hellman / Merkle
        + NTRUEncrypt
    + Message digest functions
        + [MD5](MOAL/algorithms/cryptography/digest/message_digest.py)
        + [RIPEMD](MOAL/algorithms/cryptography/digest/message_digest.py)
        + [SHA-1](MOAL/algorithms/cryptography/digest/message_digest.py)
        + [HMAC](MOAL/algorithms/cryptography/digest/message_digest.py)
        + [Tiger (TTH)](MOAL/algorithms/cryptography/digest/message_digest.py)
    + Techniques
        + Shamir's secret sharing scheme
        + Blakley's secret sharing scheme
    + Other techniques and decryption
        + Subset sum
        + Shor's
+ Genetic algorithms
    + Fitness proportionate selection (aka roulette-wheel selection)
    + Truncation selection
    + Tournament selection
    + Stochastic universal sampling
+ Machine learning
    + PAVA (Pool-Adjacent-Violators Algorithm)
    + Multiplicative Weights
+ Bioinformatics and Cheminformatics
    + Needleman-Wunsch
    + Smith-Waterman
    + Ullmann's
+ Compression
    + Lossless
        + Burrows-Wheeler transform
        + Deflate
        + Delta encoding
        + Incremental encoding
        + LZW. (Lempel-Ziv-Welch)
        + LZ77 and 78
        + Lempel-Ziv-Markov chain
        + LZO
        + Prediction by Partial Matching
        + Shannon-Fano coding
        + Truncated binary
        + Run-length encoding
        + Sequitur
        + EZW (Embedded Zerotree Wavelet)
        + Entropy encoding
        + Huffman coding
            + Adaptive
        + Arithmetic coding
        + Range encoding
        + Unary coding
        + Elias delta, gamma, omega coding
        + Fibonacci coding
        + Golomb coding
        + Rice coding
    + Lossy
        + Linear predictive coding
        + A-law algorithm
        + Mu-law algorithm
        + Fractal compression
        + Transform coding
        + Vector quantization
        + Wavelet compression
+ Graphics
    + Bresenham's line
    + Colorization
    + Depixelizing Pixel Art
    + DDA line
    + Flood fill
    + HDR
        + /TBD/
    + Xiaolin Wu's line
    + Painter's
    + Ray tracing
    + Phong shading
    + Gouraud shading
    + Scanline rendering
    + Global illumination
    + Interpolation
    + Resynthesizer
    + Slope-intercept
    + Spline interpolation
    + 3D Surface Tracker Technology
+ Geometry
    + Gift wrapping
    + Gilbert-Johnson-Keerthi distance
    + Graham scan
    + Line segment intersection
    + Point in polygon
    + Ray/Plane intersection
        + Line/Triangle intersection
    + Polygonization of implicit surfaces
    + Triangulation
+ Mathematics
    + Algebra
        + Buchberger's
        + Extended Euclidean
        + Fourier transform multiplication
        + Gram-Schmidt process
        + Gauss-Jordan elimination
        + Karatsuba multiplication
        + Knuth-Bendix completion
        + Multivariate division
        + Risch
        + Toom-Cook (Toom3)
        + Eigenvalue algorithm
            + R algorithm
            * Inverse iteration
            * Lanczos iteration
            * Arnoldi iteration
            * Rayleigh quotient iteration
            * Jacobi method
            * Bisection
            * Divide-and-conquer
            * Eigenvector algorithms
            * Richardson eigenvector algorithm.
            * Max-Plus
            * Abrams and Lloyd eigenvector
        Arithmetic
        + Binary GCD
        + Booth's multiplication
        + Euclidean algorithm
        + Binary multiplication (Peasant or Egyptian multiplication)
    + Discrete logarithm in group theory
        + Baby-step giant-step
        + Pollard's rho algorithm for logarithms
        + Pohlig-Hellman
        + Index calculus algorithm
+ Integer factorization
    + Prime factorization
        + Fermat's factorization method
        + Trial division
        + Lenstra elliptic curve factorization / ECM
        + Pollard's rho
        + Pollard's p-1
        + Congruence of squares
        + Quadratic sieve
        + Dixon's factorization method
        + Special number field sieve
        + General number field sieve (GNS)
+ Merging
    + [Simple Merge](MOAL/algorithms/sorting/merge_sort.py)
    + k-way Merge
+ Logic programming
    + Davis–Putnam
+ Matrix processing
    + [Exponentiating by squaring](MOAL/algorithms/matrix_processing/matrix_processing.py)
    + Rutishauser
    + Strassen
    + Symbolic Cholesky decomposition
    + Zha's algorithm
    + Matrix chain multiplication
+ Optic
    + Gerchberg Saxton
+ Texts
    + Searching
        + Aho-Corasick
        + Bitap (or shift-or, shift-and, Baeza-Yates-Gonnet)
        + Boyer-Moore-Horspool
        + Apostolico-Giancarlo
        + Burrows Wheeler transform
        + Knuth-Morris-Pratt
        + Rabin-Karp
        + Longest common subsequence problem
        + Longest increasing subsequence problem
        + Shortest common supersequence
        + Horspool
    + Approximate matching
        + [Hamming distance](MOAL/algorithms/coding_theory/hamming_distance.py)
        + [Levenshtein distance](MOAL/algorithms/coding_theory/levenshtein_distance.py)
        +     Damerau–Levenshtein distance
        + Soundex
        + Metaphone
        + NYSIIS
    + Word processing
        + Latent Dirichlet Allocation
        + Latent Semantic Indexing
        + Stemming
+ Utilities
    + Doomsday
    + Xor swap
    + Hamming weight
    + Luhn
    + Create bit mask
+ Misc.
    + BrowseRank
    + Hypertext Induced Topic Selection (HITS, patent in 1997)
    + Growth-Algorithm Model of Leaf Shape
    + PageRank
    + Schreier-Sims
    + Robinson-Schensted
+ Coding theory
  + String edit
    + Jaro–Winkler distance
    + Lee distance
    + MostFreqKDistance
    + MinHash
    + Longest common subsequence
      + Hunt–McIlroy
    + Longest common substring
    + Longest palindromic substring
+ Operating systems
    + Mutual exclusion management
    + Szymanski's
    + Taubenfeld's black-white bakery
    + Banker
    + Page replacement
    + Bully
    + Disk scheduling
    + Elevator
    + Shortest seek first
    + Process synchronization
    + Peterson
    + Lamport's Bakery
    + Dekker
    + Scheduling algorithms
    + Earliest deadline first scheduling
    + Fair-share scheduling
    + Least slack time scheduling / Least Laxity First
    + List scheduling
    + critical path
    + longest path
    + highest level first
    + longest processing time
    + Multi level feedback queue
    + Rate-monotonic scheduling
    + Round-Robin scheduling
    + Shortest job next (or first)
    + Shortest remaining time
+ (Pseudo) Random number generators
    + Blum Blum Shub
    + Mersenne twister
    + Lagged Fibonacci generator
    + Linear congruential generator
    + Yarrow
    + Fortuna
    + Linear feedback shift register
+ Astronomy
    + Ephemerides
    + Julian day
    + Julian date
+ Signal processing
    + CORDIC
    + Rainflow-counting
    + OSEM
    + Goertzel algorithm
    + Discrete Fourier transform
    + Fast Fourier transform
      * Cooley-Tukey
      * Rader's
      * Bluestein's
      * Bruun's
      * Prime-factor
    + Richardson-Lucy deconvolution
    + Elser Difference-Map
    + Shazam
+ Software engineering
    + Unicode Collation
    + CHS conversion
    + Cyclic redundancy check
    + Parity control
+ Memory allocation
    + Boehm garbage collector
    + Buddy memory allocation
    + Generational garbage collector
    + Mark and sweep
    + Reference counting
+ Distributed systems
    + Lamport ordering
    + Snapshot
    + Vector clocks
    + Marzullo
    + Intersection
+ Optimization
    + Almost Linear Max Flow
    + Ant colony optimization
    + BFGS (Broyden-Fletcher-Goldfarb-Shanno method)
    + Branch and bound
    + Conjugate gradient method
    + Evolution strategy
    + Gauss-Newton
    + Gradient descent
    + Levenberg-Marquardt
    + Line search
    + Local search
    + Nelder-Mead method (downhill simplex method)
    + Newton's method in optimization
    + Paxos
    + PSO, Particle swarm optimization
    + Random-restart hill climbing
    + Simplex
    + Simulated annealing
    + Stochastic tunneling
    + Tabu search
    + Trust search
+ Parsing
    + Cocke–Younger–Kasami
    + Earley
    + Forward–backward
    + Conditional Inside
    + Inside-outside
    + LL Parsers
    + ANTLR
    + LR Parsers
    + Dijkstra's shunting yard
    + LALR (Look-ahead LR)
    + SLR (Simple LR) parser
    + Canonical LR parser or LR(1) parser
    + GLR. (Generalized LR parser)
    + Recursive Descent Parsers
    + Packrat parser
+ Prediction
    + Baum-Welch
    + Viterbi
+ Quantum
    + Grover's
    + Shor's
    + Deutsch-Jozsa
+ Distributed Networking
  + Koorde
  + Chord
+ Lists, arrays and trees
    + Breadth-first search
    + Best-first search
    + [Depth-first search](MOAL/data_structures/graphs/graphs.py)
    + Dictionary search
    + Disjoint-set data structure and algorithm
    + Interpolated search / predictive search
    + Median search
    + Selection algorithm
    + Uniform-cost search
+ Prime test
    + AKS (Agrawal-Kayal-Saxena)
    + Fermat
    + Miller-Rabin
    + Spigot
    + Sieve of Eratosthenes
    + Sieve of Atkin
    + Solovay-Strassen
+ Numerical
    + [Fibonacci sequence](MOAL/maths/number_theory.py)
    + Biconjugate gradient method
    + Dancing Links
    + De Boor
    + De Casteljau's
    + False position method
    + Gauss-Legendre
    + Kahan summation
    + MISER
    + Newton's method
    + Secant method
    + Shifting nth-root
    + Square root
    + Borwein's
    + Metropolis-Hastings
+ Sorting
    + Binary tree sort
    + Bucket sort
    + Cocktail sort (bidirectional bubble, shaker, ripple, shuttle, happy hour)
    + Comb sort
    + Counting sort
    + Gnome sort
    + Introsort
    + Pancake sort
    + Pigeonhole sort
    + Postman sort
    + Smoothsort
    + Stochastic
    - [Insertion sort](MOAL/algorithms/sorting/insertion_sort.py)
    - [Merge sort](MOAL/algorithms/sorting/merge_sort.py)
    - [Quick sort](MOAL/algorithms/sorting/quick_sort.py)
    - Splay sort
    - Heap sort
    - Radix sort
      - MSD
      - Adaptive
      - MBM
      - Forward
    - [Bubble Sort](MOAL/algorithms/sorting/bubble_sort.py)
    - [Bogo Sort (anti-pattern)](MOAL/algorithms/sorting/bogo_sort.py)
    - Burst sort
    - [Selection Sort](MOAL/algorithms/sorting/selection_sort.py)
    - [Shell Sort](MOAL/algorithms/sorting/shell_sort.py)
+ Approximation
+ Greedy
+ Dynamic programming
+ Divide & conquer
+ Time series analysis
  + Dynamic time warping
+ Geometry
  + Manhattan distance
  + Euclidean distance
+ Graph traversal
  + Shortest Path Problems
  + Dijkstra's Algorithm
  + Knight's Tour Problem
  + The Word Ladder Problem
  + Prim's Spanning Tree Algorithm
  + Building the Word Ladder Graph
  + Topological Sorting
  + Strongly Connected Components
  + A* tree search
  + 3D Surface Tracker Technolog
  + Bellman-Ford
  + Graph canonization
  + Perturbation methods
  + Floyd-Warshall
  + Floyd's cycle-finding
  + Johnson
  + Hopcroft–Karp algorithm
  + Kruskal
  + Boruvka
  + Ford-Fulkerson
  + Edmonds-Karp
  + Nonblocking Minimal Spanning Switch
  + Woodhouse-Sharp
  + Spring based
  + Hungarian
  + Coloring
  + Nearest neighbor
  + Tarjan's off-line least common ancestors

## Computer Organization

Note: some encoding schemes are not really used in computer organization, but are grouped as such because there is some crossover. In most cases, many of the numeral systems below can be seen as simply pure mathematical notation in the context of a writing system.

+ Transistors
+ Logic gates
+ [Data-types & representation](MOAL/computer_organization/data_types.py)
  + [Bit](MOAL/computer_organization/data_types.py)
  + [Nibble](MOAL/computer_organization/data_types.py)
  + [Byte](MOAL/computer_organization/data_types.py)
  + [Octet](MOAL/computer_organization/data_types.py)
  + [*byte](MOAL/computer_organization/data_types.py)
  + [Two's complement](MOAL/computer_organization/one_twos_complement.py)
  + [Ones' complement](MOAL/computer_organization/one_twos_complement.py)
+ [Numerical encoding](MOAL/computer_organization/numerical_encoding_basic.py)
  + [N-ary](MOAL/computer_organization/positional.py)
    + [Binary](MOAL/computer_organization/numerical_encoding_basic.py)
       + [Binary coded decimal (BCD)](MOAL/computer_organization/bcd.py)
        + [8421](MOAL/computer_organization/bcd.py)
        + 4221
        + 7421
        + [excess-3](MOAL/computer_organization/bcd.py)
        + Telephony (TCBD)
    + Bi-Quinary
    + [Ternary](MOAL/computer_organization/positional.py)
      + Balanced ternary
    + [Quaternary](MOAL/computer_organization/positional.py)
    + [Quinary](MOAL/computer_organization/positional.py)
    + [Senary](MOAL/computer_organization/positional.py)
    + [Septenary](MOAL/computer_organization/positional.py)
    + [Octal](MOAL/computer_organization/numerical_encoding_basic.py)
    + [Nonary](MOAL/computer_organization/positional.py)
    + [Decimal](MOAL/computer_organization/numerical_encoding_basic.py)
    + [Undecimal](MOAL/computer_organization/positional.py)
    + [Duodecimal](MOAL/computer_organization/positional.py)
    + [Tridecimal](MOAL/computer_organization/positional.py)
    + [Tetradecimal](MOAL/computer_organization/positional.py)
    + [Pentadecimal](MOAL/computer_organization/positional.py)
    + [[Hexadecimal](MOAL/computer_organization/positional.py)](MOAL/computer_organization/numerical_encoding_basic.py)
    + [Octodecimal](MOAL/computer_organization/positional.py)
    + [Vigesimal](MOAL/computer_organization/positional.py)
    + [Tetravigesimal](MOAL/computer_organization/positional.py)
    + [Pentavigesimal](MOAL/computer_organization/positional.py)
    + [Hexavigesimal](MOAL/computer_organization/positional.py)
    + [Septemvigesimal](MOAL/computer_organization/positional.py)
    + [Trigesimal](MOAL/computer_organization/positional.py)
    + [Duotrigesimal](MOAL/computer_organization/positional.py)
    + [Hexatrigesimal](MOAL/computer_organization/positional.py)
    + [Sexagesimal](MOAL/computer_organization/positional.py)
    + [Duosexagesimal](MOAL/computer_organization/positional.py)
    + [Tetrasexagesimal](MOAL/computer_organization/positional.py)
    + [Pentaoctagesimal](MOAL/computer_organization/positional.py)
    + [Centovigesimal](MOAL/computer_organization/positional.py)
    + [Duocentoquadragesimal](MOAL/computer_organization/positional.py)
    + [Trecentosexagesimal](MOAL/computer_organization/positional.py)
    + [Custom](MOAL/computer_organization/positional.py)
  + Complex
    + Quater-Imaginary base
    + Twindragon
  + Non-integer bases
    + Golden ratio
    + Euler
    + Pi-ary
    + Sqrt 2
    + 12th root of two
  + Redundant binary representation (RBR)
  + Quote notation
  + Fibonacci coding
  + [Skew binary](MOAL/computer_organization/skew_binary.py)
  + Ostrowski numeration
  + Negative
    + Negabinary
    + Negadecimal
    + Negaternary
    + Negafibonacci
  + Mixed radix
    + [Factoradic](MOAL/computer_organization/factoradic.py)
  + Bijective
    + base-10
    + base-26
  + [1-adic bijective (tally)](MOAL/computer_organization/positional.py)
  + Johnson code
  + Gray code
    + n-ary
    + Balanced
    + Binary-reflected (BRGC)
    + Monotonic
    + Beckett–Gray
    + Snake-in-the-box
    + Single-track
+ Math
  + [Endianness (byte ordering)](MOAL/computer_organization/endianness.py)
  + [Binary](MOAL/computer_organization/data_types.py)
    + [Addition](MOAL/computer_organization/data_types.py)
    + [Subtraction](MOAL/computer_organization/data_types.py)
    + [Multiplication](MOAL/computer_organization/data_types.py)
    + [Division](MOAL/computer_organization/data_types.py)
    + Square root
    + [Bitwise operations](MOAL/computer_organization/bitwise_operations.py)
      + [XOR](MOAL/computer_organization/bitwise_operations.py)
      + [OR](MOAL/computer_organization/bitwise_operations.py)
      + [AND](MOAL/computer_organization/bitwise_operations.py)
      + [NOT](MOAL/computer_organization/bitwise_operations.py)
      + [Shifts](MOAL/computer_organization/bitwise_operations.py)
        + [Arithmetical](MOAL/computer_organization/bitwise_operations.py)
        + [Logical](MOAL/computer_organization/bitwise_operations.py)
        + [Rotate no carry](MOAL/computer_organization/bitwise_operations.py)
        + [Rotate through carry](MOAL/computer_organization/bitwise_operations.py)
  + [Bit field](MOAL/computer_organization/bit_field.py)
  + [Flag field](MOAL/computer_organization/bit_field.py)
  + [Bit Masking](MOAL/computer_organization/bitwise_operations.py)
+ Memory
  + Memory hierarchy
  + Virtual memory
  + Memory mapped I/O
  + Content-addressable memory
+ Synchronization primitives

## Operating Systems

+ Concurrency
  + Multi-tasking
    + Dining philosophers
    + Race condition
    + Futures / Promises
    + Deadlock
    + Lock
    + Barrier
    + Single reader multiple writer
    + Turnstile
    + Mutual exclusion (mutex)
    + Starvation
    + Priority inversion
    + Semaphores
  + Primitives
    + Process
    + Threads
      + Kernel
      + Green
      + POSIX
      + Models
        + Kernel level (1:1)
        + User level (N:1)
        + Hybrid (M:N)
    + Co-routines [language]
    + Tail call [language]
    + Fibers [system]
    + Continuation [language]
  + Schedulers
  + Producer / consumer
+ Memory management
+ File systems
+ Security
  + Protection ring
  + Supervisor
  + Hypervisor
  + Language based
+ System on a chip (SoC)
+ Inter-process communication
  * File
  * Signal
  * Socket
  * Message Queue
  * Pipe
    - Named
  * Semaphore
  * Shared memory
  * Message passing
  * Memory-mapped file

## Networking

+ Ethernet
+ Protocols
  * Application
    - LDAP
  + RPC
    + JSONRPC
    + XMLRPC
  + Bluetooth
  + Fibre channel
  + TCP / IP
  + RTPS
  + SSH
  + UDP
    + Twisted UDP
  + FTP/sFTP
    + Twisted FTP
  + SMTP
  + Telnet
  + HTTP/HTTPS
    + HTTP Servers
      + G-Unicorn
      + uWSGI
  + SSL
  + TLS
  + POP
  + E6
  + NTP
  + PPP
  + NNTP
  + IMAP
  + Bitcoin
  + Recursive network architecture (RNA)
  + Custom (make one!)
+ Load balancing
  + NGINX
  + Apache
  + HAProxy
+ Administration
  + Software defined
+ WWW
  * Semantic Web
    - RDF
    - RDFS
    - SKOS
    - SPARQL
    - Notation3
    - N-Triples
    - Turtle
    - OWL
    - RIF
    - Unifying Logic and Proof layers

## Data Storage / Transmission

+ Storage
  + Search Server
    + [Elastic Search](MOAL/storage/search/elasticsearch_db.py)
    + Apache Drill
    + Lemur
    + Lucene
    + Solr
    + Sphinx
    + Xapian
    + Terrier Search Engine
  + Databases
    + Relational
      + MySql
      + [PostgreSql](MOAL/storage/databases/relational/postgresql_psycopg2.py)
        * [Psycopg2](MOAL/storage/databases/relational/postgresql_psycopg2.py)
    + Key/value
      + [Redis (doc + k/v)](MOAL/storage/databases/keyvalue/redis_db.py)
      + Accumulo
    + Document
      + [MongoDB](MOAL/storage/databases/document/mongo_db.py)
      + CouchDB
    + Graph
      * TinkerPop (interfacing)
      + Neo4j
      * Titan
      * Giraph
    + WideColumn
      + HBase
      + BigTable
    + Data structures
      + Inverted Index
    + Services
      * BigQuery
      * Datomic
    * Other
      - InfluxDB
      * hustle
+ Serialization
  + Avro
  + CSV
  + JSON
  + MessagePack
  + Protocol Buffers
  + S-expressions
  + YAML
  + Custom (make one!)
+ Modeling
  + SPICE
  + CMMI
  + Data model
  + ER model
  + Function model
  + Information model
  + Meta modeling
  + Object model
  + Systems model
  + View model
+ Transformation
  + Migration
  + Conversion
  + Metadata
    + Descriptive
    + Structural

## Systems Engineering

+ Architecture
  + Model driven (MDA)
  + MVC / N-Tier
  + Aspect oriented system
  + Middleware
    * Application
    * Distributed
  + SOA
    + Micro-services
  + RESTful API
    + Basic
    + HATEOAS
  + API design
    * JSONAPI (jsonapi.org)
    + Fluent interface
+ Parallel Computing
+ Distributed Computing
  * Fault-tolerance
  * Self-stabilization
  + Peer-to-Peer (P2P)
    + Structured
    + Unstructured
  + CAP Theorem
  + "Big Data" processing
    + Hadoop file system
    + Hadoop MapReduce
    + Kafka
    + Storm
    + PIG
    + ZooKeeper
      + Kazoo
    + Lucene
+ Message queuing
  + RabbitMQ
  + ZeroMQ
+ Performance
  + Caching
    + Varnish
    + [Memcached](MOAL/systems_engineering/performance/caching/memcached_example.py)

## Artifical Intelligence

+ Machine learning
  + Supervised learning
    + Decision tree
    + Perceptrons
    + Support vector machines
    + K-means clustering
    + Bayesian probability
    + Neural networks
      + Self-organizing map (Kohonen map)
      - Neocognitron
      * ADALINE
        - MADALINE
      + Adaptive Resonance Theory
        + ART 1
        + ART 2
        + ART 2-A
        + ART 3
        + Fuzzy ART
        + ARTMAP
        + Fuzzy ARTMAP
      + Recurrent (RNNs)
        + Boltzmann machine
        + Backpropagation
        + Hopfield
        + Elman
        + Jordan
        + Echo state
        + Long short term memory
        + Bi-directional
        + Continuous-time
        + Hierarchical
        + Recurrent multilayer Perceptron
        + Second order
        + Pollack's sequential cascaded
        + Neural turing machines
        + Bidirectional associative memory (BAM)

## Robotics & Electronics

+ Arduino
  * Firmata
    - (via) Johnny Five
+ Raspberry Pi
+ HDLs
  + Analog
  + Digital circuit
    + Verilog

## Graphics

+ /TBD/

## Theory of Computation

+ Automata theory
  + Continuous spatial automata
  + Cellular automata
    + Reversible
    + Totalistic
    + Von Neumann universal constructor
    + Nobili
  + Abstract machine
    + Pushdown automata
      + Generalized
    + [Turing machine](MOAL/automata_theory/turing_machine.py)
      + [Universal](MOAL/automata_theory/universal_turing_machine.py)
      + [Decider / Total](MOAL/automata_theory/turing_machine.py)
      + Alternating
      + Quantum
      + Non-deterministic
      + Read-only
      + Read-only right moving s
      + Probabilistic
      + Multi-tape
      + Multi-track
    + Stack machine
    + Register machine / Wang-b machine
      + [Pointer](MOAL/automata_theory/pointer_machine.py)
        + [Schonhage Storage Modification](MOAL/automata_theory/pointer_machine.py)
        + [Kolmogorov-Uspenskii](MOAL/automata_theory/pointer_machine.py)
        + Knuth's Linking Automaton
        + Atomistic Pure-LISP (APLM)
        + Atomistic Full-LISP (AFLM)
        + General atomistic
        + Jone's I Language 1
        + Jone's I Language 2
      + [Counter](MOAL/automata_theory/counter_machine.py)
        + [SheperdsonSturgis](MOAL/automata_theory/counter_machine.py)
        + [Minsky](MOAL/automata_theory/counter_machine.py)
        + Program
        + [Abacus](MOAL/automata_theory/counter_machine.py)
        + Lambek
        + Successor
        + SuccessorRAM
        + ElgotRobinsonRASP
      + Random-access stored-program
      + Random access
      + Cell probe
  + Finite State Machines (FSM)
    + Transducers
    + Acceptors
    + Classifiers
    + Sequencers
    + Markov chain
    + Regular expressions
    + Richards controller
    + Moore
    + Mealy
    + Levenshtein automaton
+ Computational complexity
  + Classes
    + P
    + NP
    + #P
    + BPP
    + PSPACE
+ PCPs
+ Circuit lower bounds
+ Arithmetic complexity
+ Quantum complexity
+ Communication complexity
+ Unique Games Conjecture

## Languages

+ Interesting language features / syntactic sugar (format: Language - feature)
  + Python - generator
    + recursive
    + expression
  + Python - decorator
    * Class
    * Method
  + [Python - context manager (with)](MOAL/languages/features/python/context_manager.py)
  + [Python - variable packing/unpacking](MOAL/languages/features/python/packing_unpacking.py)
  + [Python - index slicing](MOAL/languages/features/python/index_slicing.py)
  + [Python - comprehensions](MOAL/languages/features/python/comprehensions.py)
  + Rust - de-structuring
  + Rust - pattern matching
  + Haskell - pattern matching
  + Haskell - monads
  + Haskell - guards
  + Haskell - comprehensions
  + Haskell - refinement types
+ Evaluation strategies
  + Eager
  + Lazy
  + Partial
  + Remote
  + Short-circuit
+ Formal language theory
  + Modeling language
    + Algebraic (Pyomo)
    + Behavioral
    + Discipline-Specific
    + Domain-specific
    + Framework-specific
    + Object-oriented
    + reality
    + Others
    + [Dyck language](MOAL/languages/formal_language_theory/modeling/dyck.py)
  + Formal grammars
    + Link
    + Tree-adjoining
    + [Recursive](MOAL/languages/formal_language_theory/grammars/attribute_context_free.py)
    + Regular
    + [Analytic](MOAL/languages/formal_language_theory/grammars/analytic_context_free.py)
      * Parsing Expression (PE)
    + [Context-sensitive](MOAL/languages/formal_language_theory/grammars/context_sensitive.py)
    + [Context-free](MOAL/languages/formal_language_theory/grammars/context_free.py)
      + Stochastic
      + [Attribute](MOAL/languages/formal_language_theory/grammars/attribute_context_free.py)
      + Adaptive
        + Recursive (RAGs)
        + Dynamic Template Translators
        + Christiansen
        + Wegbreit
        + Dynamic
        + Meta-S calculus
        + Imperative
        + Declarative
        + Hybrid / Time-space
      + [Ambiguous](MOAL/languages/formal_language_theory/grammars/context_free.py)
      + [Chomsky normal form](MOAL/languages/formal_language_theory/grammars/context_free.py)
      + [Backus-Naur Form (BFN)](MOAL/languages/formal_language_theory/grammars/backus_naur.py)
        + Extended
+ Paradigms
  * Parallel
    - Languages
      - Chapel (language)
  + Functional
    + Languages
      + Haskell
      + OCaml
      + Lisp
      + Clojure
      + Python
        * PyMonad
    + Features
      + Functional Parametric polymorphism
  + Logic
    + Abductive
    + Answer set
    + Constraint
    + Functional
    + Inductive
    + Prolog
  + Object-oriented
    + Features
      + [Class hierarchy](MOAL/languages/paradigms/object_oriented/oop_classes.py)
      + [Static, class, & abstract methods](MOAL/languages/paradigms/object_oriented/oop_classes.py)
        + [Abstract Base Classes](MOAL/languages/paradigms/object_oriented/abstract_baseclass.py)
      + Overloading
      + Polymorphism
        + Operator overloading
        + Function overloading/ad-hoc polymorphism
        + Parametric polymorphism
        + Single / Dynamic dispatch
        + Double dispatch
        + Multiple dispatch
        + Static binding
        + Virtual function
        + Sub-typing
        + Static / Dynamic binding
  + Array programming
    + J
  + Meta-programming
    + Languages
      + Racket
      + Scheme
  + Template meta-programming
  + Automatic
    + Program synthesis
  + Dataflow
    + Flow based
    + Cell-oriented
    + Reactive
    + Pipeline
      + Hartmann
      + [UNIX](MOAL/languages/paradigms/dataflow/pipelines/unix_cmds.sh)
  + Stream processing
  + Concurrent
    + Languages
      + GO
      + Rust
      + Nimrod
      + Mozart
  + Extensible
  + Domain Specific (DSL)
    + Metalinguistic abstraction
    + [Embeddable](MOAL/languages/domain_specific/embedded_dsl.py)
    + Macros
      + Hygienic
      + Anaphoric
      + Text Substitution
        + Sublime plugin
    + Templating language (make one!)

## Type theory

+ Type systems
  + Type safety
  + Type checking
      + Dynamic
      + Static
  + Inferred
  + Manifest
  + [Nominal](MOAL/type_theory/nominal_structural.py)
  + [Structural](MOAL/type_theory/nominal_structural.py)
  + Dependent
  + [Duck](MOAL/type_theory/duck.py)
  + Gradual
  + Latent
  + Sub-structural
  + Uniqueness
  + Strong
  + Weak

## Program Execution

+ Emulator
  + Binary translation
  + Hardware
  + In-circuit
  + Server
  + Terminal
  + Network
  + Instruction set
  + Video game console
  + Semulation
  + Logic simulation
+ Processing units
  + CPU
    + Architectures
      + Very long instruction word (VLIW)
      + Complex instruction set computing (CISC)
      + Fetch
      + Decode
      + Execute
  + Control unit
  + ALU
  + AGU
  + APU
  + Vector processor
  + Field Programmable Gate Array (FPGA)
  + Microprocessor
    + Reduced instruction set computing (RISC)
+ Runtime system
  + Specific runtimes
    + Android Runtime (ART)
    + crt0
    + Common Language Runtime (CLR)
    + Dalvik
    + Java virtual machine (JVM)
+ Runtime library
+ Executable
+ Compilation
  + Assembler
  + Linker
  + Compile farm
    + GCC Compile farm
+ Compiler
  + Software
    + Semantics encoding
    + Meta-compilation
    + Source-to-source (transpiler)
    + Binary recompiler
    + One pass
    + Multi pass
    + Front end
    + Back end
    + Implementations
      + PL/0
      + Psyco
      + Cython
      + PyPy
      + GCC
      + Clang
    + Custom (make one!)
    + Symbol table
    + [Abstract Syntax Tree (AST)](MOAL/execution/compiler/abstract_syntax_tree.py)
    + Abstract semantic graph
    + Components
      + Parser
        + Top down
            + LL(1)
            + LL(k)
              + Simple
              + Look-Ahead / LALR
        + Bottom up
          + Backtracking
          + Shift-reduce
        + Recursive descent
      + Lexer
        + Tokenizer
        + Lexical grammar generation
        + Scanner
        + Evaluator
        + Lexer generator
+ Interpreter
  + Bytecode interpreters
  + Abstract Syntax Tree interpreters
  + Just-in-time compilation
  + Self-interpreter
+ Virtual machine
  + [Process](MOAL/execution/virtual_machine/process_vm.py)
  + System
  + Dynamic recompilation
  + Hardware-assisted virtualization
  + p-code machine
+ Source code
+ Object code
+ Bytecode
+ Machine code
  + [Opcode](MOAL/execution/machine/opcodes.py)
  + Assembly language
    + Assembler concept
    + Languages
      + ARM
      + MIPS
      + x86
      + 6502

## Other resources / references

### Requirements list for BCS
wikipedia.org/wiki/Bachelor_of_Computer_Science

### Other resources

*Wikipedia*
+ https://en.wikipedia.org/wiki/List_of_important_publications_in_computer_science
+ https://en.wikipedia.org/wiki/Analysis#Computer_science
+ https://en.wikipedia.org/wiki/Central_processing_unit
+ https://en.wikipedia.org/wiki/System_on_a_chip
+ https://en.wikipedia.org/wiki/Programming_paradigm
+ https://en.wikipedia.org/wiki/List_of_algorithms
+ https://en.wikipedia.org/wiki/NoSQL
+ https://en.wikipedia.org/wiki/Evaluation_strategy
+ https://en.wikipedia.org/wiki/Machine_learning
+ https://en.wikipedia.org/wiki/Recurrent_neural_network
+ https://en.wikipedia.org/wiki/Register_machine
+ https://en.wikipedia.org/wiki/Cellular_automaton
+ https://en.wikipedia.org/wiki/Turing_machine
+ https://en.wikipedia.org/wiki/Static_program_analysis
+ https://en.wikipedia.org/wiki/Lists_of_network_protocols
+ https://en.wikipedia.org/wiki/Communications_protocol
+ https://en.wikipedia.org/wiki/Software_development_process
+ https://en.wikipedia.org/wiki/Software_testing#Testing_methods
+ https://en.wikipedia.org/wiki/Cipher
+ https://en.wikipedia.org/wiki/Type_theory
+ https://en.wikipedia.org/wiki/Remote_procedure_call
+ https://en.wikipedia.org/wiki/Inter-process_communication
+ https://en.wikipedia.org/wiki/Performance_engineering
+ https://en.wikipedia.org/wiki/Persistent_data_structure
+ https://en.wikipedia.org/wiki/Software_design_pattern
+ https://en.wikipedia.org/wiki/Category:Formal_languages
+ https://en.wikipedia.org/wiki/Retroactive_data_structures
+ https://en.wikipedia.org/wiki/Linear_programming
+ https://en.wikipedia.org/wiki/Modeling_language
+ https://en.wikipedia.org/wiki/Formal_grammar#The_Chomsky_hierarchy
+ https://en.wikipedia.org/wiki/LL_parser
+ https://en.wikipedia.org/wiki/List_of_programming_languages_by_type#Machine_languages
+ https://en.wikipedia.org/wiki/Comparison_of_data_serialization_formats
+ https://en.wikipedia.org/wiki/Thread_(computing)#Processes.2C_kernel_threads.2C_user_threads.2C_and_fibers
+ https://en.wikipedia.org/wiki/List_of_compilers
+ https://en.wikipedia.org/wiki/Logic#Types_of_logic
+ https://en.wikipedia.org/wiki/Discrete_mathematics
+ https://en.wikipedia.org/wiki/Hardware_description_language
+ https://en.wikipedia.org/wiki/Symbol_table
+ https://en.wikipedia.org/wiki/Mathematics#Fields_of_mathematics
+ https://en.wikipedia.org/wiki/Lexical_analysis
+ https://en.wikipedia.org/wiki/Mathematical_logic
  + https://en.wikipedia.org/wiki/Set_theory#Areas_of_study
  + https://en.wikipedia.org/wiki/Proof_theory
  + https://en.wikipedia.org/wiki/Computability_theory#Areas_of_research
  + https://en.wikipedia.org/wiki/Model_theory
+ https://en.wikipedia.org/wiki/List_of_data_structures
+ https://en.wikipedia.org/wiki/List_of_numeral_systems
  + https://en.wikipedia.org/wiki/Factorial_number_system
  + https://en.wikipedia.org/wiki/Gray_code
  + https://en.wikipedia.org/wiki/Bitwise_operation
+ https://en.wikipedia.org/wiki/Coding_theory
+ https://en.wikipedia.org/wiki/Aspect-oriented_software_development
+ https://en.wikipedia.org/wiki/GRASP_(object-oriented_design)

*Misc*
+ fullstackpython.com/table-of-contents.html
+ interactivepython.org/
+ refactoring.com/catalog/
+ anandology.com/python-practice-book

### Optional reading:
+ *Introduction to Algorithm Design* - Jon Kleinberg and Eva Tardos
+ *Introduction to Algorithms CLRS (MIT)*
+ *Purely functional data structures* - Chris Okasaki
+ *The Language of Machines: An Introduction to Computability and Formal Languages* - Robert W. Floyd, Richard Beigel

### Notes, Q/A, research
+ www.stackoverflow.com/questions/2487576/trie-vs-suffix-tree-vs-suffix-array
+ research.microsoft.com/en-us/um/people/gurevich/Opera/78.pdf
+ symbolicanalysis.wordpress.com/category/other-methodologies/turing-machine-and-related-automata/
+ github.com/boyers/theorem_prover
+ symbolicanalysis.wordpress.com/2009/12/15/propositional-directed-acyclic-graph-pdag-vs-aho/
+ quora.com/What-is-the-difference-between-Top-Down-parsing-and-Bottom-up-parsing-in-programming-languages
+ github.com/raganwald-deprecated/homoiconic/blob/master/2009-10-08/metalinguistic.md
+ www.youtube.com/watch?v=0JXhJyTo5V8
+ echo.co/blog/os-x-1010-yosemite-local-development-environment-apache-php-and-mysql-homebrew
+ www.stackoverflow.com/questions/9624774/after-mysql-install-via-brew-i-get-the-error-the-server-quit-without-updating
+ https://en.wikipedia.org/wiki/Unix_philosophy#Eric_Raymond.E2.80.99s_17_Unix_Rules
+ www.youtube.com/playlist?list=PLFDnELG9dpVxEpbyL53CYebmLI58qJhlt
+ www.scriptol.com/programming/list-algorithms.php
+ www.wisegeek.com/what-is-a-free-list.htm
+ www.youtube.com/watch?v=ED2iJXkdhCQ
+ www.slideshare.net/AlexRomanoff/introduction-to-pairwise-testing-31094064
+ www.catb.org/esr/writings/taoup/html/ch01s06.html
+ www.cs.unc.edu/~stotts/COMP145/cohesion.html
+ zedshaw.com/archive/indirection-is-not-abstraction/
+ www.cs.mun.ca/~harold/Courses/Old/CS3716.W12/Diary/Rod/grasp2/grasp2.html
+ https://en.wikipedia.org/wiki/Semantic_Web
+ https://developer.ridgerun.com/wiki/index.php/How_to_generate_sphinx_documentation_for_python_code_running_in_an_embedded_system#Edit_index.rst
+ http://scriptsonscripts.blogspot.com/2012/09/quick-sphinx-documentation-for-python.html
+ www.crypto101.io/
+ https://en.wikipedia.org/wiki/List_of_hash_functions
+ http://kmcallister.github.io/talks/rust/2015-dependent-types/slides.html
+ http://chimera.labs.oreilly.com/books/1230000000929/index.html
+ https://www.fpcomplete.com/user/konn/prove-your-haskell-for-great-safety/dependent-types-in-haskell
+ http://rustbyexample.com
+ http://www.alpcentauri.info/heightmaps.html
