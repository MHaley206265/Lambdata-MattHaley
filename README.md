# Lambdata-MattHaley
A collection of data science utility functions

## Functions
- has_null()
- train_val_test()

## Descriptions

### has_null
Takes in a dataframe (df) and returns a value of
True if the dataframe has null values or False if
the dataframe does not containe null values.

By default, this also prints a table showing which
features contain null values as well as how many null
values they contain. This cant be disabled by passing
in a False value for details.

### train_val_test
This function splits a dataframe into train, validation
and test sets.  By default it splits the dataframe 70%/15%/15%
into train, validation, and test respectively

## Reliances
pandas
scikit-learn