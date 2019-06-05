# UGA2019
Repository for Grenoble Projects in 2019

## Members

- Masahide Nakamura (Kobe-U)
- Florian Carrio (UGA)
- Bastien Zigmann (UGA)
- Quentin Guerre-berthelot (UGA)
- Lucas Gisselaire (UGA)
- Lydie du Bousquet (UGA)

## Project Goal

Develop concepts, architectures, and methods that can assure the quality, 
reliablity, and security for __machine-learning-based software (MLSW)__.


## Definition of MLSW
Just for convinience, we first focus on _supervised_ machine learning only.

MLSW is a software _S_ such that:
- _S_ contains a __model__ _M_ derived by a machine-leraning process
- _S_ takes data _D = (d1, d2, ..., dn)_ as an input
- _S_ obtains a prediction _y = M(d1, d2, ..., dn)_ based on the model _M_ and the input data _D_
- _S_ performs a sequence of actions _ACT(y)= [a1(y); a2(y); ... ; an(y)]_ based on the prediction y 

<img src="./concept_drawing.png">


## Approach
1. Consider motivating examples.
1. Investigate risks and threats.
1. Develop methods to cope with the risks and the threats.
1.

### [Quentin App (Breast Cancer Diagnosys)](./BreastCancer/note.md)
	

### White wine quality prediction (Lucas)
1. Project motivation:

	My idea is to create a model which tries to assign a quality indicator (subjective) to a wine bottle depending on the physical (objective) properties of the bottle. 
	By computing the quality of a given bottle, wine resellers may be able to infer the popularity of said bottle without relying on market studies or other non-automatic models which may very well be both less accurate and more expensive.

2. Risk study:

	While the concept seems interesting on paper, we can easily think of multiple things that can go wrong or induce other problems. Namely:

	* The quality prediction is straight-up wrong:

		While prediction models do use some of the initial data for testing which makes the model more robust, wrong predictions CAN definitely occur because of the model's non-deterministic nature.

	* Input fed to the model is too different from training data:

		Because of the relatively low sample size of the initial dataset (~5000 rows), it is easy to imagine that a bottle fed to the model has physical properties very much different from those of the initial dataset. This disparity may in turn induce a wrong prediction.

	* Web (remote) service is unavailable or compromised:

		The application relies on a remote service to make its predictions; if the service becomes unavailable or compromised, then either no predictions will be able to be made whatsoever, or the predictions will have no value.
		
3. Minimizing the risks:

	Because the model is unpredictable by nature, it is clear that the probability of a problem occuring will never be null; however, I will try looking into ways to minimize the risks I recognized in the last step:

	* Wrong prediction:

		On top of the prediction, a "prediction quality indicator" could be computed to judge the quality of a prediction; for example, a bottle of quality 5.5 with 99% accuracy may be safer/more marketable than a bottle of quality 6.5 with 10% accuracy. All in all, this would probably give more sense & value to a prediction.

	* "Bad" input:

		To prevent users from trying to predict the quality of bottles that the model may not be able to properly handle, I could limit the input to certain pre-determined intervals so as to ensure that the input data is kept in the range of the initial training data. In the same fashion, I could compute a "data ressemblance" factor and only accept inputs within a given range to feed the model.

	* Web service reliance:

		- Warn the user when the service becomes unreachable.
		- Add security mechanisms (key-based encryption & authentification) to ensure that the prediction is reliable.

### Florian's Application : Student Performance Prediction 

1. Project motivation : 

To stay in the theme, I chosen to study the differents factors which affects a student during his scholar year. For this, I finded an interesting dataset about India's students informations, with a column which indicates the "End semester Percentage", in another words, if a student will pass achieve the university year. That's the most interesting field, so we'll try to predict it.
It could be a very interesting algorithms for all Indian Universitys which wants to select the students who deserve the most.

2. Risk & Threats Investivation

Evidently, all applications of this kind needs to be secured on all there differents modules/services that it is used.
So here is all of my investigation results : 

- All the datas needs to be set and correctly set

- Internet connection needs to be ok

- API Key for Azure Machine Learning needs to be encrypted

- To go further, an implementation of signatures messaging to compare them between the emission and reception of datas could be interesting
( to avoid data tampering )

3. Security Implementation

So to implements all of the security issues above, here is my plan :

- To be sure that all the data are present with integrity I opted for Listbox selection with Tkinter, thus pre-defined data needs to be selected also.

- About Internet connection, a simple check to azure website in python is enough.

- For the API Key privacy, I stored it in a private local file.

- To go further, Azure Keyvault looks like very interesting to verify signatures between messages.

## Deliverables

- Quentin App : run the script [StartBCancerDiagnosys.sh](./StartBCancerDiagnosys.sh)

- [Application Examples](./examples/)




