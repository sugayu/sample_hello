==========
Quickstart
==========


This is the first step of Python programming!
=============================================

When you start to learn new computing language, it's a nice idea to say
hello to the new world.

.. code:: ipython

   import sample_hello
   sample_hello.world()

This is the best greeting ever.

running codes
-------------

This code runs when exporting to reST from the emacs-org document.

.. code:: python

   import numpy as np
   a = np.arange(10)
   return a

.. raw:: org

   #+results: test-code

.. container:: RESULTS drawer

   [0 1 2 3 4 5 6 7 8 9]

Test of equations
=================

We would like to write mathematics like
:math:`\chi^2 = \left[ (D - M)/\sigma \right]^2` and

.. math::

   \begin{equation}
   \label{eq:1}
   \chi^2 = \left( \frac{D-M}{\sigma} \right)^2,
   \end{equation} \qquad (1)

where :math:`D` is the data, :math:`M` the model, and :math:`\sigma` is
the uncertainty.

Test of writing
===============

List
----

-  This is the first.
-  This is the second.
-  This is the third.

List 2
------

First
   This is the first.
Second
   This is the second.
Third
   This is the third.

Table
-----

========= === ====
Name      SFR Mass
========= === ====
Galaxy    1   11
B14-65666 200 10
Human     0   -29
========= === ====

directives
==========

.. note::

   This is note.

.. warning::

   This is warning.

.. caution::

   This is caution.

.. important::

   This is important.

.. tip::

   This is tip.

.. hint::

   This is hint.

.. attention::

   This is attention.

.. danger::

   This is danger.
