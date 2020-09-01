def dicom_to_df(is_first_half):
    '''
    extracting metadata from dicoms to dataframes usinf fastai
    :parameters: is_first_half(boolean) if true process first half of patients, else process second half; required due to memory constraints.
    '''
    !pip install torch torchvision feather-format kornia pyarrow --upgrade  > /dev/null
    !pip install git+https://github.com/fastai/fastai2 > /dev/null
    from fastai2.basics import *
    from fastai2.medical.imaging import *
    import os
    train_dir = '../input/osic-pulmonary-fibrosis-progression/train'
    all_patients_dicom_dir = os.listdir(train_dir)
    all_patients_dicom_dir = [*map(lambda patientid:os.path.join(train_dir,patientid),all_patients_dicom_dir)]
    len(all_patients_dicom_dir),all_patients_dicom_dir[0]
    %time 
    dicom_dfs = []
    if is_first_half:
        all_patients_dicom_dir=all_patients_dicom_dir[:88]
        filename='first_half.csv'
    else:
        all_patients_dicom_dir=all_patients_dicom_dir[88:]
        filename='last_half.csv'
    for patient_dicom_folder_path in tqdm(all_patients_dicom_dir):
        path = Path(patient_dicom_folder_path)
        fns_trn = path.ls()
        df_trn = None
        df_trn = pd.DataFrame.from_dicoms(fns_trn, px_summ=True)
        dicom_dfs.append(df_trn)
    pd.concat(dicom_dfs).to_csv(filename)
