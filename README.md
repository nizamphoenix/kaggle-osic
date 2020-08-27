# kaggle-osic
Predicting prognosis in patients with pulmonary fibrosis.  

#### What is pulmonary fibrosis?  
[Pulmonary fibrosis](https://www.mayoclinic.org/diseases-conditions/pulmonary-fibrosis/symptoms-causes/syc-20353690) is a lung disease that occurs when lung tissue becomes damaged and scarred. This makes it more difficult for lungs to work properly.

In [this]() competition, we are asked to predict a patient’s severity of lung function based on a CT scan of their lungs. We’ll determine lung function based on output from a spirometer, which measures the volume of air inhaled and exhaled. The challenge is to use machine learning techniques to make a prediction with the image, metadata, and baseline FVC as input obtained from DICOM files of the CT scan.

### Metric.  
The evaluation metric of this competition is a modified version of Laplace Log Likelihood. 
