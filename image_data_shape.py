import nibabel as nib

nii_file_path = 'path_to_your_nii_file.nii'
nii_image = nib.load('ADNI_RESIZED/ADNI_002_S_0295_MR_MPR__GradWarp__B1_Correction_Br_20070219174038655_S21856_I40967.nii')
image_data = nii_image.get_fdata()

print("Dimensions of the NIFTI image:", image_data.shape)

