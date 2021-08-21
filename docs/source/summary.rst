Summary
============

The project is divided in several sections.

Analyse
-------

My custom analysis functions are here. At the time, it only entails a function to calculate the highest posterior density from a distribution.

Datastructures
~~~~~~~~~~~~~~

Here are some useful pydantic datastructures that also act as an input for other functions in this package. The dataclasses are divided in two sections.

1. Questionnaires

  - These dataclasses entail all the necessary answers for a questionnaire, and also calculates their respective scores. Questionnaires currently implemented are:

    #. TOPICS

    #. Dejong Gierveld Loneliness Scale

    #. Wellbeing short-form

    #. Life Space Questionnaire

2. Networks data

   - A simple datastructure to capture a network structure with python datetime timestamps.
