# Discussion on 2019-06-04

- 15:00-18:30
- with Prof. Francois Portet

## Presentation of the individual applications
- Frolian: Indian students
- Bastien: Men Felitry
- Quentin: Breast Cancer Prediction
- Lucas: White wine quality assessment

## Generalizing the problem
Find the common/similar parts of risks and threats

<img src="http://133.30.159.3:8080/capybara/api/img/5cf61109342cf20c814369d7.png">

## Important mechanisms to address the risk

Online monitoring of
1. Data compatibility
  - The input data should be compatible with the one used in model
1. Action performed
  - The action performed should be tolerance for the environment
1. Confidence of prediction
  - In addition to yes/or, the model should give the probability of confidence.
  - If the confidence is low, the system can delegate the decision to the user.
1. Pool of the data
  - The system should pool the data so that the characteristics of the input data
    are still maintained from the original dataset.
  - The security and privacy issues must be addressed.

## Anticipated Threats

Threats = A bad situation brought by adversaries

1. Substitution
1. Tampering
   - data, model, algorithms
1. Information leakage
   - hack the data pool 
1. Denial of Service (DoS)
   - DoS attacks to Web apps
   - DoS attacks to Azure

[Back to README](../README.md]
