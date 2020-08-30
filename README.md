# kaggle-osic
Predicting prognosis in patients with pulmonary fibrosis.  
![gifofimage](./imgs/sample.gif)
#### What is pulmonary fibrosis?  
[Pulmonary fibrosis](https://www.mayoclinic.org/diseases-conditions/pulmonary-fibrosis/symptoms-causes/syc-20353690) is a lung disease that occurs when lung tissue becomes damaged and scarred. This makes it more difficult for lungs to work properly.

In [this](https://www.kaggle.com/c/osic-pulmonary-fibrosis-progression) competition, we predict a patient’s severity of lung function based on a CT scan of their lungs. We’ll determine lung function based on output from a spirometer, which measures the volume of air inhaled and exhaled. The challenge is to use machine learning techniques to make a prediction: final three FVC measurements for each patient, as well as a confidence value in the prediction.   

What is Forced vital capacity (FVC)?    
FVC is the amount of air that can be forcibly exhaled from your lungs after taking the deepest breath possible, as measured by spirometry.  

### Metric.  
The evaluation metric of this competition is a modified version of Laplace Log Likelihood. In medical applications, it is useful to evaluate a model's confidence in its decisions. Accordingly, the metric is designed to reflect both the accuracy and certainty of each prediction.  
For each true FVC measurement, an FVC and a confidence measure (standard deviation σ) are predicted.   

The metric is computed as follows:  
  <img src="https://render.githubusercontent.com/render/math?math=metric = -\frac{\sqrt{2} \Delta}{\sigma_{clipped}} - \ln ( \sqrt{2} \sigma_{clipped} )">  
  where,
  <img src="https://render.githubusercontent.com/render/math?math=\sigma_{clipped} = max(\sigma, 70),"> and
  <img src="https://render.githubusercontent.com/render/math?math=\Delta = min (\Big|FVC_{true} - FVC_{predicted}\Big|, 1000 )">    
  
Predicting an FVC value with high error and low standard deviation leads to large penalties; while predicting with high standard deviation penalises less, relatively. The error is thresholded at 1000 ml to avoid large errors adversely penalising results, while the confidence values are clipped at 70 ml to reflect the approximate measurement uncertainty in FVC. The final score is calculated by averaging the metric across all test set Patient_Weeks (three per patient).
The metric values will be negative and *higher* is better.

  


  





