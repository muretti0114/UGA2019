#!/bin/bash
echo
echo '##########################################################################'
echo 'The App for the diagnosys of Brest Cancer is lunch'
echo 'python version : 3'
echo '##########################################################################'
echo
echo 'few things to know :'
echo
echo '- To run the App successfully you will need the Security file <SecuAccess> '
echo 'store in BreastCancer file.'
echo
echo '- On the main page there are some text field, the easiest way to field them,'
echo 'is to field the text field that take a list of values and automaticly field '
echo 'all the other ones.'
echo
echo '- there is a sample of values in the file <wdbc.data> the explications of this'
echo 'sample is in the file <wdbc.names>.'
echo

cd BreastCancer/Apps/
python diagnosys.py