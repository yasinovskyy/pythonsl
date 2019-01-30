Syntax overview
===============

Python is a general-purpose object-oriented language. Python code is meant to be read by humans and many language design decisions are made with readability in mind.

Once you get used to the Python way of using indentation to group statements [#indentation]_, you realize the language syntax is similar to many other programming languages.

Python uses many keywords that can be found in other languages. ``and``, ``break``, ``class``, ``continue``, ``else``, ``for``, ``if``, ``not``, ``or``, ``return``, ``try``, and ``while`` can be used same way as in C, C++, and Java. Just like in other languages, Python `keywords <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ cannot be used as identifiers.


Variables and Expressions
-------------------------

Here is an example of a variable assignment and increment. You don't have to declare type of a variable, yet ``x`` is going to be treated as an integer. Notice that the ``print`` statement in line 8 does not change the value of ``x``, but the assignment in line 10 does.

.. literalinclude:: ../../src/syntax/variables.py
   :emphasize-lines: 8-9
   :linenos:
 
Here is the output of this code fragment:

.. literalinclude:: ../../src/syntax/variables.txt
   :language: none

.. warning::

    Expressions like ``++x``, ``x++``, ``--x``, and ``x--`` may be legal in certain contexts, but their behavior is not the same as in other languages [#increment]_. Don't use them.

Conditions
----------

Python structures ``if..else`` and ``if..elif..else`` are used to create conditional branches in a program. ``elif`` serves the same purpose as ``else if`` is other languages.

.. literalinclude:: ../../src/syntax/conditions.py
   :linenos:
 
Here is the output of this code fragment:

.. literalinclude:: ../../src/syntax/conditions.txt
   :language: none

Ternary conditional expression was added to Python 2.5 [#ternary]_.

.. literalinclude:: ../../src/syntax/conditions-ternary.py
   :linenos:
 
Here is the output of this code fragment:

.. literalinclude:: ../../src/syntax/conditions-ternary.txt
   :language: none

.. note::

    There is no ``switch`` statement in Python [#switch]_. Use ``if..elif..else`` instead.


Loops
-----

``while`` loop if usually used when the condition can change based on user input.

.. literalinclude:: ../../src/syntax/loops-while.py
   :linenos:

Assuming the user enters *boo*, *foo*, and *secret*, the output of this fragment is as follows:

.. literalinclude:: ../../src/syntax/loops-while.txt
   :language: none

``for`` is usually used to iterate over a sequence of known length (e.g. a string, a range, a collection).

.. literalinclude:: ../../src/syntax/loops-for.py
   :linenos:

The output is each letter of the word on a separate line.

.. literalinclude:: ../../src/syntax/loops-for.txt
   :language: none

``range`` takes first value, last value, and the step (positive or negative) as parameters. Remember that the last value is not included in the range.

.. literalinclude:: ../../src/syntax/loops-for-range.py
   :linenos:

Here is the output of this code fragment:

.. literalinclude:: ../../src/syntax/loops-for-range.txt
   :language: none

If you have some code that needs to run once the loop exits **successfully**, use ``for..else``.

.. literalinclude:: ../../src/syntax/loops-for-else.py
   :linenos:

The loop exits successfully and the ``else`` clause is executed.

.. literalinclude:: ../../src/syntax/loops-for-else.txt
   :language: none

Compare it to the following fragment:

.. literalinclude:: ../../src/syntax/loops-for-else-break.py
   :linenos:

The loop breaks and the ``else`` clause is not executed.

.. literalinclude:: ../../src/syntax/loops-for-else-break.txt
   :language: none

.. note::

    There is no ``do..while`` loop in Python [#dowhile]_.


Functions
---------

Consider the following function definitions and invocations:

.. literalinclude:: ../../src/syntax/functions.py
   :emphasize-lines: 11
   :linenos:
 
Notice that the line 11 does not cause any errors, but it doesn't produce any output either. Here is the output of this code fragment:

.. literalinclude:: ../../src/syntax/functions.txt
   :language: none

Here is another example of a valid Python code that does not produce the expected output:

.. literalinclude:: ../../src/syntax/functions-unexpected.py
   :emphasize-lines: 5
   :linenos:

Here is the output of this code fragment:

.. literalinclude:: ../../src/syntax/functions-unexpected.txt
   :language: none

Previous example illustrates some *unexpected* behavior but you have to remember that in Python functions can be passed as arguments to other functions.

.. literalinclude:: ../../src/syntax/functions-objects.py
   :emphasize-lines: 9-11
   :linenos:
 
Functions ``hello`` and ``bye`` are passed to the function ``say`` and later are invoked with each name as an argument.

.. literalinclude:: ../../src/syntax/functions-objects.txt
   :language: none

Functions don't have to be declared, which is very convenient if you are not planning to reuse them. Such anonymous functions can be created on-the-fly using ``lambda``.

.. literalinclude:: ../../src/syntax/functions-lambda.py
   :linenos:
 
This fragment of code prints the ``roster``, first sorted in alphabetical order and then by the length of the words:

.. literalinclude:: ../../src/syntax/functions-lambda.txt
   :language: none

You can specify default argument values when defining a function. This way, if a function is invoked without an argument, its default value is going to be used.

.. literalinclude:: ../../src/syntax/functions-arguments.py
   :emphasize-lines: 6
   :linenos:
 
Here is the output of this code fragment:

.. literalinclude:: ../../src/syntax/functions-arguments.txt
   :language: none

.. warning::

    Functions are evaluated when defined, not when they are called. This can lead to unexpected behavior when the default value of a parameter is a mutable object [#control]_.


File I/O
--------

Consider the following input file:

.. literalinclude:: ../../src/syntax/files.in
   :language: none

We can read and process the content of the file using the following approach:
 
.. literalinclude:: ../../src/syntax/files.py
   :linenos:

``with`` makes sure that the file is properly closed when it's no longer needed.

Here is the output of this code fragment:

.. literalinclude:: ../../src/syntax/files.txt
   :language: none

Another way to read file content is to use method ``read``:

.. literalinclude:: ../../src/syntax/files2.py
   :linenos:

``[1:-1]`` at line 4 ignores the first (number) and the last (empty) lines of the input file.


.. rubric:: Footnotes

.. [#control] `4. More Control Flow Tools — Python 3.7.2 documentation <https://docs.python.org/3/tutorial/controlflow.html>`_
.. [#dowhile] `[Python-ideas] PEP 315: do-while <https://mail.python.org/pipermail/python-ideas/2013-June/021610.html>`_
.. [#increment] `Python IAQ: Infrequently Answered Questions <http://norvig.com/python-iaq.html>`_
.. [#indentation] `Why does Python use indentation for grouping of statements? <https://docs.python.org/3/faq/design.html#why-does-python-use-indentation-for-grouping-of-statements>`_
.. [#switch] `Why isn’t there a switch or case statement in Python? <https://docs.python.org/3/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python>`_
.. [#ternary] `[Python-Dev] Conditional Expression Resolution <https://mail.python.org/pipermail/python-dev/2005-September/056846.html>`_

.. index:: variable, loop, function
